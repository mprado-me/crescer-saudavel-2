from admin.fields import MarkdownTextField
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class ExchangesAndReturnsContentView(BaseContentView):
    name = R.string.exchanges_and_returns
    endpoint = R.string.exchanges_and_returns_endpoint

    column_formatters = dict(
        content_html=ProjBaseView.html_formatter
    )
    column_list = ['content_html']

    form_excluded_columns = ["content_html"]
    form_extra_fields = dict(
        content_markdown=MarkdownTextField(label=R.string.content, example=R.string.markdown_example),
    )
    form_rules = (
        "content_markdown",
    )
