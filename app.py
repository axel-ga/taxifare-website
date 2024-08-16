import streamlit as st
import requests
import datetime
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
pickup_datetime = st.date_input("pickup date", value="default_value_today")
pickup_longitude = st.number_input("Insert a pickup lon", value=None, placeholder="Type a number..."
pickup_latitude = st.number_input("Insert a pickup lat", value=None, placeholder="Type a number..."
dropoff_longitude = st.number_input("Insert a dropoff lon", value=None, placeholder="Type a number..."
dropoff_latitude = st.number_input("Insert a droppoff lat", value=None, placeholder="Type a number..."
passenger_count = st.number_input('passenger count', min_value=None, max_value=None)

2. Let's build a dictionary containing the parameters for our API...
payload = {
    'pickup_datetime':pickup_datetime,
    'pickup_longitude':pickup_longitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':passenger_count
    }

3. Let's call our API using the `requests` package...

response = requests.get(url,params=payload).json()
print(response.status_code)
st.write(response, unsafe_allow_html=False)

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
url = 'https://taxifare.lewagon.ai/predict'

pickup_datetime = st.date_input("pickup date", value="default_value_today")
mytime = st.time_input("pickup time", value="now")
pickup_longitude = st.number_input("Insert a pickup lon", value=None, placeholder="Type a number...")
pickup_latitude = st.number_input("Insert a pickup lat", value=None, placeholder="Type a number...")
dropoff_longitude = st.number_input("Insert a dropoff lon", value=None, placeholder="Type a number...")
dropoff_latitude = st.number_input("Insert a droppoff lat", value=None, placeholder="Type a number...")
passenger_count = st.number_input('passenger count', min_value=None, max_value=None,step=1)

payload = {
    'pickup_datetime':str(pickup_datetime)+" "+str(mytime),
    'pickup_longitude':pickup_longitude,
    'pickup_latitude':pickup_latitude,
    'dropoff_longitude':dropoff_longitude,
    'dropoff_latitude':dropoff_latitude,
    'passenger_count':int(passenger_count)
    }

response = requests.get(url,params=payload).json()
st.write(response, unsafe_allow_html=False)
