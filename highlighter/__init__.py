"""Flask module
file: __init__.py
date: 12.12.2012
author smith@example.com
license: MIT"""

from flask import Flask, render_template, request, Markup


def create_app():
    """Create flask app for binding."""
    app = Flask(__name__)

    template_file_name = 'index.html'

    @app.route('/', methods=['GET'])
    def index():
        return render_template(template_file_name)

    @app.route('/', methods=['POST'])
    def process():
        search_text = request.form['search']
        text = request.form['text']
        highlighted_text = highlight_text(text, search_text)
        result = {'text': text,
                  'highlighted_text': Markup(highlighted_text),
                  }
        return render_template(template_file_name, **result)

    def highlight_text(text, search_text):
        """Markup searched string in given text.
        @:param text - string text to be processed
        @:return marked text, e.g., "sample text <mark>highlighted part</mark> rest of the text"."""
        lower_text, search_text = text.lower(), search_text.lower()
        highlighted_text = []
        open_tag = '<mark>'
        close_tag = '</mark>'

        search = 0
        while search < len(lower_text):
            search = lower_text.find(search_text, search, len(lower_text))
            if search != -1:
                result = highlighted_text.append(search)
                search = lower_text.find(search_text, search + 1, len(lower_text))
            else:
                break

        result = highlighted_text
        if len(result) > 0:
            result_1 = result
            result_1 = [i + len(search_text) for i in result_1]

            index = len(result) - 1
            new_text = text
            while index >= 0:
                marked_text = new_text[:result[index]] + \
                          open_tag + new_text[result[index]:result_1[index]] \
                          + close_tag + new_text[result_1[index]:]
                index -= 1
                new_text = marked_text
            return marked_text
        else:
            return text

    return app
