# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import uuid

from decimal import Decimal
from collections import OrderedDict
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.orm import relationship
from proj_extensions import db
from sqlalchemy.dialects.postgresql import JSON
from models.base import BaseModel
from models.user import User
from models.product import Product
from proj_exceptions import InvalidOrderStatusIdError, InvalidOrderStatusChange, InsufficientStockToSendOrder, \
    InconsistentDataBaseError, InvalidClientToOrder, InvalidOrderError
from proj_utils import SortMethodMap
from r import R


class Order(BaseModel):
    uuid = db.Column(db.String(R.dimen.uuid_length), nullable=False)
    client_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    client_email = db.Column(db.String(R.dimen.email_max_length), nullable=False)
    client = relationship("User", back_populates="orders")
    status = db.Column(db.Enum(R.id), default=R.id.ORDER_STATUS_PAID, nullable=False)
    paid_datetime = db.Column(db.DateTime, nullable=False)
    sent_datetime = db.Column(db.DateTime)
    delivered_datetime = db.Column(db.DateTime)
    amount_by_product_id = db.Column(JSON, nullable=False)
    products_total_price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    products_table_data = db.Column(db.JSON, nullable=False)
    total_table_data = db.Column(db.JSON, nullable=False)

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_CLIENT_EMAIL,         R.string.client_email,          asc(client_email)),
        (R.id.SORT_METHOD_NEWEST,               R.string.newest,                desc(paid_datetime)),
        (R.id.SORT_METHOD_OLDER,                R.string.older,                 asc(paid_datetime)),
        (R.id.SORT_METHOD_LOWER_TOTAL_PRICE,    R.string.lowest_price,          asc(products_total_price)),
        (R.id.SORT_METHOD_HIGHER_TOTAL_PRICE,   R.string.higher_price,          desc(products_total_price)),
    ])

    order_status_map = OrderedDict()
    order_status_map[R.id.ORDER_STATUS_ANY] = R.string.any
    order_status_map[R.id.ORDER_STATUS_CANCELED] = R.string.canceled
    order_status_map[R.id.ORDER_STATUS_PAID] = R.string.paid
    order_status_map[R.id.ORDER_STATUS_SENT] = R.string.sent
    order_status_map[R.id.ORDER_STATUS_DELIVERED] = R.string.delivered

    @staticmethod
    def create_new(**kwargs):
        order = Order(**kwargs)
        client = User.get(order.client_id)
        if client == None:
            raise InvalidClientToOrder
        order.client_email = client.email

        products_amounts_zip = order.get_products_amounts_zip()

        for product, amount in products_amounts_zip:
            if amount <= 0 or product.stock < amount:
                raise InvalidOrderError

        order.products_total_price = order._get_products_total_price(products_amounts_zip)
        order.products_table_data = order._get_products_table_data(products_amounts_zip)
        order.total_table_data = order._get_total_table_data(products_amounts_zip=products_amounts_zip, client=client)
        order.inc_products_reserved(products_amounts_zip)
        order.uuid = str(uuid.uuid4())

        db.session.add(order)
        db.session.commit()
        return order

    def get_products_amounts_zip(self):
        products = []
        amounts = []

        for product_id, amount in self.amount_by_product_id.iteritems():
            product = Product.get(product_id)
            if product == None:
                raise InvalidOrderError
            products.append(product)
            amounts.append(amount)

        return zip(products, amounts)

    def inc_products_reserved(self, products_amounts_zip):
        for product, amount in products_amounts_zip:
            product.reserved += amount
            db.session.add(product)

    def get_status_as_string(self):
        return self.order_status_map[self.status]

    def get_formatted_paid_datetime(self):
        return self.paid_datetime.strftime(R.string.default_datetime_format)

    def get_formatted_sent_datetime(self):
        return self.sent_datetime.strftime(R.string.default_datetime_format)

    def get_formatted_delivered_datetime(self):
        return self.delivered_datetime.strftime(R.string.default_datetime_format)

    @staticmethod
    def get_order_status_id_choices():
        choices = []
        for order_status_id, order_status_name in Order.order_status_map.iteritems():
            choices.append((str(order_status_id.value), order_status_name))
        return choices

    def _get_products_total_price(self, products_amounts_zip):
        products_total_price = Decimal("0.00")
        for product, amount in products_amounts_zip:
            products_total_price += product.get_price(n_units=amount)
        return products_total_price

    def _get_products_table_data(self, products_amounts_zip):
        rows = []
        for product, amount in products_amounts_zip:
            rows.append([
                "#" + str(product.id),
                product.title,
                product.get_formatted_price(),
                amount,
                product.get_formatted_price(n_units=amount)
            ])

        return dict(
            table_data=dict(
                id="products-table",
                cols=[
                    dict(
                        id="product-id",
                        title=R.string.id,
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        id="product-title",
                        title=R.string.product_title,
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        id="product-price",
                        title=R.string.price,
                        type=R.id.COL_TYPE_TEXT.value,
                        tooltip=R.string.product_price_tooltip
                    ),
                    dict(
                        id="product-amount",
                        title=R.string.amount,
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        id="product-subtotal",
                        title=R.string.subtotal,
                        type=R.id.COL_TYPE_TEXT.value,
                        tooltip=R.string.subtotal_tooltip
                    ),
                ],
                rows=rows
            )
        )

    def _get_total_table_data(self, products_amounts_zip, client):
        freight = client.get_freight()
        return dict(
            table_data=dict(
                no_head = True,
                bordered = True,
                classes="products-total-table",
                id="total-table",
                cols=[
                    dict(
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        type=R.id.COL_TYPE_TEXT.value,
                    )
                ],
                rows=[
                    [R.string.products, R.string.price_with_rs(self.products_total_price)],
                    [R.string.freight, R.string.price_with_rs(freight)],
                    [R.string.total, R.string.price_with_rs(self.products_total_price + freight)]
                ]
            )
        )

    def get_formatted_products_total_price(self):
        return str(self.products_total_price).replace(".", ",")

    def mark_as_sent(self):
        if self.status != R.id.ORDER_STATUS_PAID:
            raise InvalidOrderStatusChange
        self.status = R.id.ORDER_STATUS_SENT
        self.sent_datetime = datetime.now()

        for product, amount in self.get_products_amounts_zip():
            if product.stock < amount:
                raise InsufficientStockToSendOrder(limiting_product=product)
            if product.reserved < amount:
                raise InconsistentDataBaseError
            product.reserved -= amount
            product.stock -= amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def unmark_as_sent(self):
        if self.status != R.id.ORDER_STATUS_SENT:
            raise InvalidOrderStatusChange

        self.status=R.id.ORDER_STATUS_PAID
        self.sent_datetime=None

        for product, amount in self.get_products_amounts_zip():
            product.reserved += amount
            product.stock += amount
            if product.reserved < 0 or product.stock < 0:
                raise InconsistentDataBaseError
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def mark_as_delivered(self):
        if self.status != R.id.ORDER_STATUS_SENT:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_DELIVERED
        self.delivered_datetime = datetime.now()

        db.session.add(self)
        db.session.commit()

    def unmark_as_delivered(self):
        if self.status != R.id.ORDER_STATUS_DELIVERED:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_SENT
        self.delivered_datetime = None

        db.session.add(self)
        db.session.commit()

    def mark_as_canceled(self):
        if self.status != R.id.ORDER_STATUS_PAID:
            raise InvalidOrderStatusChange

        self.status=R.id.ORDER_STATUS_CANCELED

        for product, amount in self.get_products_amounts_zip():
            product.reserved -= amount
            if product.reserved < 0:
                raise InconsistentDataBaseError
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def mark_as_paid(self):
        if self.status != R.id.ORDER_STATUS_CANCELED:
            raise InvalidOrderStatusChange

        self.status=R.id.ORDER_STATUS_PAID

        for product, amount in self.get_products_amounts_zip():
            product.reserved += amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_n_orders(status):
        if not status in Order.order_status_map.keys():
            raise InvalidOrderStatusIdError
        return Order.query.filter(Order.status == status).count()
