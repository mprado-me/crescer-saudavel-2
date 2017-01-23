# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from unittest import TestCase as BaseTestCase

from flask import url_for

from app_contexts.app import app
from proj_extensions import db
from models.product import Product
from models.product_subcategory import ProductSubcategory
from models.product_category import ProductCategory
from r import R


class TestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.config["SERVER_NAME"] = "localhost:5000"
            app.config["WTF_CSRF_ENABLED"] = False

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test(self):
        with app.app_context():
            with app.test_client() as c:
                # ------------------------------------------------------------------------------------------------------
                # ProductCategory
                # ------------------------------------------------------------------------------------------------------
                n_categories = ProductCategory.count()
                self.assertEqual(n_categories, 0)
                response = c.post(url_for("admin_products.add_category"), data=dict(
                    category_name=R.string.test1,
                    active=True,
                ))
                self.assertEqual(response.status_code, 302)
                n_categories = ProductCategory.count()
                self.assertEqual(n_categories, 1)
                category = ProductCategory.get_last()
                self.assertEqual(category.name, R.string.test1)
                self.assertEqual(category.active, True)

                # ------------------------------------------------------------------------------------------------------
                # ProductSubcategory
                # ------------------------------------------------------------------------------------------------------
                n_subcategories = ProductSubcategory.count()
                self.assertEqual(n_subcategories, 0)
                with app.test_client() as c:
                    response = c.post(url_for("admin_products.add_subcategory"), data=dict(
                        category_id="1",
                        subcategory_name=R.string.test1,
                        active=True,
                    ))
                    self.assertEqual(response.status_code, 302)
                    n_subcategories = ProductSubcategory.count()
                    self.assertEqual(n_subcategories, 1)
                    subcategory = ProductSubcategory.get_last()
                    self.assertEqual(subcategory.category_id, 1)
                    self.assertEqual(subcategory.name, R.string.test1)
                    self.assertEqual(subcategory.active, True)

                # ------------------------------------------------------------------------------------------------------
                # Product
                # ------------------------------------------------------------------------------------------------------
                n_products = Product.query.count()
                self.assertEqual(n_products, 0)
                with app.test_client() as c:
                    response = c.post(url_for("admin_products.add_product"), data=dict(
                        title=R.string.test1,
                        active=False,
                        category_id="1",
                        subcategory_id="1",
                        price=R.string.test_price,
                        stock=R.dimen.test_stock,
                        min_available=R.dimen.test_min_available,
                        summary=R.string.test1,
                        image_1="",
                        image_2="",
                        image_3="",
                        image_4="",
                        image_5="",
                        image_6="",
                        image_7="",
                        image_8="",
                        image_9="",
                        image_10=""
                    ))
                    self.assertEqual(response.status_code, 302)
                    self.assertEqual(Product.count(), 1)

                    response = c.post(url_for("admin_products.add_product"), data=dict(
                        title=R.string.test1,
                        active=True,
                        category_id="1",
                        subcategory_id="1",
                        price=R.string.test_price,
                        stock=R.dimen.test_stock,
                        min_available=R.dimen.test_min_available,
                        summary=R.string.test1,
                        image_1="",
                        image_2="",
                        image_3="",
                        image_4="",
                        image_5="",
                        image_6="",
                        image_7="",
                        image_8="",
                        image_9="",
                        image_10=""
                    ))
                    self.assertEqual(response.status_code, 302)
                    self.assertEqual(Product.count(), 2)
                    product = Product.get_last()
                    self.assertEqual(product.title, R.string.test1)
                    self.assertEqual(product.active, True)
                    self.assertEqual(product.category_id, 1)
                    self.assertEqual(product.subcategory_id, 1)
                    self.assertEqual(product.price, Decimal(R.string.test_price.replace(",", ".")))
                    self.assertEqual(product.stock, R.dimen.test_stock)
                    self.assertEqual(product.min_available, R.dimen.test_min_available)
                    self.assertEqual(product.image_1, "")
                    self.assertEqual(product.image_2, "")
                    self.assertEqual(product.image_3, "")
                    self.assertEqual(product.image_4, "")
                    self.assertEqual(product.image_5, "")
                    self.assertEqual(product.image_6, "")
                    self.assertEqual(product.image_7, "")
                    self.assertEqual(product.image_8, "")
                    self.assertEqual(product.image_9, "")
                    self.assertEqual(product.image_10, "")

                    self.assertEqual(product.available, R.dimen.test_stock)
                    self.assertEqual(product.reserved, 0)
                    self.assertEqual(product.sales_number, 0)

                    product = Product(
                        title=R.string.test1,
                        active=True,
                        category_id="1",
                        subcategory_id="1",
                        price=Decimal(R.string.test_price.replace(",", ".")),
                        stock=22,
                        reserved=12,
                        min_available=R.dimen.test_min_available,
                        summary=R.string.test1,
                        image_1="",
                        image_2="",
                        image_3="",
                        image_4="",
                        image_5="",
                        image_6="",
                        image_7="",
                        image_8="",
                        image_9="",
                        image_10="",
                        sales_number=3
                    )
                    db.session.add(product)
                    db.session.commit()
                    self.assertEqual(Product.count(), 3)
                    product = Product.get_last()
                    self.assertEqual(product.title, R.string.test1)
                    self.assertEqual(product.active, True)
                    self.assertEqual(product.category_id, 1)
                    self.assertEqual(product.subcategory_id, 1)
                    self.assertEqual(product.price, Decimal(R.string.test_price.replace(",", ".")))
                    self.assertEqual(product.stock, 22)
                    self.assertEqual(product.min_available, R.dimen.test_min_available)
                    self.assertEqual(product.image_1, "")
                    self.assertEqual(product.image_2, "")
                    self.assertEqual(product.image_3, "")
                    self.assertEqual(product.image_4, "")
                    self.assertEqual(product.image_5, "")
                    self.assertEqual(product.image_6, "")
                    self.assertEqual(product.image_7, "")
                    self.assertEqual(product.image_8, "")
                    self.assertEqual(product.image_9, "")
                    self.assertEqual(product.image_10, "")

                    self.assertEqual(product.available, 10)
                    self.assertEqual(product.reserved, 12)
                    self.assertEqual(product.sales_number, 3)