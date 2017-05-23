# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, SubmitField, TextAreaField, IntegerField
from wtforms.fields.html5 import TelField

from flask.ext.bombril.form_validators import Required
from flask_bombril.form_validators import EmailFormat
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import MarkdownValidator
from flask_bombril.form_validators.phone_fomat.phone_format import PhoneFormat
from models.blog.blog_post import BlogPost
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from proj_utils import get_image_choices, safe_string
from r import R


class CarouselForm(FlaskForm):
    active = BooleanField(
        label=R.string.active,
        default=False
    )
    title = StringField(
        label=R.string.title,
        validators=[
            Length(max_length=R.dimen.carousel_title_max_length)
        ])
    subtitle = StringField(
        label=R.string.subtitle,
        validators=[
            Length(max_length=R.dimen.carousel_subtitle_max_length)
        ])
    link = StringField(
        label=R.string.link,
        validators=[
            Length(max_length=R.dimen.link_max_length)
        ])
    image = SelectField(
        label=R.string.image,
    )

    submit = SubmitField(label=R.string.save)

    def __init__(self, home_content=None, carousel_number=None, **kwargs):
        super(CarouselForm, self).__init__(**kwargs)
        self.image.choices = get_image_choices(include_none=True)

        if home_content != None and carousel_number != None:
            assert carousel_number in range(1, 3 + 1)
            if carousel_number == 1:
                self.active.data = home_content.carousel_item_1_active
                self.title.data = home_content.carousel_item_1_title
                self.subtitle.data = home_content.carousel_item_1_subtitle
                self.link.data = home_content.carousel_item_1_link
                self.image.data = home_content.carousel_item_1_image
            elif carousel_number == 2:
                self.active.data = home_content.carousel_item_2_active
                self.title.data = home_content.carousel_item_2_title
                self.subtitle.data = home_content.carousel_item_2_subtitle
                self.link.data = home_content.carousel_item_2_link
                self.image.data = home_content.carousel_item_2_image
            else:
                self.active.data = home_content.carousel_item_3_active
                self.title.data = home_content.carousel_item_3_title
                self.subtitle.data = home_content.carousel_item_3_subtitle
                self.link.data = home_content.carousel_item_3_link
                self.image.data = home_content.carousel_item_3_image


