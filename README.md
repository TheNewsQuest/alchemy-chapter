<p align="center"><img src="https://i.ibb.co/MRsMLzR/image.png" width="500" height="280" /></p>

# Alchemy Chapter - Alchemists are magicians!

In this chapter, a magic spell will be used in order to cast arbitrary text content into wonderful quests! Be aware that this chapter can be quite heavy for setup and configuration as it's hard to do magic btw (for that reason, Docker is used to simplify the running process)!

## Installation guide

### Installing packages

    pip install -r requirements.txt

### Downloading data

#### Question-answer model

Download the [multitask-qg-ag-v2 model](https://drive.google.com/file/d/1-_XTBfJ7MQaECLSwwySpUIIQeC4P3ng1/view?usp=sharing) checkpoint and place it in the `app/ml_models/question_generation/models/` directory.

#### Distractor generation

Download the [race-distractors model](https://drive.google.com/file/d/1jKdcbc_cPkOnjhDoX4jMjljMkboF-5Jv/view?usp=sharing) checkpoint and place it in the `app/ml_models/distractor_generation/models/` directory.

Download [sense2vec](https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz), extract it and place the `s2v_old` folder and place it in the `app/ml_models/sense2vec_distractor_generation/models/` directory.

## Test run

### Run Flask

    export FLASK_APP=api_gateway.py
    export FLASK_ENV=development
    flask run

### Calling API

    cd test
    python test.py

## Training on your own

The training scripts are available in the `training` directory.
