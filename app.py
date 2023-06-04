# Add all your application here
# app.add_app("Create Portfolio", portfolioGenerator.app)
# app.add_app("Create Cover Letter", coverLetterCreator.app)

# Contents of ~/my_app/streamlit_app.py
import streamlit as st
from apps import portfolioGenerator, coverLetterCreator

def main_page():
    st.markdown("# PORTFOLIIFY🎈")
    st.markdown("## Create your portfolio and cover letter in seconds")
    st.markdown("### How it works?")
    st.markdown("It is powered by OpenAI's GPT-3. It uses the information you provide to generate a portfolio or cover letter. It is not perfect but it is a good starting point. You can edit the generated text to make it more personal.")

    st.markdown("### How to use?")
    st.markdown("So simple navigate to pages and fill the form. You can also edit the generated text to make it more personal.")

    st.markdown("With ❤️ by [Sri Ram](https://www.linkedin.com/in/sriram-km)")


def page2():
    portfolioGenerator.app()

def page3():
    coverLetterCreator.app()

option = st.sidebar.selectbox(
    'Menu',
    ('Home', 'Create Portfolio', 'Create cover latter'))

if option == 'Home':
    main_page()
elif option == 'Create Portfolio':
    page2()
elif option == 'Create cover latter':
    page3()
