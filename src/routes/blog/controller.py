# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from datetime import datetime
from flask import render_template, abort
from sqlalchemy import desc
from flask_bombril.utils.utils import get_int_from_request_arg, get_datetime_from_request_arg_as_unix_ms_timestamp, \
    get_string_from_request_arg
from models.blog.blog_post import BlogPost
from models.blog.blog_tag import BlogTag
from models.content.blog import BlogContent
from r import R
from routes.blog import blog_blueprint


@blog_blueprint.route("/")
def main():
    page = get_int_from_request_arg(R.string.page_arg_name, 1)
    tag_id = get_int_from_request_arg(R.string.tag_id_arg_name, 0)
    date = get_datetime_from_request_arg_as_unix_ms_timestamp(R.string.datetime_arg_name, datetime.now()).date()

    recent_blog_posts = BlogPost.query.order_by(desc(BlogPost.date), BlogPost.id).filter_by(active=True).limit(2).all()

    previous_posts_query = BlogPost.query.order_by(desc(BlogPost.date), BlogPost.id).filter_by(active=True)
    if len(recent_blog_posts) > 0:
        previous_posts_query = previous_posts_query.filter(BlogPost.id != recent_blog_posts[0].id)
    if len(recent_blog_posts) > 1:
        previous_posts_query = previous_posts_query.filter(BlogPost.id != recent_blog_posts[1].id)

    if tag_id != 0:
        previous_posts_query = previous_posts_query.filter(BlogPost.tags.any(BlogTag.id == tag_id))

    previous_posts_query = previous_posts_query.filter(BlogPost.date <= date)

    previous_posts_pagination = previous_posts_query.paginate(page=page, per_page=R.dimen.n_blog_posts_per_page)

    blog_tags = BlogTag.query.filter_by(active=True).all()

    return render_template(
        "blog/main.html",
        recent_blog_posts=recent_blog_posts,
        previous_posts_pagination=previous_posts_pagination,
        blog_tags=blog_tags,
        current_tag_id=tag_id,
        date=date,
        blog_content=BlogContent.get()
    )


@blog_blueprint.route("/busca")
def search():
    q = get_string_from_request_arg(R.string.search_query_arg_name, "")
    page = get_int_from_request_arg(R.string.page_arg_name, 1)

    blog_posts_query = BlogPost.query.order_by(desc(BlogPost.date), BlogPost.id) \
        .whoosh_search(q, or_=True)\
        .filter_by(active=True)

    blog_posts_pagination = blog_posts_query.paginate(page=page, per_page=R.dimen.n_blog_posts_per_page_in_search)

    return render_template("blog/search.html", q=q, blog_posts_pagination=blog_posts_pagination)


# noinspection PyShadowingBuiltins
@blog_blueprint.route("/post/<int:id>")
def post(id):
    blog_post = BlogPost.get(id)
    if not blog_post:
        abort(404)
    return render_template("blog/post.html", blog_post=blog_post)
