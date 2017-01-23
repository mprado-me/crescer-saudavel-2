# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_extensions import db
from models.base import BaseModel
from r import R


class Footer(BaseModel):
    lower_text = db.Column(db.String(R.dimen.footer_lower_text_max_length))

    @staticmethod
    def get():
        footers = Footer.query.all()
        assert len(footers)
        return footers[0]

    @staticmethod
    def set_values_from_form(footer_form):
        footer = Footer.get()
        footer.lower_text = footer_form.lower_text.data
        db.session.add(footer)
        db.session.commit()
