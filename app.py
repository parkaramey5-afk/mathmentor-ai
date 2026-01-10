import streamlit as st
import sympy as sp

st.set_page_config(page_title="MathMentor AI")

st.title("📘 MathMentor AI")
st.write("Smart Math Solver using Symbolic Computation")

x = sp.symbols('x')

topic = st.selectbox(
    "Select topic",
    [
        "Solve Equation",
        "Differentiate",
        "Integrate",
        "Simplify Expression",
        "Factor Expression",
        "Limit"
    ]
)

expression = st.text_input("Enter mathematical expression:")

if st.button("Get Answer"):
    if expression.strip() == "":
        st.warning("Please enter an expression.")
    else:
        try:
            expr = sp.sympify(expression)

            if topic == "Solve Equation":
                result = sp.solve(expr, x)

            elif topic == "Differentiate":
                result = sp.diff(expr, x)

            elif topic == "Integrate":
                result = sp.integrate(expr, x)

            elif topic == "Simplify Expression":
                result = sp.simplify(expr)

            elif topic == "Factor Expression":
                result = sp.factor(expr)

            elif topic == "Limit":
                point = st.number_input("Limit as x →", value=0.0)
                result = sp.limit(expr, x, point)

            st.success("Answer:")
            st.latex(sp.latex(result))

        except Exception as e:
            st.error("Invalid expression or unsupported operation.")
