# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from os.path import isfile, join

from flask import url_for
from markupsafe import Markup
from sqlalchemy.orm import relationship
from configs import default_app_config as config
from models.associations import blog_post_and_blog_tag_association_table
from models.base import BaseModel
from proj_extensions import db
from r import R


class BlogPost(BaseModel):
    __tablename__ = "blog_post"

    __searchable__ = [
        "title",
        "summary_html",
        "content_html"
    ]

    active = db.Column(db.Boolean, default=False, nullable=False)
    title = db.Column(db.String(R.dimen.blog_post_title_max_length), nullable=False)
    date = db.Column(db.Date, nullable=False)
    thumbnail_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    summary_markdown = db.Column(db.UnicodeText, nullable=False, default="")
    summary_html = db.Column(db.UnicodeText, nullable=False, default="")
    content_markdown = db.Column(db.UnicodeText, nullable=False, default="")
    content_html = db.Column(db.UnicodeText, nullable=False, default="")
    tags = relationship("BlogTag", secondary=blog_post_and_blog_tag_association_table, back_populates="blog_posts")

    def __repr__(self):
        html = [
            "<table>",
            "   <tr>",
            "       <td style='vertical-align: top;'><img src='%s' style='max-width: 96px;'></td>",
            "       <td style='padding-left: 4px;'>",
            "           <b><searchable>#%s</searchable></b><br><searchable>%s</searchable>",
            "       </td>",
            "   <tr>",
            "</table>"
        ]
        return Markup(''.join(html) % (self.get_thumbnail_src(), self.id, self.title))

    def get_thumbnail_src(self):
        if self.has_thumbnail_image():
            return join("/", config.BLOG_THUMBNAIL_IMAGES_FROM_STATIC_PATH, self.thumbnail_filename)
        else:
            return join("/", config.IMAGES_FROM_STATIC_PATH, R.string.blog_thumbnail_default_filename)

    def get_href(self):
        return url_for("blog.blog_post", blog_post_id=self.id)

    def get_thumbnail_wide_filename(self):
        if self.thumbnail_filename:
            return self.thumbnail_filename.split('.')[0] + "-wide." + self.thumbnail_filename.split('.')[1]
        return None

    def get_thumbnail_wide_src(self):
        if self.has_thumbnail_wide_image():
            return join("/", config.BLOG_THUMBNAIL_IMAGES_FROM_STATIC_PATH, self.get_thumbnail_wide_filename())
        else:
            return join("/", config.IMAGES_FROM_STATIC_PATH, R.string.blog_thumbnail_wide_default_filename)

    def has_thumbnail_image(self):
        return (self.thumbnail_filename is not None) and \
               isfile(join(config.BLOG_THUMBNAIL_IMAGES_FULL_PATH, self.thumbnail_filename))

    def has_thumbnail_wide_image(self):
        thumbnail_wide_filename = self.get_thumbnail_wide_filename()
        return (thumbnail_wide_filename is not None) and \
               isfile(join(config.BLOG_THUMBNAIL_IMAGES_FULL_PATH, thumbnail_wide_filename))
