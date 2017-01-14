# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import sys

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app
from extensions import db
from models.utils import create_states, create_product_category_example, create_product_example, \
    create_blog_post_example


def restart_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_states()
        product_category_example = create_product_category_example()
        create_product_example(product_category_example.id)
        create_blog_post_example()
        print "Db restarted."

if __name__ == "__main__":
    restart_db()
