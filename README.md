# AIforSEA Challenge

<a href="https://www.aiforsea.com/"><h2 align="center">AI for S.E.A.</h2></a>

<p align="center">
  Based on telematics data, how might we detect if the driver is driving dangerously?   
  <br>
  <strong>Category: </strong> Safety
  <br><br>
  <a href="https://www.aiforsea.com/traffic-management">
    <img alt="Traffic Management" height="50%" width="50%" src="https://static.wixstatic.com/media/397bed_1b867ef7b8e84c3f841bc8f7aa9ea9b6~mv2.png/v1/fill/w_279,h_279,al_c,q_80,usm_0.66_1.00_0.01/Grab%20EDM_Traffic%20Management.webp">
  </a>
</p>

---

### Table of Contents

- [Problem Statement](#Problem-Statement)
- [Instructions](#Instructions)
- [Data Preprocessing](#Data-Preprocessing)
- [Feature Selection](#Feature-Selection)
- [Models](#Models)
- [References](#References)

---

### Problem Statement

https://www.aiforsea.com/safety

Given the telematics data for each trip and the label if the trip is tagged as dangerous driving, derive a model that can detect dangerous driving trips.

---

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
  |__safety-models.ipynb
  |__safety_preprocessing.py
```

Getting the new dataset:

1. Run all of the cells in **safety-data-preprocessing.ipynb** to generate **safety_dataset_new.csv**.
2. Run all the cells in **safety-feature-selection.ipynb** to generate **safety_dataset_filtered.csv** from the previous CSV file. This performs feature selection.

Creating the model and evaluation:

3. Run all of the cells in **safety-model.ipynb**

---

### Data Preprocessing

The notebook for data preprocessing can be found [here](https://github.com/pinardy/aiforsea/blob/master/safety-data-preprocessing.ipynb).

For each trip (or bookingID), we obtain the the following for each feature

- average
- standard deviation
- maximum
- minimum
- 10th, 30th, 70th, 90th percentile
- length of trip (average speed \* time)

---

### Feature Selection

The notebook for feature selection can be found [here](https://github.com/pinardy/aiforsea/blob/master/safety-feature-selection.ipynb)

**Extra Tree Classifier** is used for extracting the top 10 features from our preprocessed dataset. Explanation for the chosen features can be found in the notebook.

---

### Models

The notebook for the models can be found [here](https://github.com/pinardy/aiforsea/blob/master/safety-models.ipynb).

Model Comparison:

| Model                  | Accuracy  | AUC       |
| ---------------------- | --------- | --------- |
| Random Forest          | **0.777** | **0.588** |
| Logistic Regression    | 0.753     | 0.500     |
| Support Vector Machine | 0.752     | 0.499     |
| Neural Network         | 0.745     | 0.532     |

From the above comparison, **Random Forest** is the best performing model.

---

### References

- [Fine-grained Abnormal Driving Behaviors
  Detection and Identification with Smartphones
  ](http://www.cs.sjtu.edu.cn/~jdyu/papers/2017_TMC_D3.pdf)
- [A Smartphone-based Sensing Platform to Model
  Aggressive Driving Behaviors
  ](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.857.8337&rep=rep1&type=pdf)
- [Predictive Modeling Using Telematics](http://www.reserveprism.com/docs/PredictiveModelingUsingTelematics.pdf)