class ProductSectionForm(FlaskForm):
    active = BooleanField(
        label=R.string.active_in_female,
        default=False
    )
    name = StringField(
        label=R.string.section_name,
        validators=[
            Length(max_length=R.dimen.product_section_name_max_length)
        ])
    link = StringField(
        label=R.string.link,
        validators=[
            Length(max_length=R.dimen.link_max_length)
        ])
    product_1_id = SelectField(label=R.string.get_product_n(1))
    product_2_id = SelectField(label=R.string.get_product_n(2))
    product_3_id = SelectField(label=R.string.get_product_n(3))
    product_4_id = SelectField(label=R.string.get_product_n(4))
    product_5_id = SelectField(label=R.string.get_product_n(5))
    product_6_id = SelectField(label=R.string.get_product_n(6))
    product_7_id = SelectField(label=R.string.get_product_n(7))
    product_8_id = SelectField(label=R.string.get_product_n(8))
    product_9_id = SelectField(label=R.string.get_product_n(9))
    product_10_id = SelectField(label=R.string.get_product_n(10))
    product_11_id = SelectField(label=R.string.get_product_n(11))
    product_12_id = SelectField(label=R.string.get_product_n(12))
    product_13_id = SelectField(label=R.string.get_product_n(13))
    product_14_id = SelectField(label=R.string.get_product_n(14))
    product_15_id = SelectField(label=R.string.get_product_n(15))
    product_16_id = SelectField(label=R.string.get_product_n(16))
    product_17_id = SelectField(label=R.string.get_product_n(17))
    product_18_id = SelectField(label=R.string.get_product_n(18))
    product_19_id = SelectField(label=R.string.get_product_n(19))
    product_20_id = SelectField(label=R.string.get_product_n(20))

    submit = SubmitField(label=R.string.save)

    def __init__(self, home_content=None, product_section_number=None, **kwargs):
        super(ProductSectionForm, self).__init__(**kwargs)
        product_choices_with_none = Product.get_choices(include_none=True, only_active=True)
        self.product_1_id.choices = product_choices_with_none
        self.product_2_id.choices = product_choices_with_none
        self.product_3_id.choices = product_choices_with_none
        self.product_4_id.choices = product_choices_with_none
        self.product_5_id.choices = product_choices_with_none
        self.product_6_id.choices = product_choices_with_none
        self.product_7_id.choices = product_choices_with_none
        self.product_8_id.choices = product_choices_with_none
        self.product_9_id.choices = product_choices_with_none
        self.product_10_id.choices = product_choices_with_none
        self.product_11_id.choices = product_choices_with_none
        self.product_12_id.choices = product_choices_with_none
        self.product_13_id.choices = product_choices_with_none
        self.product_14_id.choices = product_choices_with_none
        self.product_15_id.choices = product_choices_with_none
        self.product_16_id.choices = product_choices_with_none
        self.product_17_id.choices = product_choices_with_none
        self.product_18_id.choices = product_choices_with_none
        self.product_19_id.choices = product_choices_with_none
        self.product_20_id.choices = product_choices_with_none

        if home_content != None and product_section_number != None:
            assert product_section_number in range(1, 5+1)
            if product_section_number == 1:
                self.active.data = home_content.product_section_1_active
                self.name.data = home_content.product_section_1_name
                self.link.data = home_content.product_section_1_link
                self.product_1_id.data = str(home_content.product_section_1_product_1_id)
                self.product_2_id.data = str(home_content.product_section_1_product_2_id)
                self.product_3_id.data = str(home_content.product_section_1_product_3_id)
                self.product_4_id.data = str(home_content.product_section_1_product_4_id)
                self.product_5_id.data = str(home_content.product_section_1_product_5_id)
                self.product_6_id.data = str(home_content.product_section_1_product_6_id)
                self.product_7_id.data = str(home_content.product_section_1_product_7_id)
                self.product_8_id.data = str(home_content.product_section_1_product_8_id)
                self.product_9_id.data = str(home_content.product_section_1_product_9_id)
                self.product_10_id.data = str(home_content.product_section_1_product_10_id)
                self.product_11_id.data = str(home_content.product_section_1_product_11_id)
                self.product_12_id.data = str(home_content.product_section_1_product_12_id)
                self.product_13_id.data = str(home_content.product_section_1_product_13_id)
                self.product_14_id.data = str(home_content.product_section_1_product_14_id)
                self.product_15_id.data = str(home_content.product_section_1_product_15_id)
                self.product_16_id.data = str(home_content.product_section_1_product_16_id)
                self.product_17_id.data = str(home_content.product_section_1_product_17_id)
                self.product_18_id.data = str(home_content.product_section_1_product_18_id)
                self.product_19_id.data = str(home_content.product_section_1_product_19_id)
                self.product_20_id.data = str(home_content.product_section_1_product_20_id)
            elif product_section_number == 2:
                self.active.data = home_content.product_section_2_active
                self.name.data = home_content.product_section_2_name
                self.link.data = home_content.product_section_2_link
                self.product_1_id.data = str(home_content.product_section_2_product_1_id)
                self.product_2_id.data = str(home_content.product_section_2_product_2_id)
                self.product_3_id.data = str(home_content.product_section_2_product_3_id)
                self.product_4_id.data = str(home_content.product_section_2_product_4_id)
                self.product_5_id.data = str(home_content.product_section_2_product_5_id)
                self.product_6_id.data = str(home_content.product_section_2_product_6_id)
                self.product_7_id.data = str(home_content.product_section_2_product_7_id)
                self.product_8_id.data = str(home_content.product_section_2_product_8_id)
                self.product_9_id.data = str(home_content.product_section_2_product_9_id)
                self.product_10_id.data = str(home_content.product_section_2_product_10_id)
                self.product_11_id.data = str(home_content.product_section_2_product_11_id)
                self.product_12_id.data = str(home_content.product_section_2_product_12_id)
                self.product_13_id.data = str(home_content.product_section_2_product_13_id)
                self.product_14_id.data = str(home_content.product_section_2_product_14_id)
                self.product_15_id.data = str(home_content.product_section_2_product_15_id)
                self.product_16_id.data = str(home_content.product_section_2_product_16_id)
                self.product_17_id.data = str(home_content.product_section_2_product_17_id)
                self.product_18_id.data = str(home_content.product_section_2_product_18_id)
                self.product_19_id.data = str(home_content.product_section_2_product_19_id)
                self.product_20_id.data = str(home_content.product_section_2_product_20_id)
            elif product_section_number == 3:
                self.active.data = home_content.product_section_3_active
                self.name.data = home_content.product_section_3_name
                self.link.data = home_content.product_section_3_link
                self.product_1_id.data = str(home_content.product_section_3_product_1_id)
                self.product_2_id.data = str(home_content.product_section_3_product_2_id)
                self.product_3_id.data = str(home_content.product_section_3_product_3_id)
                self.product_4_id.data = str(home_content.product_section_3_product_4_id)
                self.product_5_id.data = str(home_content.product_section_3_product_5_id)
                self.product_6_id.data = str(home_content.product_section_3_product_6_id)
                self.product_7_id.data = str(home_content.product_section_3_product_7_id)
                self.product_8_id.data = str(home_content.product_section_3_product_8_id)
                self.product_9_id.data = str(home_content.product_section_3_product_9_id)
                self.product_10_id.data = str(home_content.product_section_3_product_10_id)
                self.product_11_id.data = str(home_content.product_section_3_product_11_id)
                self.product_12_id.data = str(home_content.product_section_3_product_12_id)
                self.product_13_id.data = str(home_content.product_section_3_product_13_id)
                self.product_14_id.data = str(home_content.product_section_3_product_14_id)
                self.product_15_id.data = str(home_content.product_section_3_product_15_id)
                self.product_16_id.data = str(home_content.product_section_3_product_16_id)
                self.product_17_id.data = str(home_content.product_section_3_product_17_id)
                self.product_18_id.data = str(home_content.product_section_3_product_18_id)
                self.product_19_id.data = str(home_content.product_section_3_product_19_id)
                self.product_20_id.data = str(home_content.product_section_3_product_20_id)
            elif product_section_number == 4:
                self.active.data = home_content.product_section_4_active
                self.name.data = home_content.product_section_4_name
                self.link.data = home_content.product_section_4_link
                self.product_1_id.data = str(home_content.product_section_4_product_1_id)
                self.product_2_id.data = str(home_content.product_section_4_product_2_id)
                self.product_3_id.data = str(home_content.product_section_4_product_3_id)
                self.product_4_id.data = str(home_content.product_section_4_product_4_id)
                self.product_5_id.data = str(home_content.product_section_4_product_5_id)
                self.product_6_id.data = str(home_content.product_section_4_product_6_id)
                self.product_7_id.data = str(home_content.product_section_4_product_7_id)
                self.product_8_id.data = str(home_content.product_section_4_product_8_id)
                self.product_9_id.data = str(home_content.product_section_4_product_9_id)
                self.product_10_id.data = str(home_content.product_section_4_product_10_id)
                self.product_11_id.data = str(home_content.product_section_4_product_11_id)
                self.product_12_id.data = str(home_content.product_section_4_product_12_id)
                self.product_13_id.data = str(home_content.product_section_4_product_13_id)
                self.product_14_id.data = str(home_content.product_section_4_product_14_id)
                self.product_15_id.data = str(home_content.product_section_4_product_15_id)
                self.product_16_id.data = str(home_content.product_section_4_product_16_id)
                self.product_17_id.data = str(home_content.product_section_4_product_17_id)
                self.product_18_id.data = str(home_content.product_section_4_product_18_id)
                self.product_19_id.data = str(home_content.product_section_4_product_19_id)
                self.product_20_id.data = str(home_content.product_section_4_product_20_id)
            elif product_section_number == 5:
                self.active.data = home_content.product_section_5_active
                self.name.data = home_content.product_section_5_name
                self.link.data = home_content.product_section_5_link
                self.product_1_id.data = str(home_content.product_section_5_product_1_id)
                self.product_2_id.data = str(home_content.product_section_5_product_2_id)
                self.product_3_id.data = str(home_content.product_section_5_product_3_id)
                self.product_4_id.data = str(home_content.product_section_5_product_4_id)
                self.product_5_id.data = str(home_content.product_section_5_product_5_id)
                self.product_6_id.data = str(home_content.product_section_5_product_6_id)
                self.product_7_id.data = str(home_content.product_section_5_product_7_id)
                self.product_8_id.data = str(home_content.product_section_5_product_8_id)
                self.product_9_id.data = str(home_content.product_section_5_product_9_id)
                self.product_10_id.data = str(home_content.product_section_5_product_10_id)
                self.product_11_id.data = str(home_content.product_section_5_product_11_id)
                self.product_12_id.data = str(home_content.product_section_5_product_12_id)
                self.product_13_id.data = str(home_content.product_section_5_product_13_id)
                self.product_14_id.data = str(home_content.product_section_5_product_14_id)
                self.product_15_id.data = str(home_content.product_section_5_product_15_id)
                self.product_16_id.data = str(home_content.product_section_5_product_16_id)
                self.product_17_id.data = str(home_content.product_section_5_product_17_id)
                self.product_18_id.data = str(home_content.product_section_5_product_18_id)
                self.product_19_id.data = str(home_content.product_section_5_product_19_id)
                self.product_20_id.data = str(home_content.product_section_5_product_20_id)


