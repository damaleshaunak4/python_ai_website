import streamlit as st
import google.generativeai as genai


myapi_key = st.secrets['GOOGLE_API_KEY']

genai.configure(api_key=myapi_key)

model = genai.GenerativeModel(model_name="gemini-2.5-flash")


# UI
col1, col2 = st.columns(2)

with col1:
    st.subheader("hi :wave:")
    st.title("I'm AI")

with col2:
    st.image("images/hi.png")

st.title(' ')


st.title("AI BOT")

user_question = st.text_input("Ask me anything")
 if user_question.strip():
        try:
            response = model.generate_content(user_question)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error from Gemini API: {e}")
    else:
        st.warning("Please enter a question.")



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
