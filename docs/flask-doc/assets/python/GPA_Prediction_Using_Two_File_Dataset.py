
# coding: utf-8

# <center> <h1> Machine Learning </h1> </center>
# <center> <h1> GPA Prediction using Scikit-Learn </h1> </center>
# <center> <h1> (A Step by Step Tutorial)</h1> </center>
# <br><br><br>
# <center> <h1> Instructor: Dr. Rao Muhammad Adeel Nawab </h1></center>

# ## Table of contents
# 
# ### 1. [Introduction](#intro)
# ### 2. [3 Phases of Machine Learning](#phase)
#    **2.1  [Training](#training)   
#      3.2  [Testing/Validation](#testing)   
#      3.3  [Application Phase](#app)**
# 
# ### 4. [Implementation step by step:]
# **4.1 [Step 1. Import Libraries](#lib)  
#   4.2 [Step 2. Read & Understand Dataset](#read)  
#   4.3 [Step 3. Data Preprocessing](#data_preprocess)  
#   4.4 [Step 4. Label Encoding](#le_encoding)  
#   4.5 [Step 5. Split Input vectors and labels](#split)  
#   4.6 [Step 6. Model Preparation](#model)  
#   4.7 [Step 7. Training Models](#training_model)  
#   4.8 [Step 8. Find Best Model](#best_trained_model)  
#   4.9 [Step 9. Saving the model - Dump file](#save_model)  
#   4.10[Step 10. Loading the model - Load File](#load_saved_model)  
#   4.11[Step 11. Getting User Input](#getting_user_input)  
#   4.12[Step 12. Prediction](#predict)**

# <a id="intro"></a>
# ## 1. Introduction
# The main aim of this tutorial is to explain the task of gpa prediction using scikit-learn Machine Learning toolkit.In this tutorial, we are provided with SAT Scores. The task is to predict GPA based on SAT Score using Machine Learning algorithms. <br><br>
# In this tutorial, the problem of GPA Prediction is treated as a supervised learning problem. The Input and Output are:<br><br>
# 
# <b>Input:</b> SAT Score(Numeric)<br><br>
# <b>Output:</b> GPA (Decimal Values/ Float Values)<br><br>
# <b>Goal:</b> Learn from Input to predict Output<br><br>
#     
# <h3> Three Phases of Machine Learning: </h3><br><br>
# <b>1. Training </b>– Learn from training data.<br><br>
# <b>2. Testing/Validation/Evaluation</b> – evaluate how good you have learning.<br><br>
# <b>3. Application </b>– Use your learned/trained models in real world applications.<br><br>
# [[ go back to the top ]](#Table-of-contents)

#  ## 2. Three Phases of Machine Learning:
#  <a id="#phase"></a> 
# <b>1. Training </b>– Learn from training data.<br><br>
# <b>2. Testing/Validation/Evaluation</b> – evaluate how good you have learning.<br><br>
# <b>3. Application </b>– Use your learned/trained models in real world applications.<br><br>
# [[ go back to the top ]](#Table-of-contents)

# <a id="#training"></a>
# <a id="#testing"></a>
# <h3>PHASE 1 & 2: TRAINING AND TESTING </h3>
# 
# **Step 1:** Import Libraries<br><br>
# **Step 2:** Read, Understand and Pre-process Train/Test Data<br><br>
# **Step 2.1:** Read Data<br><br>
# **Step 2.2:** Understand Data<br><br>
# **Step 2.3:** Pre-process Data<br><br>
# **Step 3:** Label Encoding for Train/Test Data<br><br>
# **Step 4:** Feature Extraction – Changing Representation of Data “from String to Vector”<br><br>
# **Step 5:** Train Machine Learning Algorithms using Training Data<br><br>
# **Step 6:** Evaluate Machine Learning Algorithms using Test Data<br><br>
# **Step 7:** Selection of Best Model<br><br><br><br>
# [[ go back to the top ]](#Table-of-contents)
# <a id="#app"></a>
# <h3> PHASE 3: APPLICATION PHASE</h3><br>
# **Step 8:** Application Phase<br><br>
# **Step 8.1:** Combine Data (Train + Test )¶<br><br>
# **Step 8.2:** Train Best Model (see Step 7) on all data(Train+Test)<br><br>
# **Step 8.3:** Save the Trained Model as Pickle File<br><br>
# **Step 9:** Make prediction on unseen/new data<br><br>
# **Step 9.1:** Load the Trained Model (saved in Step 8.3)<br><br>
# **Step 9.2:** Take Input from User<br><br>
# **Step 9.3:** Convert User Input into Feature Vector (Same as Feature Vector of Trained Model)<br><br>
# **Step 9.4:** Apply Trained Model on Feature Vector of Unseen Data and Output Prediction (Male/Female) to User<br><br>
# [[ go back to the top ]](#Table-of-contents)

