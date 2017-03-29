# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.r import R
from flask_bombril.utils import raise_with_stop


class Unique(object):
    def __init__(self, model, field, message=R.string.unique_field, stop=True):
        self.message = message
        self.model = model
        self.field = field
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise_with_stop(self)
