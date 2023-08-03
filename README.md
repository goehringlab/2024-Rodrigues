# Rodrigues et al., 2023

[![CC BY 4.0][cc-by-shield]][cc-by]
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsmbland/Rodrigues-et-al/HEAD?filepath=%2Fscripts/INDEX.ipynb)
[![run with docker](https://img.shields.io/badge/run%20with-docker-0db7ed?logo=docker)](https://www.docker.com/)

Analysis code for Rodrigues et al., 2023, with example datasets.

## Instructions

To run the notebooks interactively you have two options:

#### Option 1: Binder

To run in the cloud, click here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsmbland/Rodrigues-et-al/HEAD?filepath=%2Fscripts/INDEX.ipynb)

(Please note that it may take several minutes to open the notebook)

#### Option 2: Docker

Step 1: Make sure [Docker](https://www.docker.com/products/docker-desktop/) is installed and open on your machine 

Step 2: Download and run the Docker container: 

    docker run --rm -p 8888:8888 tsmbland/rodrigues-et-al

Once the Docker image has finished downloading, this will print two URLs at the bottom for you to copy and paste into your web browser to open up Jupyter (please try both)

Step 3: Navigate to _scripts/INDEX.ipynb_ to run the notebooks

Step 4: When finished, delete the image:

    docker image rm tsmbland/rodrigues-et-al

## Citation

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