class MoreCategoriesSectionForm(FlaskForm):
    category_1_id = SelectField(label=R.string.category_n(1))
    category_1_image = SelectField(label=R.string.image_of_category_n(1))
    subcategory_1_of_category_1_id = SelectField(label=R.string.subcategory_n_of_category_m(n=1, m=1))
    subcategory_2_of_category_1_id = SelectField(label=R.string.subcategory_n_of_category_m(n=2, m=1))
    subcategory_3_of_category_1_id = SelectField(label=R.string.subcategory_n_of_category_m(n=3, m=1))
    subcategory_4_of_category_1_id = SelectField(label=R.string.subcategory_n_of_category_m(n=4, m=1))
    subcategory_5_of_category_1_id = SelectField(label=R.string.subcategory_n_of_category_m(n=5, m=1))

    category_2_id = SelectField(label=R.string.category_n(2))
    category_2_image = SelectField(label=R.string.image_of_category_n(2))
    subcategory_1_of_category_2_id = SelectField(label=R.string.subcategory_n_of_category_m(n=1, m=2))
    subcategory_2_of_category_2_id = SelectField(label=R.string.subcategory_n_of_category_m(n=2, m=2))
    subcategory_3_of_category_2_id = SelectField(label=R.string.subcategory_n_of_category_m(n=3, m=2))
    subcategory_4_of_category_2_id = SelectField(label=R.string.subcategory_n_of_category_m(n=4, m=2))
    subcategory_5_of_category_2_id = SelectField(label=R.string.subcategory_n_of_category_m(n=5, m=2))

    category_3_id = SelectField(label=R.string.category_n(3))
    category_3_image = SelectField(label=R.string.image_of_category_n(3))
    subcategory_1_of_category_3_id = SelectField(label=R.string.subcategory_n_of_category_m(n=1, m=3))
    subcategory_2_of_category_3_id = SelectField(label=R.string.subcategory_n_of_category_m(n=2, m=3))
    subcategory_3_of_category_3_id = SelectField(label=R.string.subcategory_n_of_category_m(n=3, m=3))
    subcategory_4_of_category_3_id = SelectField(label=R.string.subcategory_n_of_category_m(n=4, m=3))
    subcategory_5_of_category_3_id = SelectField(label=R.string.subcategory_n_of_category_m(n=5, m=3))

    category_4_id = SelectField(label=R.string.category_n(4))
    category_4_image = SelectField(label=R.string.image_of_category_n(4))
    subcategory_1_of_category_4_id = SelectField(label=R.string.subcategory_n_of_category_m(n=1, m=4))
    subcategory_2_of_category_4_id = SelectField(label=R.string.subcategory_n_of_category_m(n=2, m=4))
    subcategory_3_of_category_4_id = SelectField(label=R.string.subcategory_n_of_category_m(n=3, m=4))
    subcategory_4_of_category_4_id = SelectField(label=R.string.subcategory_n_of_category_m(n=4, m=4))
    subcategory_5_of_category_4_id = SelectField(label=R.string.subcategory_n_of_category_m(n=5, m=4))

    category_5_id = SelectField(label=R.string.category_n(5))
    category_5_image = SelectField(label=R.string.image_of_category_n(5))
    subcategory_1_of_category_5_id = SelectField(label=R.string.subcategory_n_of_category_m(n=1, m=5))
    subcategory_2_of_category_5_id = SelectField(label=R.string.subcategory_n_of_category_m(n=2, m=5))
    subcategory_3_of_category_5_id = SelectField(label=R.string.subcategory_n_of_category_m(n=3, m=5))
    subcategory_4_of_category_5_id = SelectField(label=R.string.subcategory_n_of_category_m(n=4, m=5))
    subcategory_5_of_category_5_id = SelectField(label=R.string.subcategory_n_of_category_m(n=5, m=5))

    category_6_id = SelectField(label=R.string.category_n(6))
    category_6_image = SelectField(label=R.string.image_of_category_n(6))
    subcategory_1_of_category_6_id = SelectField(label=R.string.subcategory_n_of_category_m(n=1, m=6))
    subcategory_2_of_category_6_id = SelectField(label=R.string.subcategory_n_of_category_m(n=2, m=6))
    subcategory_3_of_category_6_id = SelectField(label=R.string.subcategory_n_of_category_m(n=3, m=6))
    subcategory_4_of_category_6_id = SelectField(label=R.string.subcategory_n_of_category_m(n=4, m=6))
    subcategory_5_of_category_6_id = SelectField(label=R.string.subcategory_n_of_category_m(n=5, m=6))

    submit = SubmitField(label=R.string.save)

    def __init__(self, home_content=None, **kwargs):
        super(MoreCategoriesSectionForm, self).__init__(**kwargs)

        dependent_choices = {}
        for category in ProductCategory.get_all():
            if category.active:
                choices = []
                choices.append((str(0), R.string.none_in_female))
                for subcategory in category.subcategories:
                    if subcategory.active:
                        choices.append((str(subcategory.id), subcategory.name))
                dependent_choices[str(category.id)] = choices
        dependent_choices[str(0)] = [(str(0), R.string.none_in_female)]

        product_category_choices = ProductCategory.get_choices(include_all=False, include_none=True, only_active=True)
        product_subcategory_choices = ProductSubcategory.get_choices(include_all=False, include_none=True, only_active=True)

        image_choices_with_none = get_image_choices(include_none=True)

        self.category_1_id.choices = product_category_choices
        self.category_1_image.choices = image_choices_with_none
        self.subcategory_1_of_category_1_id.choices = product_subcategory_choices
        self.subcategory_2_of_category_1_id.choices = product_subcategory_choices
        self.subcategory_3_of_category_1_id.choices = product_subcategory_choices
        self.subcategory_4_of_category_1_id.choices = product_subcategory_choices
        self.subcategory_5_of_category_1_id.choices = product_subcategory_choices
        dict_of_category_1 = dict(
            depends_on="category_1_id",
            dependent_choices=json.dumps(dependent_choices)
        )
        self.subcategory_1_of_category_1_id.render_kw = dict_of_category_1
        self.subcategory_2_of_category_1_id.render_kw = dict_of_category_1
        self.subcategory_3_of_category_1_id.render_kw = dict_of_category_1
        self.subcategory_4_of_category_1_id.render_kw = dict_of_category_1
        self.subcategory_5_of_category_1_id.render_kw = dict_of_category_1

        self.category_2_id.choices = product_category_choices
        self.category_2_image.choices = image_choices_with_none
        self.subcategory_1_of_category_2_id.choices = product_subcategory_choices
        self.subcategory_2_of_category_2_id.choices = product_subcategory_choices
        self.subcategory_3_of_category_2_id.choices = product_subcategory_choices
        self.subcategory_4_of_category_2_id.choices = product_subcategory_choices
        self.subcategory_5_of_category_2_id.choices = product_subcategory_choices
        dict_of_category_2 = dict(
            depends_on="category_2_id",
            dependent_choices=json.dumps(dependent_choices)
        )
        self.subcategory_1_of_category_2_id.render_kw = dict_of_category_2
        self.subcategory_2_of_category_2_id.render_kw = dict_of_category_2
        self.subcategory_3_of_category_2_id.render_kw = dict_of_category_2
        self.subcategory_4_of_category_2_id.render_kw = dict_of_category_2
        self.subcategory_5_of_category_2_id.render_kw = dict_of_category_2

        self.category_3_id.choices = product_category_choices
        self.category_3_image.choices = image_choices_with_none
        self.subcategory_1_of_category_3_id.choices = product_subcategory_choices
        self.subcategory_2_of_category_3_id.choices = product_subcategory_choices
        self.subcategory_3_of_category_3_id.choices = product_subcategory_choices
        self.subcategory_4_of_category_3_id.choices = product_subcategory_choices
        self.subcategory_5_of_category_3_id.choices = product_subcategory_choices
        dict_of_category_3 = dict(
            depends_on="category_3_id",
            dependent_choices=json.dumps(dependent_choices)
        )
        self.subcategory_1_of_category_3_id.render_kw = dict_of_category_3
        self.subcategory_2_of_category_3_id.render_kw = dict_of_category_3
        self.subcategory_3_of_category_3_id.render_kw = dict_of_category_3
        self.subcategory_4_of_category_3_id.render_kw = dict_of_category_3
        self.subcategory_5_of_category_3_id.render_kw = dict_of_category_3

        self.category_4_id.choices = product_category_choices
        self.category_4_image.choices = image_choices_with_none
        self.subcategory_1_of_category_4_id.choices = product_subcategory_choices
        self.subcategory_2_of_category_4_id.choices = product_subcategory_choices
        self.subcategory_3_of_category_4_id.choices = product_subcategory_choices
        self.subcategory_4_of_category_4_id.choices = product_subcategory_choices
        self.subcategory_5_of_category_4_id.choices = product_subcategory_choices
        dict_of_category_4 = dict(
            depends_on="category_4_id",
            dependent_choices=json.dumps(dependent_choices)
        )
        self.subcategory_1_of_category_4_id.render_kw = dict_of_category_4
        self.subcategory_2_of_category_4_id.render_kw = dict_of_category_4
        self.subcategory_3_of_category_4_id.render_kw = dict_of_category_4
        self.subcategory_4_of_category_4_id.render_kw = dict_of_category_4
        self.subcategory_5_of_category_4_id.render_kw = dict_of_category_4

        self.category_5_id.choices = product_category_choices
        self.category_5_image.choices = image_choices_with_none
        self.subcategory_1_of_category_5_id.choices = product_subcategory_choices
        self.subcategory_2_of_category_5_id.choices = product_subcategory_choices
        self.subcategory_3_of_category_5_id.choices = product_subcategory_choices
        self.subcategory_4_of_category_5_id.choices = product_subcategory_choices
        self.subcategory_5_of_category_5_id.choices = product_subcategory_choices
        dict_of_category_5 = dict(
            depends_on="category_5_id",
            dependent_choices=json.dumps(dependent_choices)
        )
        self.subcategory_1_of_category_5_id.render_kw = dict_of_category_5
        self.subcategory_2_of_category_5_id.render_kw = dict_of_category_5
        self.subcategory_3_of_category_5_id.render_kw = dict_of_category_5
        self.subcategory_4_of_category_5_id.render_kw = dict_of_category_5
        self.subcategory_5_of_category_5_id.render_kw = dict_of_category_5

        self.category_6_id.choices = product_category_choices
        self.category_6_image.choices = image_choices_with_none
        self.subcategory_1_of_category_6_id.choices = product_subcategory_choices
        self.subcategory_2_of_category_6_id.choices = product_subcategory_choices
        self.subcategory_3_of_category_6_id.choices = product_subcategory_choices
        self.subcategory_4_of_category_6_id.choices = product_subcategory_choices
        self.subcategory_5_of_category_6_id.choices = product_subcategory_choices
        dict_of_category_6 = dict(
            depends_on="category_6_id",
            dependent_choices=json.dumps(dependent_choices)
        )
        self.subcategory_1_of_category_6_id.render_kw = dict_of_category_6
        self.subcategory_2_of_category_6_id.render_kw = dict_of_category_6
        self.subcategory_3_of_category_6_id.render_kw = dict_of_category_6
        self.subcategory_4_of_category_6_id.render_kw = dict_of_category_6
        self.subcategory_5_of_category_6_id.render_kw = dict_of_category_6

        if home_content is not None:
            self.category_1_id.data = str(
                home_content.more_categories_section_category_1_id)
            self.subcategory_1_of_category_1_id.data = str(
                home_content.more_categories_section_subcategory_1_of_category_1_id)
            self.subcategory_2_of_category_1_id.data = str(
                home_content.more_categories_section_subcategory_2_of_category_1_id)
            self.subcategory_3_of_category_1_id.data = str(
                home_content.more_categories_section_subcategory_3_of_category_1_id)
            self.subcategory_4_of_category_1_id.data = str(
                home_content.more_categories_section_subcategory_4_of_category_1_id)
            self.subcategory_5_of_category_1_id.data = str(
                home_content.more_categories_section_subcategory_5_of_category_1_id)

            self.category_2_id.data = str(
                home_content.more_categories_section_category_2_id)
            self.subcategory_1_of_category_2_id.data = str(
                home_content.more_categories_section_subcategory_1_of_category_2_id)
            self.subcategory_2_of_category_2_id.data = str(
                home_content.more_categories_section_subcategory_2_of_category_2_id)
            self.subcategory_3_of_category_2_id.data = str(
                home_content.more_categories_section_subcategory_3_of_category_2_id)
            self.subcategory_4_of_category_2_id.data = str(
                home_content.more_categories_section_subcategory_4_of_category_2_id)
            self.subcategory_5_of_category_2_id.data = str(
                home_content.more_categories_section_subcategory_5_of_category_2_id)

            self.category_3_id.data = str(
                home_content.more_categories_section_category_3_id)
            self.subcategory_1_of_category_3_id.data = str(
                home_content.more_categories_section_subcategory_1_of_category_3_id)
            self.subcategory_2_of_category_3_id.data = str(
                home_content.more_categories_section_subcategory_2_of_category_3_id)
            self.subcategory_3_of_category_3_id.data = str(
                home_content.more_categories_section_subcategory_3_of_category_3_id)
            self.subcategory_4_of_category_3_id.data = str(
                home_content.more_categories_section_subcategory_4_of_category_3_id)
            self.subcategory_5_of_category_3_id.data = str(
                home_content.more_categories_section_subcategory_5_of_category_3_id)

            self.category_4_id.data = str(
                home_content.more_categories_section_category_4_id)
            self.subcategory_1_of_category_4_id.data = str(
                home_content.more_categories_section_subcategory_1_of_category_4_id)
            self.subcategory_2_of_category_4_id.data = str(
                home_content.more_categories_section_subcategory_2_of_category_4_id)
            self.subcategory_3_of_category_4_id.data = str(
                home_content.more_categories_section_subcategory_3_of_category_4_id)
            self.subcategory_4_of_category_4_id.data = str(
                home_content.more_categories_section_subcategory_4_of_category_4_id)
            self.subcategory_5_of_category_4_id.data = str(
                home_content.more_categories_section_subcategory_5_of_category_4_id)

            self.category_5_id.data = str(
                home_content.more_categories_section_category_5_id)
            self.subcategory_1_of_category_5_id.data = str(
                home_content.more_categories_section_subcategory_1_of_category_5_id)
            self.subcategory_2_of_category_5_id.data = str(
                home_content.more_categories_section_subcategory_2_of_category_5_id)
            self.subcategory_3_of_category_5_id.data = str(
                home_content.more_categories_section_subcategory_3_of_category_5_id)
            self.subcategory_4_of_category_5_id.data = str(
                home_content.more_categories_section_subcategory_4_of_category_5_id)
            self.subcategory_5_of_category_5_id.data = str(
                home_content.more_categories_section_subcategory_5_of_category_5_id)

            self.category_6_id.data = str(
                home_content.more_categories_section_category_6_id)
            self.subcategory_1_of_category_6_id.data = str(
                home_content.more_categories_section_subcategory_1_of_category_6_id)
            self.subcategory_2_of_category_6_id.data = str(
                home_content.more_categories_section_subcategory_2_of_category_6_id)
            self.subcategory_3_of_category_6_id.data = str(
                home_content.more_categories_section_subcategory_3_of_category_6_id)
            self.subcategory_4_of_category_6_id.data = str(
                home_content.more_categories_section_subcategory_4_of_category_6_id)
            self.subcategory_5_of_category_6_id.data = str(
                home_content.more_categories_section_subcategory_5_of_category_6_id)


