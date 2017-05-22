# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.orm import relationship
from models.base import BaseModel
from proj_extensions import db
from models.product import Product
from models.product_subcategory import ProductSubcategory
from r import R


class ProductCategory(BaseModel):
    __tablename__ = "product_category"

    name = db.Column(db.String(R.dimen.product_category_name_max_length), nullable=False)
    priority = db.Column(db.Integer, default=R.dimen.default_product_category_priority, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    product_subcategories = relationship("ProductSubcategory", order_by=ProductSubcategory.name, back_populates="product_category")
    products = relationship("Product", order_by=Product.title, back_populates="category")

    def __repr__(self):
        return self.name
