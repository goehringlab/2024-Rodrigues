# Rodrigues et al., 2023

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tsmbland/Rodrigues-et-al/HEAD?filepath=%2Fscripts/INDEX.ipynb)
[![CC BY 4.0][cc-by-shield]][cc-by]

Analysis code for Rodrigues et al., 2023, with example datasets.

## Instructions

To run the notebooks interactively you have two options:

#### Option 1: Cloud

To run in the cloud, click the 'launch binder' button at the top. Please note that it may take several minutes to open the notebook

#### Option 2: Local

Step 1: Open [Docker](https://www.docker.com/products/docker-desktop/) and pull the docker image (copy and paste into the terminal)

    docker pull tsmbland/rodrigues-et-al

Step 2: Run the docker container (copy and paste into the terminal)

    docker run -p 8888:8888 tsmbland/rodrigues-et-al

This will print a URL for you to copy and paste into your web browser to open up Jupyter

Step 3: When finished, delete the container and image
    
    docker container prune -f
    docker image rm tsmbland/rodrigues-et-al
## Citation

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