class BlogSectionForm(FlaskForm):
    active = BooleanField(
        label=R.string.active_in_female,
        default=False
    )
    name = StringField(
        label=R.string.section_name,
        validators=[
            Length(max_length=R.dimen.blog_section_name_max_length)
        ])
    link = StringField(
        label=R.string.link,
        validators=[
            Length(max_length=R.dimen.link_max_length)
        ]
    )
    post_1_id = SelectField(label=R.string.get_post_n(1))
    post_2_id = SelectField(label=R.string.get_post_n(2))

    submit = SubmitField(label=R.string.save)

    def __init__(self, home_content=None, blog_section_number=None, **kwargs):
        super(BlogSectionForm, self).__init__(**kwargs)
        post_choices_with_none = BlogPost.get_choices(include_none=True, only_active=True)
        self.post_1_id.choices = post_choices_with_none
        self.post_2_id.choices = post_choices_with_none

        if home_content != None and blog_section_number != None:
            assert blog_section_number in range(1, 3+1)
            if blog_section_number == 1:
                self.active.data = home_content.blog_section_1_active
                self.name.data = home_content.blog_section_1_name
                self.link.data = home_content.blog_section_1_link
                self.post_1_id.data = str(home_content.blog_section_1_post_1_id)
                self.post_2_id.data = str(home_content.blog_section_1_post_2_id)
            elif blog_section_number == 2:
                self.active.data = home_content.blog_section_2_active
                self.name.data = home_content.blog_section_2_name
                self.link.data = home_content.blog_section_2_link
                self.post_1_id.data = str(home_content.blog_section_2_post_1_id)
                self.post_2_id.data = str(home_content.blog_section_2_post_2_id)
            else:
                self.active.data = home_content.blog_section_3_active
                self.name.data = home_content.blog_section_3_name
                self.link.data = home_content.blog_section_3_link
                self.post_1_id.data = str(home_content.blog_section_3_post_1_id)
                self.post_2_id.data = str(home_content.blog_section_3_post_2_id)


