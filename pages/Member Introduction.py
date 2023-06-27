import streamlit as st
from PIL import Image
tab1, tab2 = st.tabs(["Qitong Xu", "Yu Chen"])
with tab1:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:blue[Qitong Xu]**')
    image = Image.open('t2.jpg')
    st.image(image, caption="Chief Programmer, responsible for distribution and regional analysis webs")
    st.divider()
    st.write("*Patience is the key in life*")
with tab2:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:blue[Qitong Xu]**')
    image = Image.open('t3.jpg')
    st.image(image, caption="Programmer, mainly responsible for the personal analysis module")
    st.divider()
    st.write("*Python is the key in life*")
