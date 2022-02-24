#!/usr/bin/env python
# coding: utf-8

# In[1]:


from logging import debug
from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('SVM_SVC_model.pickle','rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.htm')   

@app.route('/predict',methods =['POST'])
def telecom_churn():
    
    gender = request.form.get('gender')
    if gender=="male":
        gender=0
    else:
        gender=1
    SeniorCitizen = request.form.get('SeniorCitizen')
    if SeniorCitizen=="Yes":
        SeniorCitizen=1
    else:
        SeniorCitizen=0
        
    Partner = request.form.get('Partner')
    if Partner=="Yes":
        Partner=1
    else:
        Partner=0
        
    Dependents = request.form.get('Dependents')
    if Dependents=="Yes":
        Dependents=1
    else:
        Dependents=0
    
    tenure = int(request.form.get('tenure'))
    
    PhoneService = request.form.get('PhoneService')
    if PhoneService=="Yes":
        PhoneService=1
    else:
        PhoneService=0
        
    MultipleLines = request.form.get('MultipleLines')
    if MultipleLines=="Yes":
        MultipleLines = 1
    elif MultipleLines == "No":
        MultipleLines=0
    else:
        MultipleLines=2
    
    InternetService = request.form.get('InternetService')
    if InternetService=='Fiber optic':
        InternetService = 1
    elif InternetService == "'DSL'":
        InternetService=0
    else:
        InternetService=2
        
    OnlineSecurity = request.form.get('OnlineSecurity')
    if OnlineSecurity=='No':
        OnlineSecurity=0
    elif OnlineSecurity=='Yes':
        OnlineSecurity=2
    else:
        OnlineSecurity=1
        
    OnlineBackup = request.form.get('OnlineBackup')
    if OnlineBackup=='No':
        OnlineBackup=0
    elif OnlineBackup=='Yes':
        OnlineBackup=2
    else:
        OnlineBackup=1
        
    OnlineSecurity = request.form.get('OnlineSecurity')
    if OnlineSecurity=='No':
        OnlineSecurity=0
    elif OnlineSecurity=='Yes':
        OnlineSecurity=2
    else:
        OnlineSecurity=1
        
    DeviceProtection = request.form.get('DeviceProtection')
    if DeviceProtection=='No':
        DeviceProtection=0
    elif DeviceProtection=='Yes':
        DeviceProtection=2
    else:
        DeviceProtection=1
        
    TechSupport = request.form.get('TechSupport')
    if TechSupport=='No':
        TechSupport=0
    elif TechSupport=='Yes':
         TechSupport=2
    else:
        TechSupport=1
    StreamingTV = request.form.get('StreamingTV')
    if StreamingTV=='No':
        StreamingTV=0
    elif StreamingTV=='Yes':
         StreamingTV=2
    else:
        StreamingTV=1
    StreamingMovies = request.form.get('StreamingMovies')
    if StreamingMovies=='No':
        StreamingMovies=0
    elif StreamingMovies=='Yes':
         StreamingMovies=2
    else:
        StreamingMovies=1
        
    Contract = request.form.get('Contract')
    if Contract=='Month-to-month':
        Contract=0
    elif Contract=='One year':
         Contract=1
    else:
        Contract=2
    
    PaperlessBilling = request.form.get('PaperlessBilling')
    if PaperlessBilling=='Yes':
        PaperlessBilling=1
    else:
        PaperlessBilling=0
    
    PaymentMethod = request.form.get('PaymentMethod')
    if  PaymentMethod=="Bank transfer (automatic)":
         PaymentMethod =0
    elif  PaymentMethod=="Credit card (automatic)":
         PaymentMethod =1
    elif  PaymentMethod=="Electronic check":
         PaymentMethod =2
    else:
        PaymentMethod =3
   
    MonthlyCharges = float(request.form.get('monthlycharges'))
    TotalCharges = float(request.form.get('result'))
    
    result = model.predict(np.array([gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,
                                    MultipleLines,InternetService,OnlineSecurity,OnlineBackup,
                                    DeviceProtection,TechSupport,StreamingTV,StreamingMovies,
                                    Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]).reshape(1,19))
            
    if result[0] == 1:
        result = "Customer will Retain"
    else:
        result ="Customer will Not Retain"

           


    return render_template('index.htm',prediction = result)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=False)

