import streamlit as st
import os
import json
from apps import ai_util

def app():
    st.title("Create your cover letter")

    with st.form("my_form"):
        path = "data/"
        dir_list = os.listdir(path)
        option = st.selectbox('User',set(dir_list))
        job_title = st.text_input("Job Title")
        jd = st.text_area("Job Description", height=150)

        submitted = st.form_submit_button("Create Cover Letter")

        if submitted:
            data = "data/" + option
            f = open(data)
            json_data = json.load(f)
            f.close()

            canditata_prompt = "Name: "+ json_data['name'] +"\nEmail: " + json_data['emailid']

            canditata_prompt += "\n\nAbout me: "+json_data['aboutme']
            canditata_prompt += "\n\nSkills: "+json_data['skills_experience']


            cv = ai_util.createCoverLetter(job_title, jd, canditata_prompt)
            st.write(cv)


