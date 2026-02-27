import streamlit as st

st.title("🎬 Hollywood Movie Analysis")
st.write("Welcome to my first app!")

# User input စမ်းကြည့်မယ်
movie = st.text_input("What is your favorite movie?")
if movie:
    st.write(f"Oh! I love {movie} too!")
