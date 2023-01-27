import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie


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