class ContactForm(FlaskForm):
    address = TextAreaField(
        label=R.string.address,
        validators=[
            MarkdownValidator()
        ]
    )
    tel = TelField(
        label=R.string.telephone,
        validators=[
            PhoneFormat(can_be_empty=True),
            Length(max_length=R.dimen.tel_max_length)
        ]
    )
    email = StringField(
        label=R.string.email,
        validators=[
            EmailFormat(can_be_empty=True),
            Length(max_length=R.dimen.email_max_length)
        ]
    )

    facebook_active = BooleanField(
        label=R.string.active,
        default=False
    )
    facebook_link = StringField(
        label=R.string.link
    )

    googleplus_active = BooleanField(
        label=R.string.active,
        default=False
    )
    googleplus_link = StringField(
        label=R.string.link
    )

    twitter_active = BooleanField(
        label=R.string.active,
        default=False
    )
    twitter_link = StringField(
        label=R.string.link
    )

    youtube_active = BooleanField(
        label=R.string.active,
        default=False
    )
    youtube_link = StringField(
        label=R.string.link
    )

    pintrest_active = BooleanField(
        label=R.string.active,
        default=False
    )
    pintrest_link = StringField(
        label=R.string.link
    )

    submit = SubmitField(label=R.string.save)

    def __init__(self, contact=None, **kwargs):
        super(ContactForm, self).__init__(**kwargs)

        if contact != None:
            self.address.data = contact.address_markdown
            self.tel.data = contact.tel
            self.email.data = contact.email

            self.facebook_active.data = contact.facebook_active
            self.facebook_link.data = safe_string(contact.facebook_link)

            self.googleplus_active.data = contact.googleplus_active
            self.googleplus_link.data = safe_string(contact.googleplus_link)

            self.twitter_active.data = contact.twitter_active
            self.twitter_link.data = safe_string(contact.twitter_link)

            self.youtube_active.data = contact.youtube_active
            self.youtube_link.data = safe_string(contact.youtube_link)

            self.pintrest_active.data = contact.pintrest_active
            self.pintrest_link.data = safe_string(contact.pintrest_link)


