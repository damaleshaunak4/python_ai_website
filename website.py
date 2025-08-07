import streamlit as st
import google.generativeai as genai

api_key = st.secrets['GOOGLE_API_KEY']

client = genai.Client(api_key="api_key")

col1, col2 = st.columns(2)

with col1:
    st.subheader("hi :wave:")
    st.title("I'm AI")

with col2:
    st.image("images/hi.png")

st.title(' ')


st.title("AI BOT")

user_question = st.text_input("Ask me anything")
if st.button("Ask",use_container_width=True):
    prompt = user_question
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents = user_question
    )

    st.write(response.text)


st.title("")
st.title("my setup")
st.image("images/setup.png")


st.write(' ')
st.title('my skills ')
st.slider('programming',0 ,100, 70)
st.slider('designing', 0, 100, 85)
st.slider('robotics', 0, 100, 70)


st.write(' ')
st.title("My Jets")

col1, col2, col3 =st.columns(3)


with col1:
    st.image("images/1.png")
    st.image("images/6.jpg")
    st.image("images/3.png")

with col2:
        st.image("images/4.png")
        st.image("images/8.avif")
        st.image("images/2.png")

with col3:
    st.image("images/7.jpg")
    st.image("images/9.jpg")
    st.image("images/5.png")


st.subheader(' ')
st.write('CONTACT')
st.title('For any inquiries, please contact me at')
st.subheader('contact@ai.com ')
