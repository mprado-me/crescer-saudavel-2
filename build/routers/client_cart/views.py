# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_cart import client_cart_blueprint


@client_cart_blueprint.route("/")
def cart():
    return "Carrinho."
