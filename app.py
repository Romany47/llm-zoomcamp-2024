import streamlit as st
import rag

def main():
    st.title("DTC Q&A System")

    with st.form(key='rag_form'):
        prompt = st.text_input("Enter your prompt")
        response_placeholder = st.empty()
        submit_button = st.form_submit_button(label='Submit')
        courses = [
            "data-engineering-zoomcamp",
            "machine-learning-zoomcamp",
            "mlops-zoomcamp"
        ]
        zoomcamp_option = st.selectbox("Select a zoomcamp", courses)

    if submit_button:
        response_placeholder.markdown("Loading...")
        response = rag.qa_bot(prompt, zoomcamp_option)
        response_placeholder.markdown(response)

if __name__ == "__main__":
    main()