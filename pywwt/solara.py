from ipyevents import Event as DOMListener
import ipywidgets as widgets
from os.path import dirname, join

from .core import BaseWWTWidget
from .jupyter import WWTJupyterWidget


dom_listener = DOMListener()

class WWTSolaraWidget(WWTJupyterWidget):

    def __init__(self, hide_all_chrome=False, app_url=None):

        if app_url is None:
           app_url = join(dirname(__file__), "web_static", "research", "index.html")
        self._appUrl = app_url

        widgets.DOMWidget.__init__(self)
        dom_listener.prevent_default_action = True
        dom_listener.watched_events = ["wheel"]
 
        self._controls = None

        self.on_msg(self._on_ipywidgets_message)

        BaseWWTWidget.__init__(self, hide_all_chrome=hide_all_chrome)
