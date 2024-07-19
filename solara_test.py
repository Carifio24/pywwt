import solara
from solara.server.server import solara_static
from solara.autorouting import generate_routes, generate_routes_directory

import os
import pywwt
from pywwt.solara import WWTSolaraWidget


@solara.component
def Page():

    dir = os.path.dirname(pywwt.__file__)
    path = solara.Path(dir) / "web_static" / "research"
    routes = generate_routes_directory(path)
    WWTSolaraWidget.element()
    for route in routes:
        print(route.children)

# The following line is required only when running the code in a Jupyter notebook:
Page()
