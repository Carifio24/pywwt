from ipyevents import Event as DOMListener
import ipywidgets as widgets
from os.path import dirname, exists, join
from os import getcwd, remove, symlink
import solara
from solara.routing import Router

from .core import BaseWWTWidget
from .jupyter import WWTJupyterWidget


dom_listener = DOMListener()

class WWTSolaraWidget(WWTJupyterWidget):

    def __init__(self, hide_all_chrome=False, app_url=None):

        if app_url is None:
            app_url = "https://web.wwtassets.org/research/latest/"
            # settings = solara.server.settings.main
            # for attr in dir(settings):
            #     print(attr, getattr(settings, attr))
            # app_path = join(dirname(__file__), "web_static", "research", "index.html")
            # print(app_path)
            # router = solara.use_router()
            # print(dir(router))
            # relative_asset_path = join("public", "wwt.html")
            # self.static_path = join(getcwd(), relative_asset_path)
            # print(self.static_path)
            # symlink(app_path, self.static_path)
            # app_url = join(settings.base_url, "static", "public", "assets", "wwt.html")
            # print(app_url)
        else:
            self.static_path = None
        self._appUrl = app_url

        widgets.DOMWidget.__init__(self)
        dom_listener.prevent_default_action = True
        dom_listener.watched_events = ["wheel"]
 
        self._controls = None

        self.on_msg(self._on_ipywidgets_message)

        BaseWWTWidget.__init__(self, hide_all_chrome=hide_all_chrome)

    def __del__(self):
        if self.static_path is not None:
            remove(self.static_path)
        super().__del__()

