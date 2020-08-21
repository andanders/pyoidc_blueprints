# pyoidc_blueprints
Prototype structure for multiple Flask blueprints in individual files, with shared authentication setup.

## Setup
- Install dependencies from pip or create Anaconda/Miniconda env with `conda env create -f environment.yml`
- Configure pyoidc by entering your OIDC settings in `config.py`
- Run Flask server `run.py`

## Test
- Enter the website and verify that login is required and that all routes are accessible.
- From `main_routes.py` `localhost:5000/about` and `localhost:5000/about`
- From `sub_routes.py` is `localhost:5000/aux`