# <a id="lib"></a>
# # Step 1: Import Libraries

# In[57]:


import re
import string
import scipy
import pickle
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import *
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.svm import LinearSVR
from sklearn.metrics import mean_absolute_error
#from prettytable import PrettyTable
from astropy.table import Table, Column

def prediction(sat_input):
# <a id="read"></a>
# # Step 2: Read, Understand & Pre-process Train/Test Data
# ### Step 2.1: Read Data

# In[58]:


	train_file = 'train.csv'
	test_file = 'test.csv'
	#Read train dataset
	train_dataset = pd.read_csv(train_file)
	#Read test dataset
	test_dataset = pd.read_csv(test_file)
	
	
	# ### Step 2.2: Understand Data
	
	# <h4>Understand Train Dataset</h4>
	
	# In[59]:
	
	
	print("Train Dataset:\n")
	train_dataset.index.names = ['index']
	train_dataset.columns.name = train_dataset.index.name
	train_dataset.index.name = None
	print(train_dataset)
	
	print("\n\n\nNumber of instances in Train Dataset:\n")
	print("Train instances: ",train_dataset.shape[0])
	
	print("\n\n\nTrain Dataset Columns:\n")
	print(train_dataset.columns)
	
	
	# <h4>Input Attribute of Train Dataset</h4>
	
	# In[60]:
	
	
	x_train = train_dataset.drop("GPA" , axis=1)
	x_train
	
	
	# <h4>Output Attribute of Train Dataset</h4>
	
	# In[61]:
	
	
	y_train = train_dataset.drop("SAT_Score" , axis=1)
	y_train
	
	
	# <h3>Understand Test Dataset</h3>
	
	# In[62]:
	
	
	print("Test Dataset:\n")
	test_dataset.index.names = ['index']
	test_dataset.columns.name = test_dataset.index.name
	test_dataset.index.name = None
	print(test_dataset)
	
	
	print("\n\n\nNumber of instances in Test Dataset:\n")
	print("Test instances: ",test_dataset.shape[0])
	
	print("\n\n\nTest Dataset Columns:\n")
	print(test_dataset.columns)
	
	
	# <h4>Input Attribute of Test Dataset</h4>
	
	# In[63]:
	
	
	x_test = test_dataset.drop("GPA" , axis=1)
	x_test
	
	
	# <h4>Output Attribute of Test Dataset</h4>
	
	# In[64]:
	
	
	y_test = test_dataset.drop("SAT_Score" , axis=1)
	y_test
	
	
	# <h3>Train Data Visualization</h3>
	
	# In[66]:
	
	
	objects = train_dataset.SAT_Score
	y_pos = np.arange(len(objects))
	performance = train_dataset.GPA
	
	# plt.bar(y_pos, performance, align='center', alpha=0.2)
	# plt.xticks(y_pos, objects)
	# plt.ylabel('GPA')
	# plt.xlabel('SAT Scores')
	# plt.title('SAT Scores with respective GPAs in Train Data')
	 
	# plt.show()
	
	
	# In[67]:
	
	
	# train_dataset.SAT_Score.plot(kind='bar',stacked=True, colormap='plasma')
	
	
	# In[24]:
	
	
	# train_dataset.GPA.plot(kind='bar',stacked=True, colormap='RdGy_r')
	
	
	# <h4>Test Data Visualization</h4>
	
	# In[69]:
	
	
	objects = test_dataset.SAT_Score
	y_pos = np.arange(len(objects))
	performance = test_dataset.GPA
	
	# plt.bar(y_pos, performance, align='center', alpha=0.8)
	# plt.xticks(y_pos, objects)
	# plt.ylabel('GPA')
	# plt.xlabel('SAT Scores')
	# plt.title('SAT Scores with respective GPAs in Test Data')
	 
	# plt.show()
	
	
	# In[70]:
	
	
	# test_dataset.SAT_Score.plot(kind='bar',stacked=True, colormap='RdGy')
	
	
	# In[72]:
	
	
	# test_dataset.GPA.plot(kind='bar',stacked=True, colormap='plasma_r')
	
	
	# <a id="#data_preprocess"></a>
	# ### Step 2.3: Pre-Precess Data
	
	# In[73]:
	
	
	print("Train dataset before pre-processing:\n")
	print(train_dataset)
	
	train_dataset = train_dataset.fillna(' ')
	
	
	print("\n\n\nTrain dataset after pre-processing:\n")
	print(train_dataset)
	
	
	# <a id="#le_encoding"></a>
	# # Step 3: Label Encoding for Test/Train Data
	
	# We haven't categorical data in our given dataset. So, LabelEncoding will not be applied/used in this scenario.
	
	# <a id="#split"></a>
	# # Step 4: Feature Extraction – Changing Representation of Data “from String to Vector”
	
	# The dataset is already in "Vector Form". So, there is no need to use CountVectorizer, TfidfVectorizer, DictVectorizer or any other.
	
	# <a id="#model"></a>
	# # Step 5: Train Machine Learning Algorithms using Training Data
	
	# ###### Random Forest Regressor
	
	# In[74]:
	
	
	model_names=[]
	
	#Random Forest Regressor
	random_forest_regressor = RandomForestRegressor()
	
	print("Parameters and their values:\n")
	print(random_forest_regressor)
	
	random_forest_regressor.fit(x_train,y_train)
	
	model_names.append('RandomForestRegressor')
	
	
	# ###### LinearSVR
	
	# In[75]:
	
	
	#linear SVC
	linear_svr = LinearSVR()
	
	print("Parameters and their values:\n")
	print(linear_svr)
	
	linear_svr.fit(x_train,y_train)
	
	model_names.append('LinearSVR')
	
	
	# ##### GradientBoostingRegressor
	
	# In[76]:
	
	
	#Gradient Boosting Regressor
	gradient_boosting_regressor = GradientBoostingRegressor()
	
	print("Parameters and their values:\n")
	print(gradient_boosting_regressor)
	
	gradient_boosting_regressor.fit(x_train,y_train)
	
	model_names.append('GradientBoostingRegressor')
	
	
	# <a id="#training_model"></a>
	# # Step 6: Evaluate Machine Learning Algorithms using Test Data
	
	# In[77]:
	
	
	x_test
	
	
	# In[78]:
	
	
	scores=[]
	
	actual = y_test
	predicted = random_forest_regressor.predict(x_test)
	
	for i in range(0,5):
	    predicted[i] = round(predicted[i],2)
	
	score = round(mean_absolute_error(actual, predicted),2)
	
	
	print("Prediction using Random Forest Regressor:\n")
	print(test_dataset.assign(predicted_GPA = predicted))
	
	print("\n\nMean Absolute Error = ", score)
	scores.append(score)
	
	
	# In[79]:
	
	
	predicted
	
	
	# In[80]:
	
	
	actual = y_test
	
	predicted = linear_svr.predict(x_test)
	
	for i in range(0,5):
	    predicted[i] = round(predicted[i],2)
	    
	    
	score = round(mean_absolute_error(actual, predicted),2)
	
	print("Prediction using Linear SVR:\n")
	print(test_dataset.assign(predicted_GPA = predicted))
	
	print("\n\nMean Absolute Error = ", score)
	scores.append(score)
	
	
	# In[81]:
	
	
	actual = y_test
	
	predicted = gradient_boosting_regressor.predict(x_test)
	
	for i in range(0,5):
	    predicted[i] = round(predicted[i],2)
	    
	    
	score = round(mean_absolute_error(actual, predicted),2)
	
	print("Prediction using Gradient Boosting Regressor:\n")
	print(test_dataset.assign(predicted_GPA = predicted))
	
	print("\n\nMean Absolute Error = ", score)
	scores.append(score)
	
	
	# <a id="#best_trained_model"></a>
	# # Step 7: Selection of Best Model
	
	# In[100]:
	
	
	# print('\n\nDetailed Performance of all the models.')
	# print("=======================================")
	# t = PrettyTable(['Model', 'Mean Absolute Error'])
	# minimum = 100 
	
	# for i in range(0, 3):
	    
	#     model = model_names[i]
	#     score = scores[i]
	    
	#     if(minimum > score):
	#         minimum = score
	#         index = i
	#     t.add_row([model,score])
	    
	# print(t)
	
	
	
	# print('\n\nBest Model.')
	# print("=======================================")
	# t = PrettyTable(['Model', 'Mean Absolute Error'])
	# t.add_row([model_names[index], scores[index]])
	# print(t)
	
	
	# # PHASE 3: APPLICATION PHASE
	# 
	# # Step 8: Application Phase
	# ### Step 8.1: Combine Data (Train+Test)
	# (Combine Features and Labels (Train features + Test Features and Train encoded labels+ Test encoded labels))
	
	# In[83]:
	
	
	train = train_dataset
	train
	
	
	# In[84]:
	
	
	test = test_dataset
	test
	
	
	# In[85]:
	
	
	print("All features in the form of DataFrame: ")
	all_data = pd.concat([train, test])
	all_data
	
	
	# In[86]:
	
	
	print("Input Attribute of Combined/All Data")
	data_input = all_data.drop("GPA" , axis=1)
	data_input
	
	
	# In[87]:
	
	
	print("Output Attribute of Combined/All Data")
	data_output = all_data.drop("SAT_Score" , axis=1)
	data_output
	
	
	# In[88]:
	
	
	print(data_input.shape)
	print(data_output.shape)
	
	
	# ### Step 8.2: Train Best Model (see Step 7) on all features (Train+Test)
	
	# In[89]:
	
	
	random_forest_regressor.fit(data_input,data_output)
	
	
	# <a id="#save_model"></a>
	# ### Step 8.3: Save the trained model as Pickle file 
	
	# In[90]:
	
	
	pickle.dump(random_forest_regressor, open('RandomForestRegressor.pkl', 'wb'))
	
	
	# [[ go back to the top ]](#Table-of-contents)
	
	# # Step 9: Make prediction on unseen/new data
	
	# <a id="#load_saved_model"></a>
	# ### Step 9.1: Load the Trained Model (saved in Step 8.3) 
	
	# In[91]:
	
	
	regressor = pickle.load(open('RandomForestRegressor.pkl', 'rb'))
	
	
	# <a id="#getting_user_input"></a>
	# ### Step 9.2: Take Input from User
	
	# In[93]:
	
	
	user_input = sat_input
	
	
	# ### Step 9.3: Convert User Input into Feature Vector (Same as Feature Vector of Trained Model) 
	
	# User input is already in Matrix Form.
	
	# <a id="#predict"></a>
	# ### Step 9.4: Apply Trained Model on Feature Vector of Unseen Data and Output Prediction (Male/Female) to User
	
	# In[94]:
	
	
	type(user_input)
	
	
	# In[95]:
	
	
	user_input = pd.DataFrame([user_input])
	
	
	# In[96]:
	
	
	print("\n\nPrediction: ", end='')
	pred = regressor.predict(user_input)
	print(pred)

	return pred


# [[ go back to the top ]](#Table-of-contents)
