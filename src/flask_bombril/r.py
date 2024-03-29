# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from enum import Enum, unique


class Resources(object):
    # noinspection PyPep8Naming
    class string(object):
        test_message = "Mensagem de teste"
        test_message_2 = "Mensagem de teste 2"

        static = "static"
        toast = "toast"
        category_separator = "-"
        success = "success"
        info = "info"
        warning = "warning"
        error = "error"

        test_file_name = "test_file_name"
        png = "png"
        jpg = "jpg"
        jpeg = "jpeg"
        and_word = "e"
        comma = ","

        # validators
        required_field = "Campo obrigatório."
        invalid_email_format = "Formato de email inválido."
        email_already_registered = "Email já cadastrado."
        unique_field = "Valor já registrado."
        field_min_length_singular = "O campo deve possuir no mínimo %(min_length)d caracter."
        field_min_length_plural = "O campo deve possuir no mínimo %(min_length)d caracteres."
        field_max_length_singular = "O campo deve possuir no máximo %(max_length)d caracter."
        field_max_length_plural = "O campo deve possuir no máximo %(max_length)d caracteres."
        field_length_range = "O campo deve possuir entre %(min_length)d e %(max_length)d caracteres."
        invalid_field_name = "Invalid field name '%(field_name)s'."
        field_must_be_equal_to = "Este campo precisa ser igual ao campo %(other_name)s."
        always_error = "Essa mensagem de erro sempre será lançada para esse campo."
        file_part_not_found = "Arquivo não encontrado."
        invalid_file_extension = "Formato de arquivo inválido."
        invalid_phone_format = "Formato de telefone inválido."
        invalid_cep_format = "Formato de cep inválido. Ex.: 12210-250"
        unique_filename = "Um arquivo com o mesmo nome já existe."

        a = "a"
        b = "b"
        c = "c"
        d = "d"

        page_arg_name = "pagina"

        invalid_price_format = "Formato de preço inválido. Exemplos de preços válidos: 0,00 | 0,80 | 0.75 | 18,30"
        invalid_not_negative_integer = "O valor fornecido deve ser um inteiro não negativo."
        invalid_markdown_format = "Formatação Markdown inválida."

        find_file = "Procurar arquivo"
        prohibited_value = "Valor não permitido. Pro favor, entre com outro valor."

        @staticmethod
        def get_message_category(type, level):
            return type + Resources.string.category_separator + level

        @staticmethod
        def func_test_message(x):
            return "Test %s" % x

        @staticmethod
        def integer_in_range_error_message(min_value, max_value):
            return "O valor fornecido deve ser um inteiro entre %s e %s." % (min_value, max_value)

    # noinspection PyPep8Naming
    @unique
    class id(Enum):
        EXAMPLE = 1

    # noinspection PyPep8Naming
    class dimen(object):
        test_int = 42
        test_int_2 = 17
        min_page = 1
        integer_in_range_default_min_value = 0
        integer_in_range_default_max_value = 100

R = Resources()
