import streamlit as st
import requests
from datetime import datetime

API_KEY ="YOUR_API_KEY"

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌦️",
    layout="centered"
)

st.title("🌦️ Weather Dashboard")

st.write("Get real-time weather information for any city.")

city = st.text_input("Enter City Name")

search = st.button("Get Weather")

if search:
    
    if city == "":
        st.warning("Please enter a city name.")
    else:
    

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    with st.spinner("Fetching weather data..."):

        response = requests.get(url)
        data = response.json()

    if data["cod"] == 200:
        st.success("✅ Weather Details")

        st.metric("🌡️ Temperature", f"{data['main']['temp']} °C")

        st.metric("💧 Humidity", f"{data['main']['humidity']} %")

        st.metric("🌬️ Wind Speed", f"{data['wind']['speed']} m/s")

        st.info(f"☁️ Weather Condition: {data['weather'][0]['description'].title()}")

        icon = data["weather"][0]["icon"]

        icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

        st.image(icon_url, width=120)

        st.success(f"📍 City: {data['name']}")

        st.write("🌍 Country:", data["sys"]["country"])

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        st.write("🌅 Sunrise:", sunrise.strftime("%I:%M %p"))
        st.write("🌇 Sunset:", sunset.strftime("%I:%M %p"))

        from datetime import datetime

        st.caption(f"Last Updated: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")