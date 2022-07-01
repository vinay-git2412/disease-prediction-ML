from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import pickle
# Create your views here.
def home(request):
    return render(request, 'index.html')

def predict(request):
    
    # Reading disease dataset
    disease_df = pd.read_csv(r"E:\Disease_detection\dataset.csv")
    disease_df = shuffle(disease_df,random_state=42)  # shuffling the dataset to see all values randomly
    # removing ('_') underscore in the text to maintain equality
    for col in disease_df.columns:
        disease_df[col] = disease_df[col].str.replace('_', ' ')
    # Flattening the values to avoid spaces
    cols = disease_df.columns
    data = disease_df[cols].values.flatten()
    reshaped = pd.Series(data)
    reshaped = reshaped.str.strip()
    reshaped = reshaped.values.reshape(disease_df.shape)
    disease_df = pd.DataFrame(reshaped, columns = disease_df.columns)
    # Replacing the Nan values with 0    
    disease_df = disease_df.fillna(0)
    # Reading symptom weights dataset
    severity_df = pd.read_csv(r"E:\Disease_detection\Symptom-severity.csv")
    # removing ('_') underscore in the text to maintain equality
    severity_df['Symptom'] = severity_df['Symptom'].str.replace('_',' ')
    # labeling the weights according to severity dataset
    vals = disease_df.values
    symptoms = severity_df['Symptom'].unique()
    for i in range(len(symptoms)):
        vals[vals == symptoms[i]] = severity_df[severity_df['Symptom'] == symptoms[i]]['weight'].values[0]   
    final_df = pd.DataFrame(vals, columns=cols)
    # labeling these 3 symptoms as 0 as their weights are not present in dataset
    final_df = final_df.replace('dischromic  patches', 0)
    final_df = final_df.replace('spotting  urination',0)
    final_df = final_df.replace('foul smell of urine',0)
    # Separating the dependent and independent variables for train test split
    X = final_df.drop('Disease', axis = 1).values
    y = final_df['Disease'].values
    # Train test split
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=42)
    # Model
    # RandomForestClassification
    from sklearn.ensemble import RandomForestClassifier
    rand_clas = RandomForestClassifier()
    rand_clas.fit(X_train,y_train) # fitting the model
    
    print(rand_clas.score(X_test,y_test)*100)
    
    
    def predd(S1,S2,S3,S4,S5,S6,S7 = 0,S8 = 0,S9 = 0,S10 = 0,S11 = 0,S12 = 0,S13 = 0,S14 = 0,S15 = 0,S16 = 0,S17 = 0):
        psymptoms = [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12,S13,S14,S15,S16,S17]
        for i in range(0,len(psymptoms)):
            if psymptoms[i] == '':
                psymptoms.pop(i)
                psymptoms.insert(i,0)
        print(psymptoms)
        a = np.array(severity_df["Symptom"])
        b = np.array(severity_df["weight"])
        for j in range(len(psymptoms)):
            for k in range(len(a)):
                if psymptoms[j]==a[k]:
                    psymptoms[j]=b[k]

        psy = [psymptoms]
        pred2 = rand_clas.predict(psy)
        
        return pred2[0]
    
    if request.method == 'POST':
        
        S1 = request.POST.get('Symptom1', False)
        S2 = request.POST.get('Symptom2', False)
        S3 = request.POST.get('Symptom3', False)
        S4 = request.POST.get('Symptom4', False)
        S5 = request.POST.get('Symptom5', False)
        S6 = request.POST.get('Symptom6', False)
    else:
        return render(request, 'index.html')    
    classification = predd(S1,S2,S3,S4,S5,S6)
    
    # creating a global function to return classification value
    global val
    def val():
        return classification
    
    return render(request, 'predict.html', {'classification_result': classification})
    

from .models import DesandPrec
 
def desc_prec(request):
       
    des_df = pd.read_csv(r"E:\Disease_detection\symptom_Description.csv")
    pec_df = pd.read_csv(r"E:\Disease_detection\symptom_precaution.csv")
    
    for i in range(len(des_df["Disease"])):
        if des_df["Disease"][i] == 'Diabetes':
            des_df["Disease"][i] = 'Diabetes '
        elif des_df["Disease"][i] == 'Hypertension':
            des_df["Disease"][i] = 'Hypertension '
        elif des_df["Disease"][i] == 'Dimorphic hemorrhoids(piles)':
            des_df["Disease"][i] = 'Dimorphic hemmorhoids(piles)'   
    
    com_df = des_df.merge(pec_df, how='right')
    
    disease = val()  #classification
    
    sep_df = com_df[com_df['Disease'] == disease]
    ind = com_df[com_df['Disease']==disease].index.values
    ind = ind[0]
    
    descpre = DesandPrec()
    
    descpre.Description = sep_df['Description'][ind]
    descpre.Precaution_1 = sep_df['Precaution_1'][ind]
    descpre.Precaution_2 = sep_df['Precaution_2'][ind]
    descpre.Precaution_3 = sep_df['Precaution_3'][ind]
    descpre.Precaution_4 = sep_df['Precaution_4'][ind]     
    descpre.classification = disease
    return render(request,'desc.html',{'descpre':descpre})    #{{descpre.Description}} use like this while mentioning in html