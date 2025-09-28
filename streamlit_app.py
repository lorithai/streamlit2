import streamlit as st

st.title("Lizard")
st.write(
    "Hello"
)

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
  <source src="https://www.soundjay.com/buttons/sounds/button-3.mp3" type="audio/mpeg">
</audio>

<button class="lizard-btn"><div style="font-size:1.5rem;width:100%;text-align:center;">🦎</div></button>
""", unsafe_allow_html=True)