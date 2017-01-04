# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.orm import relationship
from proj_exceptions import InvalidIdError
from extensions import db
from models.product import Product
from models.product_subcategory import ProductSubcategory
from r import R


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(R.dimen.product_category_max_length))
    active = db.Column(db.Boolean, default=False, nullable=False)
    subcategories = relationship("ProductSubcategory", order_by=ProductSubcategory.name, back_populates="category")
    products = relationship("Product", order_by=Product.title, back_populates="category")

    @staticmethod
    def add_from_form(add_product_category_form):
        product_category = ProductCategory(
            name=add_product_category_form.category_name.data,
            active=add_product_category_form.active.data
        )
        db.session.add(product_category)
        db.session.commit()

    @staticmethod
    def disable(category_id):
        category = ProductCategory.query.filter_by(id=category_id).one_or_none()
        if not category:
            raise InvalidIdError
        category.active = False
        db.session.add(category)
        db.session.commit()

    @staticmethod
    def activate(category_id):
        category = ProductCategory.query.filter_by(id=category_id).one_or_none()
        if not category:
            raise InvalidIdError
        category.active = True
        db.session.add(category)
        db.session.commit()