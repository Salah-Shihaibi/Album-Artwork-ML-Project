# INTRODUCING XAV BRUGGEN'S _ML Album Artwork Genre Predictor_

This is a Python project to predict the genre of an album based on the cover art.

## _Usage_

To use this repo locally, select the code link from above and make a local copy with:

- `git clone [YOUR_LINK_HERE]`

Change directory into server:
- `cd ./server`

Start a virtual environment with:

- `source PATH/venv/bin/activate`

Install required libraries by running the command below:

- `bash ./install_libraries.sh`



#### _Installation Requirements_

Run the following command in root:

`curl -sL https://firebase.tools | bash`

- python >= 3.10.2
- flask >= 2.0.3
- pytest >= 7.0.1
- flask_restful >= 0.3.9
- psycopg2 >= 2.9.3
- firebase-admin

To run a local server run the following command:
`bash ./start_flask.sh`

## _Testing_

Testing is completed with Pytest library. To run tests execute:

- `bash ./run_test.sh`

## _Linting_

Linting is preformed using pylint. To run the linter execute:

- `bash ./run_linting`


### _Containerisation_

To create an image of the app, navigate to the root directory and execute the following in the terminal:

- `docker composed build`

To create a container:

- `docker composed up`

### _Credits_

Built by [XAV BRUGGEN](https://github.com/gravybru), collaborators include:

- [Eden O'Brien](https://github.com/eobr)
- [Salah Shihaibi](https://github.com/salah-shihaibi)
- [Ed Heywood-Everett](https://github.com/edheyev)
- [Elliot Ferryman-Avery](https://github.com/TermMC)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
