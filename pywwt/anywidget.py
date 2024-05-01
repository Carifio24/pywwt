import os
import re
from dataclasses import asdict
from pathlib import Path
from traitlets import default

from anywidget import AnyWidget
from ipywidgets import Layout

from pywwt.core import BaseWWTWidget

bundler_output_dir = Path(__file__).parent / "web_static" / "research"
esm_dir = bundler_output_dir / "js"
css_dir = bundler_output_dir / "css"

esm_regex = re.compile("app.*.js")
for root, dirs, files in os.walk(esm_dir):
    for file in files:
        if esm_regex.match(file):
            esm_location = esm_dir / file
            break

css_regex = re.compile("app.*.css")
for root, dirs, files in os.walk(css_dir):
    for file in files:
        if css_regex.match(file):
            css_location = css_dir / file
            break

class WWTAnyWidget(AnyWidget, BaseWWTWidget):
    # _esm = esm_location
    # _css = css_location
    _esm = Path(__file__).parent / "main.js"
    _css = Path(__file__).parent / "style.css"

    def __init__(self, hide_all_chrome=False):
        AnyWidget.__init__(self)
        BaseWWTWidget.__init__(self, hide_all_chrome=hide_all_chrome)

        self.on_msg(self._on_app_message_received)

    def _actually_send_msg(self, msg, buffers=None):
        super().send(asdict(msg), buffers)

    @default("layout")
    def _default_layout(self):
        return Layout(height="400px", align_self="stretch")
