from flask_admin.form import rules
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class DispatchView(BaseContentView):
    name = R.string.dispatch
    endpoint = R.string.dispatch_endpoint

    column_formatters = dict(
        content_html=ProjBaseView.html_formatter
    )
    column_list = ['content_html']

    form_args = dict(
        content_markdown=dict(
            render_kw=dict(
                example=R.string.markdown_example
            )
        )
    )
    form_excluded_columns = ["content_html"]
    form_rules = (
        rules.Field('content_markdown', render_field='markdown_text'),
    )