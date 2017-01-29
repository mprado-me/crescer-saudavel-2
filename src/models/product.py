# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from flask import url_for
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from proj_exceptions import InvalidNUnitsError
from proj_extensions import db
from models.base import BaseModel
from r import R
from proj_utils import parse_markdown, SortMethodMap


class Product(BaseModel):
    title = db.Column(db.String(R.dimen.product_title_max_length), nullable=False)
    _active = db.Column(db.Boolean, default=False, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("product_category.id"), nullable=False)
    category = relationship("ProductCategory", back_populates="products")
    subcategory_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    subcategory = relationship("ProductSubcategory", back_populates="products")
    price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    _stock = db.Column(db.Integer, nullable=False)
    _available = db.Column(db.Integer, nullable=False)
    _reserved = db.Column(db.Integer, default=0, nullable=False)
    _min_available = db.Column(db.Integer, nullable=False)
    is_available_to_client = db.Column(db.Boolean, nullable=False)
    _summary_markdown = db.Column(db.UnicodeText, nullable=False)
    summary_html = db.Column(db.UnicodeText, nullable=False)
    sales_number = db.Column(db.Integer, default=0)

    image_1 = db.Column(db.Text)
    image_2 = db.Column(db.Text)
    image_3 = db.Column(db.Text)
    image_4 = db.Column(db.Text)
    image_5 = db.Column(db.Text)
    image_6 = db.Column(db.Text)
    image_7 = db.Column(db.Text)
    image_8 = db.Column(db.Text)
    image_9 = db.Column(db.Text)
    image_10 = db.Column(db.Text)

    tab_1_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_1_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_1_content_markdown = db.Column(db.UnicodeText)
    tab_1_content_html = db.Column(db.UnicodeText)
    tab_2_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_2_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_2_content_markdown = db.Column(db.UnicodeText)
    tab_2_content_html = db.Column(db.UnicodeText)
    tab_3_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_3_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_3_content_markdown = db.Column(db.UnicodeText)
    tab_3_content_html = db.Column(db.UnicodeText)
    tab_4_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_4_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_4_content_markdown = db.Column(db.UnicodeText)
    tab_4_content_html = db.Column(db.UnicodeText)
    tab_5_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_5_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_5_content_markdown = db.Column(db.UnicodeText)
    tab_5_content_html = db.Column(db.UnicodeText)
    tab_6_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_6_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_6_content_markdown = db.Column(db.UnicodeText)
    tab_6_content_html = db.Column(db.UnicodeText)
    tab_7_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_7_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_7_content_markdown = db.Column(db.UnicodeText)
    tab_7_content_html = db.Column(db.UnicodeText)
    tab_8_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_8_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_8_content_markdown = db.Column(db.UnicodeText)
    tab_8_content_html = db.Column(db.UnicodeText)
    tab_9_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_9_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_9_content_markdown = db.Column(db.UnicodeText)
    tab_9_content_html = db.Column(db.UnicodeText)
    tab_10_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_10_title = db.Column(db.String(R.dimen.tab_title_max_length))
    _tab_10_content_markdown = db.Column(db.UnicodeText)
    tab_10_content_html = db.Column(db.UnicodeText)

    @hybrid_property
    def tab_1_content_markdown(self):
        return self._tab_1_content_markdown

    @tab_1_content_markdown.setter
    def tab_1_content_markdown(self, value):
        self._tab_1_content_markdown = value
        self.tab_1_content_html = parse_markdown(value)

    @hybrid_property
    def tab_2_content_markdown(self):
        return self._tab_2_content_markdown

    @tab_2_content_markdown.setter
    def tab_2_content_markdown(self, value):
        self._tab_2_content_markdown = value
        self.tab_2_content_html = parse_markdown(value)

    @hybrid_property
    def tab_3_content_markdown(self):
        return self._tab_3_content_markdown

    @tab_3_content_markdown.setter
    def tab_3_content_markdown(self, value):
        self._tab_3_content_markdown = value
        self.tab_3_content_html = parse_markdown(value)

    @hybrid_property
    def tab_4_content_markdown(self):
        return self._tab_4_content_markdown

    @tab_4_content_markdown.setter
    def tab_4_content_markdown(self, value):
        self._tab_4_content_markdown = value
        self.tab_4_content_html = parse_markdown(value)

    @hybrid_property
    def tab_5_content_markdown(self):
        return self._tab_5_content_markdown

    @tab_5_content_markdown.setter
    def tab_5_content_markdown(self, value):
        self._tab_5_content_markdown = value
        self.tab_5_content_html = parse_markdown(value)

    @hybrid_property
    def tab_6_content_markdown(self):
        return self._tab_6_content_markdown

    @tab_6_content_markdown.setter
    def tab_6_content_markdown(self, value):
        self._tab_6_content_markdown = value
        self.tab_6_content_html = parse_markdown(value)

    @hybrid_property
    def tab_7_content_markdown(self):
        return self._tab_7_content_markdown

    @tab_7_content_markdown.setter
    def tab_7_content_markdown(self, value):
        self._tab_7_content_markdown = value
        self.tab_7_content_html = parse_markdown(value)

    @hybrid_property
    def tab_8_content_markdown(self):
        return self._tab_8_content_markdown

    @tab_8_content_markdown.setter
    def tab_8_content_markdown(self, value):
        self._tab_8_content_markdown = value
        self.tab_8_content_html = parse_markdown(value)

    @hybrid_property
    def tab_9_content_markdown(self):
        return self._tab_9_content_markdown

    @tab_9_content_markdown.setter
    def tab_9_content_markdown(self, value):
        self._tab_9_content_markdown = value
        self.tab_9_content_html = parse_markdown(value)

    @hybrid_property
    def tab_10_content_markdown(self):
        return self._tab_10_content_markdown

    @tab_10_content_markdown.setter
    def tab_10_content_markdown(self, value):
        self._tab_10_content_markdown = value
        self.tab_10_content_html = parse_markdown(value)

    @hybrid_property
    def summary_markdown(self):
        return self._summary_markdown

    @summary_markdown.setter
    def summary_markdown(self, value):
        self._summary_markdown = value
        self.summary_html = parse_markdown(value)

    @hybrid_property
    def active(self):
        return self._active

    @active.setter
    def active(self, new_active):
        self._active = new_active
        self.update_is_available_to_client()

    @hybrid_property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, new_stock):
        self._stock = new_stock
        self.update_available()
        self.update_is_available_to_client()

    @hybrid_property
    def reserved(self):
        return self._reserved

    @reserved.setter
    def reserved(self, new_reserved):
        self._reserved = new_reserved
        self.update_available()
        self.update_is_available_to_client()

    @hybrid_property
    def min_available(self):
        return self._min_available

    @min_available.setter
    def min_available(self, new_min_available):
        self._min_available = new_min_available
        self.update_is_available_to_client()

    @hybrid_property
    def available(self):
        return self._available

    @hybrid_property
    def id_formatted(self):
        return R.string.id_prefix + str(self.id)

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_ID,               R.string.id,                    asc("id")),
        (R.id.SORT_METHOD_TITLE,            R.string.title,                 asc(title)),
        (R.id.SORT_METHOD_LOWEST_PRICE,     R.string.lowest_price,          asc(price)),
        (R.id.SORT_METHOD_HIGHER_PRICE,     R.string.higher_price,          desc(price)),
        (R.id.SORT_METHOD_LOWEST_STOCK,     R.string.lowest_stock,          asc(_stock)),
        (R.id.SORT_METHOD_HIGHER_STOCK,     R.string.higher_stock,          desc(_stock)),
        (R.id.SORT_METHOD_LOWEST_AVAILABLE, R.string.lowest_available,      asc(_available)),
        (R.id.SORT_METHOD_HIGHER_AVAILABLE, R.string.higher_available,      desc(_available)),
        (R.id.SORT_METHOD_LOWEST_RESERVED,  R.string.lowest_reserved,       asc(_reserved)),
        (R.id.SORT_METHOD_HIGHER_RESERVED,  R.string.higher_reserved,       desc(_reserved)),
        (R.id.SORT_METHOD_BEST_SELLER,      R.string.best_seller,           desc(sales_number)),
        (R.id.SORT_METHOD_LESS_SOLD,        R.string.less_sold,             asc(sales_number))
    ])

    client_sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_NAME,             R.string.name,                  asc(title)),
        (R.id.SORT_METHOD_BEST_SELLER,      R.string.best_seller,           desc(sales_number)),
        (R.id.SORT_METHOD_LOWEST_PRICE,     R.string.lowest_price,          asc(price)),
        (R.id.SORT_METHOD_HIGHER_PRICE,     R.string.higher_price,          desc(price)),
    ])

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            title=form.title.data,
            active=form.active.data,
            category_id=int(form.category_id.data),
            subcategory_id=int(form.subcategory_id.data) if int(form.subcategory_id.data) != 0 else None,
            price=Decimal(form.price.data.replace(',', '.')),
            stock=int(form.stock.data),
            min_available=int(form.min_available.data),
            summary_markdown=form.summary.data,

            image_1=form.image_1.data,
            image_2=form.image_2.data,
            image_3=form.image_3.data,
            image_4=form.image_4.data,
            image_5=form.image_5.data,
            image_6=form.image_6.data,
            image_7=form.image_7.data,
            image_8=form.image_8.data,
            image_9=form.image_9.data,
            image_10=form.image_10.data,

            tab_1_active=form.tab_1_active.data,
            tab_1_title=form.tab_1_title.data,
            tab_1_content_markdown=form.tab_1_content.data,
            tab_2_active=form.tab_2_active.data,
            tab_2_title=form.tab_2_title.data,
            tab_2_content_markdown=form.tab_2_content.data,
            tab_3_active=form.tab_3_active.data,
            tab_3_title=form.tab_3_title.data,
            tab_3_content_markdown=form.tab_3_content.data,
            tab_4_active=form.tab_4_active.data,
            tab_4_title=form.tab_4_title.data,
            tab_4_content_markdown=form.tab_4_content.data,
            tab_5_active=form.tab_5_active.data,
            tab_5_title=form.tab_5_title.data,
            tab_5_content_markdown=form.tab_5_content.data,
            tab_6_active=form.tab_6_active.data,
            tab_6_title=form.tab_6_title.data,
            tab_6_content_markdown=form.tab_6_content.data,
            tab_7_active=form.tab_7_active.data,
            tab_7_title=form.tab_7_title.data,
            tab_7_content_markdown=form.tab_7_content.data,
            tab_8_active=form.tab_8_active.data,
            tab_8_title=form.tab_8_title.data,
            tab_8_content_markdown=form.tab_8_content.data,
            tab_9_active=form.tab_9_active.data,
            tab_9_title=form.tab_9_title.data,
            tab_9_content_markdown=form.tab_9_content.data,
            tab_10_active=form.tab_10_active.data,
            tab_10_title=form.tab_10_title.data,
            tab_10_content_markdown=form.tab_10_content.data
        )

    @staticmethod
    def get_choices(include_none=False):
        product_choices = []
        if include_none:
            product_choices = [(str(0), R.string.none_in_masculine)]

        for id_title in Product.query.order_by(Product.title).with_entities(Product.id, Product.title).all():
            product_choices.append((str(id_title[0]), id_title[1]))

        return product_choices

    def disable(self):
        self.active = False
        db.session.add(self)
        db.session.commit()

    def to_activate(self):
        self.active = True
        db.session.add(self)
        db.session.commit()

    def add_to_stock(self, value):
        self.stock += value
        db.session.add(self)
        db.session.commit()

    def remove_from_stock(self, value):
        self.stock -= value

        if self.stock < 0:
            self.stock = 0

        db.session.add(self)
        db.session.commit()

    def update_stock(self, value):
        self.stock = value
        db.session.add(self)
        db.session.commit()

    def get_href(self):
        return url_for("client_products.product", **{R.string.product_id_arg_name: self.id})

    def get_main_image_src(self):
        image_name = self.image_1
        if image_name is None or image_name == "":
            image_name = R.string.default_product_image_name
        return url_for("static", filename="imgs/" + image_name)

    def get_price(self, n_units=1):
        if not isinstance(n_units, int) or n_units < 0:
            raise InvalidNUnitsError
        return self.price * Decimal(str(n_units))

    def get_formatted_price(self, n_units=1, include_rs=False):
        formatted_price = ""
        if include_rs:
            formatted_price += "R$ "
        formatted_price += str(self.get_price(n_units=n_units)).replace(".", ",")
        return formatted_price

    def update_available(self):
        if self._reserved == None:
            self._reserved = 0
        if self._stock is not None:
            self._available = self._stock - self._reserved

    def update_is_available_to_client(self):
        if self._active is not None and self._available is not None and self._min_available is not None:
            if self._active and self._available > self._min_available:
                self.is_available_to_client = True
            else:
                self.is_available_to_client = False
