import streamlit as st
import base64
import os
# load media
audio_file = "media/audio/lizard.mp3"
audio_path = os.path.join("media","audio","lizard.mp3")
audio_path_waw = os.path.join("media","audio","lizard.waw")
with open(audio_path, "rb") as f:
    audio_bytes = f.read()
b64_audio = base64.b64encode(audio_bytes).decode()


st.title("Lizard")
st.write(
    "b64_audio"
)

#st.audio(audio_path, format="audio/mpeg")

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


            
<audio id="lizard-sound2" controls>
  <source src="https://raw.githubusercontent.com/lorithai/streamlit2/main/media/audio/lizard.mp3" type="audio/mpeg">
</audio>
            


<button class="lizard-btn">🦎</button>

<script>
document.getElementById("lizard-btn").addEventListener("click", function() {
    var a = document.getElementById("lizard-sound");
    a.currentTime = 0;
    a.play();
});
</script>


""", unsafe_allow_html=True)


"""
<audio id="lizard-sound" controls>
  <source src="data:audio/mp3;base64,{b64_audio}"  preload="auto">
</audio>

<audio id="lizard-sound3" controls>
  <source src="https://raw.githubusercontent.com/lorithai/streamlit2/main/media/audio/lizard.wav" type="audio/wav">
</audio>
"""