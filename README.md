# disease-prediction-ML

This is a disease prediction web application. In which we use disease dataset,symptom-severity dataset,disease_description,disease_precaution datasets for developing machine learning model later on it can be used in our web application

- Disease Dataset --> This dataset contains symptoms as well as disease name in a dataframe 
- Symptom-severity --> This dataset contains the weights of each symptom. so by this dataset we can assign weights for disease dataset, because the disease dataset is in charcater format. we are using this to avoid "one-hot encoding".
- Disease_description --> This dataset contains the description of each disease. so that we can display the description of disease in our follow up page in our application.
- Disease_precaution --> This is similar to previous dataset and will be displayed in follow up page.

## Front-end:
In home page, we will have 6 drop down options to enter symptoms and then we will have a predict option to run our Ml model in backend and predict the disease,after clicking predict you will be redirected to next page displaying disease name and they will be separate option to check disease_desc as well as disease_precaution, which will redirect to new page.
For working of frontend, i have used HTML,CSS,JS.

## Backend:
For working of backend, i had used Django python framework.

Intially we will create models for predict,desc and precautions options.

after that we can setup our csv files/ datasets to database, so that we can access them at the time of operating.

In django views, we will first import models which are already written, then create 3 function

predict function ---> to read data from database and create machine learning model using random forest model after all the pre-processing steps are done like cleaning,encoding with symptom-severity and finally the base ML model is completed.

Predd function ---> we use this function to extract data from user request and adapt this data to our predict function, which gives disease name as output in "predict.html" page.

desc_prec function ---> after getting the disease name we can use this info and find the disease descrption and disease precautions, we can get this data from datasets in database. this function returns disease descrption and disease precautions in "dwsc.html".


This is the Complete description about my disease_prediction web application.



