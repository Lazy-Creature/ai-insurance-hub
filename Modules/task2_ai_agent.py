# task2_ai_agent.py
import streamlit as st
import re

# --- Premium Calculator Tool ---
def premium_calculator(user_input: str):
    try:
        # Extract structured inputs
        age_match = re.search(r"age\s*=?\s*(\d+)", user_input)
        coverage_match = re.search(r"coverage\s*=?\s*(\d+)", user_input)
        term_match = re.search(r"term\s*=?\s*(\d+)", user_input)

        if not age_match or not coverage_match or not term_match:
            return "Please provide input in format: age=<value>, coverage=<value>, term=<value>"

        age = int(age_match.group(1))
        coverage = float(coverage_match.group(1))
        term = int(term_match.group(1))

        # Premium Calculation
        base = 0.005
        age_factor = 1 + (max(0, age - 30)) * 0.01
        annual = coverage * base * age_factor
        total = annual * term

        return {
            "Age": age,
            "Coverage": coverage,
            "Term years": term,
            "Annual premium": round(annual, 2),
            "Total premium": round(total, 2)
        }

    except Exception as e:
        return f"Error: {str(e)}"


# --- Agent Runner ---
def run_agent(user_query=None):
    """
    If user_query is passed, calculates and returns the result (used from app.py)
    Otherwise, shows standalone Streamlit UI.
    """
    if user_query:
        return premium_calculator(user_query)

    # Standalone Streamlit UI***************************************************************** 
    st.subheader("Premium Calculator Agent")
    user_query = st.text_input("Enter structured input (age=..., coverage=..., term=...):")

    if st.button("Calculate"):
        if user_query:
            result = premium_calculator(user_query)
            if isinstance(result, dict):
                st.write("**Premium Calculator Result:**")
                st.json(result)  # show result on UI
            else:
                st.write(result)
        else:
            st.warning("Please enter input first.")

#*********************************************************************************************
# Run standalone
if __name__ == "__main__":
    run_agent()
