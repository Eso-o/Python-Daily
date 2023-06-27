import streamlit as st
from PIL import Image
tab1, tab2 = st.tabs(["Qitong Xu", "Yu Chen"])
with tab1:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:blue[Qitong Xu]**')
    st.write("*Patience is the key in life*")
    st.divider()
    image1 = Image.open('t2.jpg')
    st.image(image1,width=400, caption="Chief Programmer, responsible for distribution and regional analysis webs")
with tab2:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:orange[Yu Chen]**')
    st.write("*Python is the key in life*")
    st.divider()
    image2 = Image.open('t3.jpg')
    st.image(image2, width=800,caption="Programmer, mainly responsible for the personal analysis module")
with st.expander("Show source code"):
        code = '''
import streamlit as st
from PIL import Image
tab1, tab2 = st.tabs(["Qitong Xu", "Yu Chen"])
with tab1:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:blue[Qitong Xu]**')
    st.write("*Patience is the key in life*")
    st.divider()
    image1 = Image.open('t2.jpg')
    image1=image1.resize(20,20)
    st.image(image1, caption="Chief Programmer, responsible for distribution and regional analysis webs")
with tab2:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:orange[Yu Chen]**')
    st.write("*Python is the key in life*")
    st.divider()
    image2 = Image.open('t3.jpg')
    image2=image2.resize(20,20)
    st.image(image2, caption="Programmer, mainly responsible for the personal analysis module")
    '''
        st.code(code,language='python')
