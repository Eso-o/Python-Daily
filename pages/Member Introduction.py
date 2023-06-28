import streamlit as st
from PIL import Image
tab1, tab2 = st.tabs(["Qitong Xu", "Yu Chen"])
with tab1:
    st.title('**Member Introduction** :blush:')
    st.header('*Luoma-kneeling group*')
    st.subheader('**:blue[Qitong Xu]**')
    st.write("*Patience is the key in life*")
    st.divider()
    image1 = Image.open('t2.jpg')
    st.image(image1,width=480, caption="Chief Programmer, responsible for distribution and regional analysis webs")
with tab2:
    st.title('**Member Introduction** :blush:')
    st.header('*Luoma-kneeling group*')
    st.subheader('**:orange[Yu Chen]**')
    st.write("*Python is the key in life*")
    st.divider()
    image2 = Image.open('t3.jpg')
    st.image(image2, width=480,caption="Programmer, mainly responsible for the personal analysis module")
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
    st.image(image1,width=480, caption="Chief Programmer, responsible for distribution and regional analysis webs")
with tab2:
    st.title('**Member Introduction** :blush:')
    st.subheader('**:orange[Yu Chen]**')
    st.write("*Python is the key in life*")
    st.divider()
    image2 = Image.open('t3.jpg')
    st.image(image2, width=480,caption="Programmer, mainly responsible for the personal analysis module")
    '''
        st.code(code,language='python')
