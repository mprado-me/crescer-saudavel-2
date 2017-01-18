# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from sqlalchemy import asc
from sqlalchemy import desc

from components.data_providers.paginator import paginator_data_provider
from components.data_providers.super_table import super_table_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_boolean_url_arg
from models.blog_post import BlogPost
from r import R
from routers.admin_blog.forms import BlogPostFilterForm
from wrappers.base.forms import SubmitForm


class AdminPostsDataProvider:
    def __init__(self):
        self.sort_method_ids = [
            R.id.SORT_METHOD_ID,
            R.id.SORT_METHOD_TITLE,
            R.id.SORT_METHOD_NEWEST,
            R.id.SORT_METHOD_OLDER
        ]
        self.sort_method_names = [
            R.string.id,
            R.string.title,
            R.string.newest,
            R.string.older,
        ]
        self.sort_method_by_id = {
            R.id.SORT_METHOD_ID: asc(BlogPost.id),
            R.id.SORT_METHOD_TITLE: asc(BlogPost.title),
            R.id.SORT_METHOD_NEWEST: desc(BlogPost.datetime),
            R.id.SORT_METHOD_OLDER: asc(BlogPost.datetime),
        }

    def get_data(self):
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NEWEST, possible_values=self.sort_method_ids)

        self.q = BlogPost.query
        self.q = self.q.filter(BlogPost.active == active)
        self.q = self.q.order_by(self.sort_method_by_id[sort_method_id])

        n_posts = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_posts)

        filter_form = BlogPostFilterForm()
        filter_form.set_values(active=active)

        return dict(
            n_items=n_posts,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_posts)
            ),
            filter_data=dict(
                filter_form=filter_form
            ),
            sort_methods=super_table_data_provider.get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_ids=self.sort_method_ids,
                sort_method_names=self.sort_method_names
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, blog_post in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(blog_post.id),
                blog_post.active,
                blog_post.title,
                blog_post.get_formatted_datetime(),
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes="edit",
                        href=url_for("admin_blog.edit_post", blog_post_id=blog_post.id),
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=blog_post.active,
                        form=SubmitForm(),
                        meta_data= {
                            "data-active-col-id": "active"
                        },
                        to_activate_url=url_for(
                            "admin_blog.to_activate_post", blog_post_id=blog_post.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_post_error(blog_post),
                        },
                        disable_url = url_for(
                                "admin_blog.disable_post", blog_post_id=blog_post.id),
                        disable_meta_data= {
                            "data-error-msg": R.string.disable_post_error(blog_post),
                        }
                    ),
                ]
            ])

        return dict(
            id="posts-table",
            cols=[
                dict(
                    id="id",
                    title=R.string.id,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="active",
                    title=R.string.active,
                    type=R.id.COL_TYPE_BOOL
                ),
                dict(
                    id="title",
                    title=R.string.title,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="date",
                    title=R.string.date,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION,
                    expandable=False
                )
            ],
            rows=rows
        )


admin_posts_data_provider = AdminPostsDataProvider()