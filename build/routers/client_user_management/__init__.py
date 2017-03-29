# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

client_user_management_blueprint = Blueprint("client_user_management", __name__, static_folder="static", template_folder="templates")

import views