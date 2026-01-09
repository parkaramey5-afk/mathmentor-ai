import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="MathMentor AI")

st.title("📘 MathMentor AI")
st.write("Your AI-powered math learning assistant")

level = st.selectbox(
    "Select your level",
    ["School", "Undergraduate", "Postgraduate"]
)

question = st.text_area("Enter your math question or concept:")

if st.button("Ask MathMentor"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"You are a math tutor for {level} students. Explain clearly:\n{question}"
            )

            st.success("Answer:")
            st.write(response.output_text)

