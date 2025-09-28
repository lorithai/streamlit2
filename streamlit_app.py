import streamlit as st
import base64
import os
from streamlit.components.v1 import html
# load media

audio_file = "media/audio/lizard.mp3"
audio_path = os.path.join("media","audio","lizard.mp3")
audio_path_waw = os.path.join("media","audio","lizard.waw")
with open(audio_path, "rb") as f:
    audio_bytes = f.read()
b64_audio = base64.b64encode(audio_bytes).decode()

audio_url = "https://raw.githubusercontent.com/lorithai/streamlit2/main/media/audio/lizard.mp3"



st.title("Lizard")
st.write(
    "b64_audio"
)
html_code = f'''
<style>
.lizard-btn {{
  background-color: #4CAF50;
  border: none;
  color: white;
  font-size: 28px;
  border-radius: 50%;
  width: 64px;
  height: 64px;
  cursor: pointer;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}}
</style>


<audio id="lizard-sound" controls="controls" src="data:audio/mp3;base64,{b64_audio}"" preload="auto"></audio>
<button class="lizard-btn" id="lizard-btn" aria-label="Play lizard sound">🦎</button>

<script>
const btn = document.getElementById('lizard-btn');
const audio = document.getElementById('lizard-sound');
btn.addEventListener('click', function() {{
    audio.currentTime = 0;
    audio.play().catch(err => console.log('play error', err));
}});
</script>
'''
html(html_code, height=140)
