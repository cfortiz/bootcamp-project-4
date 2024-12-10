# Carlos' Audio Script

## Overview

For this project we analyzed crash and weather data to build a predictive model
evaluating the likelihood of injuries during motor vehicle accidents. Our
workflow included data preprocessing, dataset integration, machine learning
model implementation, optimization, and documentation.

Our goal is to derive meaningful predictive power with at least 75%
classification accuracy or an R-squared value of 0.80, aligning weather
conditions with crash patterns.

## Team

Our team is composed of:

* Elif Celebi
* Kiki Chan
* Elizabeth Conn
* Kassidy MunnMinoda
* Carlos Ortiz

## Problems

We had to obtain data from two differnt sources.  We obtained crash data from
the New York City public data APIs, and weather data from openweathermap.com.
Due to time and money constraints, we limited ourselves to historical weather
data from Manhattan from 2022 to present.

After obtaining the data, we had to merge it into a cohesive dataset that was
then processed to use one-hot encodings for categorical data to prepare for
training machine learning models.

## Models and Accuracy

Given that the dimensions on our data were mostly intuitive on their own, we
conceived of three possibilities: Deep Neural Networks, Random Forests, and
LSTM models (for time series).  Once we narrowed down our approach to exclude
time-series predictions, we ruled out LSTM, and opted to compare a neural
network model with a random forest model.

After tuning and training our models, we found that the neural network model
only performed barely above random chance with an accuracy of 59%, while the
random forest model performed with an accuracy of 97%.  Furthermore, the
hyperparameter tuning and training of the neural network model was significantly
slower than the training of the random forest model.
