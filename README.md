# Rodrigues et al., 2024

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsmbland/Rodrigues-et-al/HEAD?filepath=%2Fscripts/INDEX.ipynb)

Analysis code for Rodrigues et al., 2024, with example datasets.

Contains the following notebooks outlining some of the analysis methods in the paper:

- [LOWESS](scripts/LOWESS.ipynb) 
Code for performing LOWESS scatterplot smoothing on dosage vs phenotype data (Figure 3)
- [Variance](scripts/Variance.ipynb)
Code for performing local variance estimation on dosage vs phenotype data (Figure 3)
- [Membrane quantification](scripts/Membrane_quantification.ipynb) 
Code for extracting membrane concentrations from midplane confocal images of embryos (Figure 4)

## Instructions

To run the notebooks interactively you have two options:

### Option 1: Local

Step 1: Open the terminal on your machine

Step 2: Download/clone the repo and navigate to the folder in your terminal

Step 3: Make sure you're running Python 3.11 or later (`python --version`). If you have an earlier version, look into [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) or [pyenv](https://github.com/pyenv/pyenv) for ways to manage multiple python versions on one machine.

Step 4: Create a virtual environment (`python -m venv .venv`) and activate it (`source .venv/bin/activate`, or `.venv/scripts/Activate.ps1` on Windows). You can also use a conda environment if you're more familiar with this.

Step 5: Install the requirements: `pip install -r requirements.txt`

Step 6: Open Jupyter: `jupyter notebook scripts/INDEX.ipynb`

### Option 2: Cloud

To run in the cloud, click here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsmbland/Rodrigues-et-al/HEAD?filepath=%2Fscripts/INDEX.ipynb)

(Please note that it may take several minutes to open the notebook, and it will sometimes fail to launch for unknown reasons)

## Citation

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

