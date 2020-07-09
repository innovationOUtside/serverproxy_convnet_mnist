"""
Return config on servers to start for convnet_mnist
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import pkg_resources

def setup_convnet_mnist():
    fpath = pkg_resources.resource_filename('convnet_mnist', 'static/')
    return {
        'command': ["python", "-m", "http.server", "--directory", fpath, "{port}"],
        'environment': {},
        'launcher_entry': {
            'title': 'convnet_mnist',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'convnet_mnist.svg')
        }
    }
© 2020 GitHub, Inc.