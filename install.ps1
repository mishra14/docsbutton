pip install -e ./jupyterliveshare
jupyter serverextension enable --py jupyterliveshare --sys-prefix
jupyter nbextension install --py jupyterliveshare --sys-prefix
jupyter nbextension enable --py jupyterliveshare --sys-prefix