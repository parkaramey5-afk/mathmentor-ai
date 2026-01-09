import streamlit as st

st.set_page_config(page_title="MathMentor AI")

st.title("📘 MathMentor AI")
st.write("Your AI-powered math learning assistant")

level = st.selectbox(
    "Select your level",
    ["School", "Undergraduate", "Postgraduate"]
)

question = st.text_area("Enter your math question or concept:")

def fake_ai_answer(q, lvl):
    return f"""
### Explanation ({lvl} Level)

**Question:** {q}

This concept can be understood as follows:

- We break the idea into simple steps
- Provide definitions and intuition
- Explain with an example

📌 *This response is generated using a simulated AI pipeline for demonstration purposes.*
"""

if st.button("Ask MathMentor"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = fake_ai_answer(question, level)
            st.success("Answer:")
            st.markdown(answer)
