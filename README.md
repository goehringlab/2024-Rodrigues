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

If you're using [conda]((https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)), just download the code, navigate to the code folder in your terminal, and run the following:

    conda env create -f environment.yml
    conda activate robustness-paper
    jupyter notebook scripts/INDEX.ipynb

Alternatively, you could create a [virtual environment](https://docs.python.org/3/library/venv.html) (with Python 3.11.6) and install the requirements using pip (`pip install -r requirements.txt`).
    
### Option 2: Cloud

To run in the cloud using Binder, click here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsmbland/Rodrigues-et-al/HEAD?filepath=%2Fscripts/INDEX.ipynb)

(Please note that it may take several minutes to open the notebook, and it will often fail to launch due to issues with the Binder server)

## Citation

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

