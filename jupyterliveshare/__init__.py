from notebook.utils import url_path_join
from liveshare import LiveShareRequestHandler

def _jupyter_server_extension_paths():
    return [{
        "module": "jupyterliveshare"
    }]


def _jupyter_nbextension_paths():
    """Required to load JS button"""
    return [dict(
        section="notebook",
        src="static",
        dest="jupyterliveshare",
        require="jupyterliveshare/index")]


def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    web_app.add_handlers(host_pattern, [
        (url_path_join(web_app.settings['base_url'], r'/liveshare'),
         LiveShareRequestHandler)
    ])