class TagsRowForm(FlaskForm):
    tag_1_image = SelectField(label=R.string.image_of_tag_n(1))
    tag_1_title = StringField(label=R.string.title_of_tag_n(1), validators=[Length(max_length=R.dimen.tag_title_max_length)])
    tag_1_subtitle = StringField(label=R.string.subtitle_of_tag_n(1), validators=[Length(max_length=R.dimen.tag_subtitle_max_length)])

    tag_2_image = SelectField(label=R.string.image_of_tag_n(2))
    tag_2_title = StringField(label=R.string.title_of_tag_n(2), validators=[Length(max_length=R.dimen.tag_title_max_length)])
    tag_2_subtitle = StringField(label=R.string.subtitle_of_tag_n(2), validators=[Length(max_length=R.dimen.tag_subtitle_max_length)])

    tag_3_image = SelectField(label=R.string.image_of_tag_n(3))
    tag_3_title = StringField(label=R.string.title_of_tag_n(3), validators=[Length(max_length=R.dimen.tag_title_max_length)])
    tag_3_subtitle = StringField(label=R.string.subtitle_of_tag_n(3), validators=[Length(max_length=R.dimen.tag_subtitle_max_length)])

    submit = SubmitField(label=R.string.save)

    def __init__(self, tags_row=None, **kwargs):
        super(TagsRowForm, self).__init__(**kwargs)

        image_choices = get_image_choices(include_none=True)

        self.tag_1_image.choices = image_choices
        self.tag_2_image.choices = image_choices
        self.tag_3_image.choices = image_choices

        if tags_row != None:
            self.tag_1_image.data = tags_row.tag_1_image
            self.tag_1_title.data = tags_row.tag_1_title
            self.tag_1_subtitle.data = tags_row.tag_1_subtitle

            self.tag_2_image.data = tags_row.tag_2_image
            self.tag_2_title.data = tags_row.tag_2_title
            self.tag_2_subtitle.data = tags_row.tag_2_subtitle

            self.tag_3_image.data = tags_row.tag_3_image
            self.tag_3_title.data = tags_row.tag_3_title
            self.tag_3_subtitle.data = tags_row.tag_3_subtitle


