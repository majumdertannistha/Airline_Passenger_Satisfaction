import numpy as np
import pickle
import streamlit as st
import xgboost

## loading the saved model
loaded_model = pickle.load(open('C:/PROJECT/Pg project/trained_model.sav','rb'))

## creating a function

def airline_satisfaction(input_data) :
    # changing input data into numpy array
    input_data_as_numpy_Array = np.array(input_data,dtype=object)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_Array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return 'The person is not satisfied'
    else:
        return 'The Person is satisfied'

def main() :

    ## giving a title
    st.title('Airline Passanger Satisfaction Prediction Application')
    ## getting the input data from user
    st.text("**Please give these answer in numerical values**")
    try :
        Age = st.text_input('Enter your age')
        FlightDistance = st.text_input('Enter flight distance of this journey')
        DepartureDelay = st.text_input('How much time flight delayed in minutes when it departs?')
        st.text("**Please give these answer with 0-5 number. Note that: Here 0 indicates strongly dis-satisfied and 5 indicates fully satisfied**")
        DepartureandArrivalTimeConvenience = st.selectbox('How much you satisfied with departure/arrival time conveniency in flight?',(0,1,2,3,4,5))
        CheckinService = st.selectbox("How much you satisfied with check in service in flight?",(0,1,2,3,4,5))
        OnlineBoarding = st.selectbox('How much you satisfied with online boarding service in flight?',(0,1,2,3,4,5))
        GateLocation = st.selectbox('How much you satisfied with gate location in flight?',(0,1,2,3,4,5))
        OnboardService = st.selectbox('How much you satisfied with boarding service in flight?',(0,1,2,3,4,5))
        SeatComfort = st.selectbox('How much you satisfied with your seat in flight?',(0,1,2,3,4,5))
        LegRoomService = st.selectbox('How much you satisfied with leg room service in flight?',(0,1,2,3,4,5))
        Cleanliness = st.selectbox('How much you satisfied with cleanliness in flight?',(0,1,2,3,4,5))
        FoodandDrink = st.selectbox('How much you satisfied with food and drink service in flight?',(0,1,2,3,4,5))
        InflightService = st.selectbox('How much you satisfied with wifi service in flight',(0,1,2,3,4,5))
        InflightWifiService = st.selectbox('How much you satisfied with wifi service in flight?',(0,1,2,3,4,5))
        InflightEntertainment = st.selectbox('How much you satisfied with entertainment in flight?',(0,1,2,3,4,5))
        BaggageHandling = st.selectbox('How much you satisfied with baggage handling?',(0,1,2,3,4,5))
        st.text('**Please give these answer with either 0 or 1 . Note that, here 0 indicates no and 1 indicates yes**')
        Gender_Male = st.selectbox('Are you male?',(0,1))
        CustomerType_Returning = st.selectbox('Are you returning in flight?',(0,1))
        TypeofTravel_Personal = st.selectbox('Are you travelling in flight for your personal purpose?',(0,1))
        Class_Economy = st.selectbox('Are you belongs to economy class?',(0,1))
        Class_EconomyPlus = st.selectbox('Are you belongs to economy plus class?',(0,1))


        ## code for prediction
        satisfaction = ''
        ## creating a button for prediction
        if st.button('PREDICT') :
            st.text("Airline passenger satisfaction prediction result")
            satisfaction = airline_satisfaction([Age,FlightDistance,DepartureDelay,DepartureandArrivalTimeConvenience,CheckinService,OnlineBoarding,GateLocation,OnboardService,SeatComfort,LegRoomService,Cleanliness,FoodandDrink,InflightService,InflightWifiService,InflightEntertainment,BaggageHandling,Gender_Male,CustomerType_Returning,TypeofTravel_Personal,Class_Economy,Class_EconomyPlus])
            st.success(satisfaction)
    except Exception as e:
        st.text(e)



if __name__ == '__main__' :
    main()


