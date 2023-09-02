import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open("titanic_trained_model.sav",'rb'))



# creating a function

def Survived_predection(input_data):
    
    #channging the input data in numpy array
    input_data_as_numpy_arr=np.asarray(input_data)
    input_int_datatype=input_data_as_numpy_arr.astype(float)
# reshape the array as we are predicting for one instance
    input_data_reshaped=input_int_datatype.reshape(1,-1)



    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
        return "The person will die"       
    
    else:
        return "The person will not die"  
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


def main():   
          
        
    # giving title 
    st.title('Titanic Prediction')   
    
    # this statement is used to make gap between 2 given lines
    st.markdown("") 
    
           
    # getting the input data from the users
    
    my_expander = st.expander(label='Note')
    with my_expander:
        'pclass - Ticket class'
        'sibsp - No of siblings / spouses aboard the Titanic'
        'parch - No of parents / children aboard the Titanic'
        
        
     # this statement is used to make gap between 2 given lines        
    st.markdown("")       
         
    
    col1, col2, col3 = st.columns(3)
    
    
    
    with col1:
        Pclass  = st.selectbox("Pclass ",
                     ['1', '2', '3'])
        
    with col2:
        Sex = st.text_input('Sex Put 0 for male 1 for female')
    
    with col3:
        Age = st.text_input('Age')
    
    with col1:
        SibSp=st.text_input('SibSp')
    
    with col2:
         Parch=st.text_input('Parch')
    
    with col3:
        Fare=st.text_input('Fare')
    
    with col1:
        Embarked = st.radio(
    "From Which Station You Board",
    ('0', '1', '2'))

        if Embarked == '0':
            st.write('You selected Southampton.')
        elif Embarked=='1':
            st.write("You selected Cherbourg.")
        else:
            st.write('You selected Queenstown')     
            
    
    
    #code for Prediction
    
    Survived=""
    
    # creating button for prediction
    
    if st.button('Survived Test Result'):
        Survived=Survived_predection([Pclass,Sex,Age,SibSp,Parch,Fare,Embarked])
        
    
    
    st.success(Survived) 
    
    
    
main()
    
    
    
    