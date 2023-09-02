import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open("titanic_trained_model.sav",'rb'))


input_data=(3,0,22.000000,1,0,7.2500,0)

#channging the input data in numpy array
input_data_as_numpy_arr=np.asarray(input_data)
input_int_datatype=input_data_as_numpy_arr.astype(float)

# reshape the array as we are predicting for one instance
input_data_reshaped=input_int_datatype.reshape(1,-1)



prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0]==0):
    print("The person will die")
else:
    print("The person will not die")  