class AboutUsForm(FlaskForm):
    summary = TextAreaField(
        label=R.string.summary,
        validators=[
            MarkdownValidator()
        ]
    )
    content = TextAreaField(
        label=R.string.complete_content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, about_us=None, **kwargs):
        super(AboutUsForm, self).__init__(**kwargs)

        if about_us != None:
            self.summary.data = about_us.summary_markdown
            self.content.data = about_us.content_markdown


class FaqForm(FlaskForm):
    content = TextAreaField(
        label=R.string.content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, faq=None, **kwargs):
        super(FaqForm, self).__init__(**kwargs)

        if faq != None:
            self.content.data = faq.content_markdown


class PaymentForm(FlaskForm):
    content = TextAreaField(
        label=R.string.content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, payment=None, **kwargs):
        super(PaymentForm, self).__init__(**kwargs)

        if payment != None:
            self.content.data = payment.content_markdown


class DispatchForm(FlaskForm):
    content = TextAreaField(
        label=R.string.content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, dispatch=None, **kwargs):
        super(DispatchForm, self).__init__(**kwargs)

        if dispatch != None:
            self.content.data = dispatch.content_markdown


class ExchangesAndReturnsForm(FlaskForm):
    content = TextAreaField(
        label=R.string.content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, exchange_and_returns=None, **kwargs):
        super(ExchangesAndReturnsForm, self).__init__(**kwargs)

        if exchange_and_returns != None:
            self.content.data = exchange_and_returns.content_markdown


class HeaderForm(FlaskForm):
    n_visible_categories = IntegerField(
        label=R.string.n_visible_categories,
        validators=[
            Required()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, header=None, **kwargs):
        super(HeaderForm, self).__init__(**kwargs)

        if header is not None:
            self.n_visible_categories.data = header.n_visible_categories


class FooterForm(FlaskForm):
    lower_text = TextAreaField(
        label=R.string.lower_text,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def __init__(self, footer=None, **kwargs):
        super(FooterForm, self).__init__(**kwargs)

        if footer is not None:
            self.lower_text.data = footer.lower_text_markdown
