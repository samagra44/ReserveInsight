import streamlit as st
import pickle as pk
import numpy as np

with open('saved_model.pkl','rb') as file:
    dtree = pk.load(file)

st.set_page_config(
    page_title="Hotel Reservation/Cancellation Prediction",
    page_icon="bar-chart",
    layout='wide'
)
st.sidebar.title("Hotel Reservation/Cancellation Prediction 🏨")
st.sidebar.title("Enter the details")
type_meal_plan_options = {'Meal Plan 1':0, 
                          'Not Selected':3,
                          'Meal Plan 2':1,
                          'Meal Plan 3':2}
type_meal_plan = st.sidebar.selectbox('Meal Plan:',list(type_meal_plan_options.keys()), index=0)

room_type_reserved_options = {'Room_Type 1':0,
                              'Room_Type 4':3,
                              'Room_Type 6':5,
                              'Room_Type 2':4,
                              'Room_Type 5':1,
                              'Room_Type 7':6,
                              'Room_Type 3':2}
room_type_reserved = st.sidebar.selectbox('Room Type Reserved:',list(room_type_reserved_options.keys()), index=0)

market_segment_type_options = {'Online':3,
                               'Offline':4,
                               'Corporate':2,
                               'Complementary':0,
                               'Aviation':1}
market_segment_type = st.sidebar.selectbox('Market Segment Type:',list(market_segment_type_options.keys()),index=0)

no_of_adults = st.sidebar.slider('Number of Adults:', min_value=1, max_value=10, value=1)
no_of_children = st.sidebar.slider('Number of Children:',min_value=0,max_value=5,value=0)
no_of_weekend_nights = st.sidebar.slider('Number of Weekend Nights:',min_value=0,max_value=10,value=1)
no_of_week_nights = st.sidebar.slider('Number of Week Nights:',min_value=0,max_value=10,value=1)
required_car_parking_space = st.sidebar.slider('Required Car Parking Space:',min_value=0,max_value=7,value=1)
repeated_guest = st.sidebar.slider('Repeated Guest:',min_value=0,max_value=10,value=1)
no_of_previous_cancellations = st.sidebar.slider('Number of Previous Cancellations:',min_value=0,max_value=15,value=0)
no_of_previous_bookings_not_canceled = st.sidebar.slider('Number of Previous Bookings Not Canceled:',min_value=0,max_value=10,value=0)
no_of_special_requests = st.sidebar.slider('Number of Special Requests:',min_value=0,max_value=100,value=1)
avg_price_per_room = st.sidebar.number_input("Insert a number:", value=5.0)
lead_time = st.sidebar.number_input("Insert a number:", value=1.0)


# Button
submit_button = st.sidebar.button('Submit')
st.title("Model Prediction Result 💁")
def make_prediction():
    input_data = {
        'type_meal_plan':type_meal_plan_options[type_meal_plan],
        'room_type_reserved':room_type_reserved_options[room_type_reserved],
        'market_segment_type':market_segment_type_options[market_segment_type],
        'no_of_adults':no_of_adults,
        'no_of_children':no_of_children,
        'no_of_weekend_nights':no_of_weekend_nights,
        'no_of_week_nights':no_of_week_nights,
        'required_car_parking_space':required_car_parking_space,
        'lead_time':lead_time,
        'repeated_guest':repeated_guest,
        'no_of_previous_cancellations':no_of_previous_cancellations,
        'no_of_previous_bookings_not_canceled':no_of_previous_bookings_not_canceled,
        'avg_price_per_room':avg_price_per_room,
        'no_of_special_requests':no_of_special_requests
    }

    input_array = [[input_data['type_meal_plan'], 
                    input_data['room_type_reserved'],
                    input_data['market_segment_type'],
                    input_data['no_of_adults'],
                    input_data['no_of_children'],
                    input_data['no_of_weekend_nights'],
                    input_data['no_of_week_nights'],
                    input_data['required_car_parking_space'],
                    input_data['lead_time'],
                    input_data['repeated_guest'],
                    input_data['no_of_previous_cancellations'],
                    input_data['no_of_previous_bookings_not_canceled'],
                    input_data['avg_price_per_room'],
                    input_data['no_of_special_requests']]]
    
    prediction = dtree.predict(input_array)
    st.write('Model Prediction 🤖: ',prediction[0])

    if prediction[0] == 0:
        st.write("Hotel Reservation will be Cancelled ❌🙆")
    else:
        st.write("Hotel Reservation will not be Cancelled ✅👌")

if submit_button:
    make_prediction()
