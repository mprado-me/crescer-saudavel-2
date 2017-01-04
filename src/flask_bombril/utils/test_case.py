# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 03/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase

from flask import request
from flask import url_for

from flask_bombril import R
from utils import stringfy_list, n_pages, slice_items, get_url_args, get_url_arg, get_page_range
from app_contexts.unit_test_app import unit_test_app as app


class TestCase(BaseTestCase):
    def test_stringfy_list(self):
        self.assertEqual("", stringfy_list([]))
        self.assertEqual(R.string.a, stringfy_list([R.string.a]))
        self.assertEqual(R.string.a + " " + R.string.and_word + " " + R.string.b,
                         stringfy_list([R.string.a, R.string.b]))
        self.assertEqual(
            R.string.a + R.string.comma + " " + R.string.b + " " + R.string.and_word + " " + R.string.c,
            stringfy_list([R.string.a, R.string.b, R.string.c]))
        self.assertEqual(
            R.string.a + R.string.comma + " " + R.string.b + R.string.comma + " " + R.string.c + " " + R.string.and_word + " " + R.string.d,
            stringfy_list([R.string.a, R.string.b, R.string.c, R.string.d]))

    def test_n_pages(self):
        self.assertEqual(1, n_pages(per_page=1, n_items=1))
        self.assertEqual(2, n_pages(per_page=1, n_items=2))
        self.assertEqual(42, n_pages(per_page=1, n_items=42))

        self.assertEqual(1, n_pages(per_page=5, n_items=0))
        self.assertEqual(1, n_pages(per_page=5, n_items=1))
        self.assertEqual(1, n_pages(per_page=5, n_items=4))
        self.assertEqual(1, n_pages(per_page=5, n_items=5))

        self.assertEqual(2, n_pages(per_page=5, n_items=6))
        self.assertEqual(2, n_pages(per_page=5, n_items=9))
        self.assertEqual(2, n_pages(per_page=5, n_items=10))

        self.assertEqual(3, n_pages(per_page=5, n_items=11))
        self.assertEqual(3, n_pages(per_page=5, n_items=15))

        self.assertEqual(4, n_pages(per_page=5, n_items=16))

    def test_slice_items(self):
        self.assertEqual(["a", "b"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=1,
                                     per_page=2))
        self.assertEqual(["a", "b", "c"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=1,
                                     per_page=3))
        self.assertEqual(["c", "d"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=2,
                                     per_page=2))
        self.assertEqual(["k", "l"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=6,
                                     per_page=2))
        self.assertEqual(["a", "b", "c", "d", "e"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=1,
                                     per_page=5))
        self.assertEqual(["f", "g", "h", "i", "j"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=2,
                                     per_page=5))
        self.assertEqual(["k", "l"],
                         slice_items(items=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"], page=3,
                                     per_page=5))

    def test_get_url_args(self):
        with app.test_client() as c:
            c.get("/")
            request.view_args = dict(
                test_view_arg="a"
            )
            request.args = dict(
                query_arg="b"
            )
            self.assertEqual(dict(test_view_arg="a", query_arg="b"), get_url_args())

    def test_get_url_arg(self):
        with app.test_client() as c:
            c.get("/")
            request.view_args = dict(
                test_view_arg="a"
            )
            request.args = dict(
                query_arg="b"
            )
            self.assertEqual("a", get_url_arg("test_view_arg"))
            self.assertEqual("b", get_url_arg("query_arg"))

    def test_get_page_range(self):
        self.assertEqual((0, 5), get_page_range(curr_page=1, per_page=5, min_page=1))
        self.assertEqual((5, 10), get_page_range(curr_page=2, per_page=5, min_page=1))
        self.assertEqual((10, 15), get_page_range(curr_page=3, per_page=5, min_page=1))

        self.assertEqual((0, 5), get_page_range(curr_page=0, per_page=5, min_page=0))
        self.assertEqual((5, 10), get_page_range(curr_page=1, per_page=5, min_page=0))
        self.assertEqual((10, 15), get_page_range(curr_page=2, per_page=5, min_page=0))
        self.assertEqual((15, 20), get_page_range(curr_page=3, per_page=5, min_page=0))