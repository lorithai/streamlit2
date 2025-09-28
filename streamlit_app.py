import streamlit as st
import base64

# load media
audio_file = "media/audio/lizard.mp3"
with open(audio_file, "rb") as f:
    audio_bytes = f.read()


st.title("Lizard")
st.write(
    "Hello"
)

b64_audio = base64.b64encode(audio_bytes).decode()

st.markdown("""
<style>
.lizard-btn {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 12px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 50%;  /* Makes it round */
    width: 60px;
    height: 60px;
    cursor: pointer;
}
</style>

<audio id="lizard-sound">
  <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mpeg">
</audio>

<button class="lizard-btn" onclick="document.getElementById('lizard-sound').play()"><div style="font-size:1.5rem;width:100%;text-align:center;">🦎</div></button>
""", unsafe_allow_html=True)