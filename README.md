# AIforsea Challenge (Category: **Safety**)

### Table of Contents

1. Problem Statement
2. Code
3. Instructions
4. Experiments

### Problem Statement

Given the telematics data for each trip and the label if the trip is tagged as dangerous driving, derive a model that can detect dangerous driving trips.

### Code

Notebooks for each of the following can be accessed by clicking on the links below.

1. Data Preprocessing
2. Feature Selection
3. Models (Random Forest)

### Instructions

**NOTE:** This codebase contains jupyter notebooks for visualising the development processes and the results, as well as python scripts to obtain the modified dataset conveniently.

However, the features raw data is not in the repository due to its large size. You'll need to ensure that the features raw data is in the correct folder (safety > features)

After cloning this repository, ensure that you keep this directory structure:

```
aiforsea
  |__safety (folder)
     |__features (folder)
     |__labels (folder)
  |__safety-data-preprocessing.ipynb
  |__safety-feature-selection.ipynb
  |__safety-model.ipynb
  |__safety_preprocessing.py
```

Getting the new dataset:

1. Run all of the cells in **safety-data-preprocessing.ipynb** to generate **safety_dataset_new.csv**.
2. Run all the cells in **safety-feature-selection.ipynb** to generate **safety_dataset_filtered.csv** from the previous CSV file. This performs feature selection.

Creating the model and evaluation:

3. Run all of the cells in **safety-model.ipynb**

### Experiments

One of the most important experimentation is with feature engineering. Hence, I evaluated how the model would perform with different sets of data with different features

1. Using only average
2. Using average, min, max, std, 30th & 70th percentile
3. Performed feature selection with dataframe from (2)
4. Remove noise on the raw dataset through rolling mean

The AUC observed is as follows:

| Experiment |      AUC       |
| ---------- | :------------: |
| (1)        | 0.695536967717 |
| (2)        | 0.710761690154 |
| (3)        | 0.71311674188  |
