# MAIS202ML-Shakespeare-Translator
# Project Description
Work-in-Progress machine learning-based shakespearean english / modern english translator
Made as part of MAIS202 winter2021 bootcamp by Svyatoslav Sklokin and Éléa Dufresne
Translations scraped from https://www.sparknotes.com/shakespeare/.

# ----------------
This repo contains both a .ipynb file that houses the translator, and a flask-react.js webapp that uses it.
The former can be found in main/, and the latter in main/Webapp/.

Note that the training weights for the translator are too large to directly store on GitHub, and so may be
downloaded from Google Drive at https://drive.google.com/drive/folders/1qBMGpf5ZWLNjEFModRPmEQy4Wr4BYp0B?usp=sharing.
The expected location of these for the .ipynb file is main/checkpoints/train/.
The expected location of these for the webapp is main/Webapp/backend/model/checkpoints/train/.
train/ should contain 'ckpt-240.index', 'ckpt-240.data-00000-of-00001', and 'checkpoint'.

# ---------------
As it is still in development, the model is contained in a single .ipynb file. It is assumed that one
would not wish to run the notebook in its entirety (and spend four days straight training the thing), so it
is advised that one opens the notebook through Jupyter, Google Colaboratory or similar, rather than turning
it into a .py file and executing it.
