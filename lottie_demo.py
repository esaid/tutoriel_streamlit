import requests
import json
import time
import streamlit as st
from streamlit_lottie import st_lottie



myButton =st.button('Cliquez moi !')

if myButton:
    st.caption('Vous venez de me :red[cliquer] :ok:')

st.stop()
def bar_progression(progress, t):
    percent_complete = 0
    my_bar = st.progress(percent_complete)
    while percent_complete < 100:
        percent_complete += progress
        time.sleep(t)
        my_bar.progress(percent_complete)
    my_bar.empty()

number = st.number_input ( 'Pick a number', 0, 10 )
bar_progression(number, 2)

st.stop()





import streamlit as st
from PIL import Image

image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')

st.stop()


















# pour les fichiers
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# pour les liens
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# le fichier de l animation
cpu_file = "cpu.json"
lottie_fichier_animation = load_lottiefile(cpu_file)
st_lottie(lottie_fichier_animation, speed=1, height=200)

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_vsg5kswn.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json, height=200)

st.stop()



