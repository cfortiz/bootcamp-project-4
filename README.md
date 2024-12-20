# bootcamp-project-4
Data Analytics BootCamp Project 4

**Overview**
This project analyzes crash and weather data to build a predictive model evaluating the likelihood of injuries during motor vehicle accidents. The workflow includes data preprocessing, dataset integration, machine learning model implementation, optimization, and documentation. The goal is to derive meaningful predictive power with at least 75% classification accuracy or an R-squared value of 0.80, aligning weather conditions with crash pattersn.


**Data Preprocessing**
The raw datasets include crash_data_2.csv containing crash records and new_york_weather.csv featuring weather observations. These datasets were merged to create a single file, merged_crash_weather_data.csv, which contains synchronized crash and weather information for analysis.

**Preparing the Data** To prepare the crash and weather datasets for merging, both datasets required cleaning and normalization. For the crash data, the crash_date and crash_time columns were combined into a single crash_datetime field to create a precise timestamp. Similarly, the weather data’s dt_iso column, representing ISO-formatted timestamps, was cleaned to remove timezone information and converted into a standardized datetime format. Both datetime columns were then rounded to the nearest hour to ensure alignment during the merge process.
The cleaned and normalized datetime columns allowed an inner join between the crash data (crash_datetime) and weather data (weather_datetime) on an hourly granularity. Irrelevant columns were dropped to focus on the essential features such as crash counts, weather conditions, and geospatial coordinates.
**Calculating Proximity Between Crash and Weather Observations** Since weather stations may not exactly align with crash locations, the geodesic distance between crash coordinates (latitude, longitude) and weather observation coordinates (lat, lon) was calculated. A distance threshold of 10,000 meters was used to filter the data, ensuring only relevant weather observations were associated with crashes. This calculation helped refine the dataset further, linking crashes to their most likely weather conditions.
**Output Dataset** The merged dataset was saved as merged_crash_weather_data.csv, featuring both crash-specific details and weather conditions at the time and location of each crash. The dataset is ready for machine learning tasks, with features like temperature, humidity, visibility, and crash injuries available for analysis.


**Machine Learning Implementation**
A machine learning pipeline was developed to train and evaluate models on the merged dataset. Two primary models were implemented: a Random Forest Classifier and a Neural Network. Both models utilized standardized data to optimize performance.

**Random Forest Classifier** The Random Forest Classifier was used to predict the likelihood of injuries in motor vehicle crashes. The data was split into training and testing sets, with features such as weather metrics (temperature, visibility, and humidity) and crash-specific metrics (e.g., number of persons injured). After training the model, it achieved a classification accuracy of 96.8%, surpassing the project’s target of 75%.
**Neural Network Model** A neural network was implemented using TensorFlow and Keras, with hyperparameter optimization performed via Keras Tuner. The hyperparameter tuning explored different configurations, including the number of layers, activation functions, and neurons per layer. While the neural network achieved a validation accuracy of 59.7%, it fell short of the Random Forest Classifier’s performance.

Hyperparameter tuning involved an iterative process where changes in the architecture were tracked, and performance improvements were documented. These results were stored in a CSV file for reference and analysis.


**Model Optimization and Evaluation**
The optimization process included iterative testing of hyperparameters and evaluating performance metrics like accuracy and R-squared. The results from each iteration were logged to track the impact of changes on the model’s effectiveness.
At the conclusion of the optimization, the Random Forest model emerged as the best-performing model with a test accuracy of 96.8%, while the neural network demonstrated limited improvements despite tuning.
The final results, including the feature importance rankings for the Random Forest model, were printed for interpretability and further analysis.

**Results**
The Random Forest Classifier demonstrated high predictive power with a classification accuracy of 96.8%. The Neural Network, though optimized with Keras Tuner, achieved a validation accuracy of 59.7%. These results highlight the effectiveness of ensemble methods for structured data like crash and weather records.
Feature importance rankings from the Random Forest model revealed that variables such as visibility, temperature, and the presence of rain were the most significant predictors of crash injuries.

**Future Improvements**
	1.	Expand Data Sources: Incorporate additional datasets, such as traffic density or road conditions, to improve model robustness.
	2.	Experiment with Advanced Models: Explore gradient boosting techniques such as XGBoost or LightGBM for further performance gains.
	3.	Leverage Temporal Models: Use time-series models like LSTMs to capture temporal dependencies in crash occurrences.
	4.	Refine Feature Engineering: Investigate additional derived features to enhance predictive accuracy.


