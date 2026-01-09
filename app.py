import streamlit as st
from openai import OpenAI

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
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a helpful math tutor explaining concepts at {level} level."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            st.success("Answer:")
            st.write(response.choices[0].message.content)
