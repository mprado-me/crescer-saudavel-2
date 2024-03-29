/**
 * Created by marco on 09/05/17.
 */
function initAllMarkdownTextArea() {
    $("button.markdown.preview").each(function () {
        var button = $(this);
        var modal = $("{0}".f(button.attr("data-target")));
        var url = button.attr("data-url");
        var loading_message = button.attr("data-loading-message");
        var error_message = button.attr("data-error-message");
        var modal_body = modal.find(".modal-body");
        var textarea = $("{0}".f(button.attr("data-textarea")));

        setAjaxButtonHandlers({
            button: button,
            url: url,
            method: "post",
            contentType: 'application/json;charset=UTF-8',
            minResponseTime: 900,
            onClick: function () {
                modal_body.html(loading_message);
                console.log("onClick");
                return JSON.stringify({"markdown_text": textarea.val()}, null, '\t')
            },
            success: function (data) {
                if (data != null && "markdown_html" in data) {
                    modal_body.html(data.markdown_html);
                }
                else {
                    modal_body.html(error_message);
                }
            },
            error: function () {
                console.log("error");
                modal_body.html(error_message);
            }
        })
    });
}

function initAllDynamicSelects() {
    $("select.dynamic").each(function () {
        var dynamicSelect = $(this);
        var determinantSelect = $("select[id={0}]".f(dynamicSelect.attr("determinant-select-id")));
        onDeterminantSelectChange(dynamicSelect, determinantSelect);
        determinantSelect.on("change", function () {
            onDeterminantSelectChange(dynamicSelect, determinantSelect);
        });
    });
}

function onDeterminantSelectChange(dynamicSelect, determinantSelect) {
    var newDeterminantSelectValue = determinantSelect.val();
    if(newDeterminantSelectValue != null){
        var dynamicChoicesData = JSON.parse(dynamicSelect.attr("dynamic-choices-data"));
        options = [];
        dynamicChoicesData[newDeterminantSelectValue.toString()].forEach(function (element) {
            options.push(new Option(element[1], parseInt(element[0])));
        });
        dynamicSelect.find("option[value]").remove();
        dynamicSelect.append(options).val("").trigger("change");
    }
}
