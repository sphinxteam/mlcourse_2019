# Installation requirements

## JupyterLab

For the `Explore_cycle_share_data.ipynb` notebook, we strongly encourage you to use the new 
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) IDE instead of the classic Jupyter Notebook.
One reason is that the [altair](https://altair-viz.github.io/) package needed for data visualization is easier to install with JupyterLab. The other reason is that JupyterLab is a greatly improved IDE and will eventually replace the Jupyter Notebook !

To install JupyterLab:
```bash
conda install -c conda-forge jupyterlab
```

To start JupyterLab:
```bash
jupyter lab
```

## Additional packages

In this notebook we will be using the following packages:

- [altair](https://altair-viz.github.io/) for data visualization
- [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/) for interactive maps

To install these packages:
```bash
# altair 
conda install -c conda-forge altair vega_datasets vega
# ipyleaflet
conda install -c conda-forge ipyleaflet
jupyter labextension install jupyter-leaflet
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```