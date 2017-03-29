# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy.orm import relationship
from proj_extensions import db
from models.base import BaseModel
from proj_utils import SortMethodMap
from r import R


class City(BaseModel):
    __tablename__ = "city"

    name = db.Column(db.String(R.dimen.city_name_max_length))
    active = db.Column(db.Boolean, default=False, nullable=False)
    state_id = db.Column(db.Integer, ForeignKey("state.id"), nullable=False)
    state = relationship("State", back_populates="cities")

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_ID, R.string.id, asc("id")),
        (R.id.SORT_METHOD_NAME, R.string.city_name, asc(name)),
    ])

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            name=form.city_name.data,
            active=form.active.data,
            state_id=int(form.state_id.data)
        )

    @staticmethod
    def get_choices(include_undefined=False, include_all=False):
        assert not(include_undefined and include_all)
        choices = []
        if include_undefined:
            choices.append((str(0), R.string.undefined_feminine))
        if include_all:
            choices.append((str(0), R.string.all))
        for city in City.query.order_by(asc(City.name)).all():
            choices.append((str(city.id), city.name))
        return choices

    def disable(self):
        self.active = False
        db.session.add(self)
        db.session.commit()

    def to_activate(self):
        self.active = True
        db.session.add(self)
        db.session.commit()