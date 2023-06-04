import base64
import streamlit as st
import json
from apps import ai_util


def app():
    st.title("Hack your portfolio")

    # Create a form using the form container
    with st.form("my_form"):
        # Add form components
        name = st.text_input("Name")
        email = st.text_input("Email")
        address = st.text_input("Address")
        cv = st.text_input("CV link")
        about_me = st.text_area("Give info for \"About me\" section", height=150, placeholder="Passionate software developer with a knack for problem-solving and a love for clean code. Experienced in building efficient and scalable applications, with expertise in languages such as Python, Java, and JavaScript. Constantly seeking new challenges to expand my skills and deliver exceptional software solutions.")
        projects = st.text_area("Give info for \"Projects\" section", height=200, placeholder="Give input in the below format\n[Project 1 title]\n[Project 1 description]\n\n[Project 2 title]\n[Project 2 description]\n\n[Project 3 title]\n[Project 3 description]\n\n")
        skills = st.text_area("Give info for \"Skills\" section",placeholder="Give input in the below format\n[Skill 1] [Skill 1 percentage]\n[Skill 2] [Skill 2 percentage]\n\n[Skill 3] [Skill 3 percentage]\n[Skill 4] [Skill 4 percentage]")
        skills_desc = st.text_area("Give info for \"Skills description\" section",placeholder="Proficient in full-stack development, with expertise in frontend technologies like HTML, CSS, and JavaScript, and backend frameworks such as Node.js and Django. Skilled in database management systems like MySQL and MongoDB. Experienced in version control tools like Git and project management methodologies such as Agile.")
        references = st.text_area("Give info for \"References\" section", height=200, placeholder="Give input in the below format\n[Refered person name]\n[Refernce message]\n[Linkin profile link]\n\n[Refered person name]\n[Refernce message]\n[Linkin profile link]\n\n[Refered person name]\n[Refernce message]\n[Linkin profile link]\n\n")
        get_in_touch = st.text_area("Give info for \"Get in touch\" section", placeholder="Let's collaborate on your next project! Feel free to reach out to me via email at or connect with me on LinkedIn. I'm always excited to discuss new opportunities, share ideas, and contribute to innovative software solutions.")
        adjectives = st.text_area("Adjectives for you",
                                    placeholder="Give the input as comma separated value like shown below\nDeveloper,Math lover,Leaner")

        submitted = st.form_submit_button("Submit")



        # Handle form submission
        if submitted:
            # Process the form data
            process_form_data(name, email, address, cv, about_me, projects, skills, skills_desc, references, get_in_touch, adjectives)
            href = download_link(open('temp.zip', 'rb').read(), 'portfolio.zip', 'Download Portfolio')
            st.markdown(href, unsafe_allow_html=True)

def download_link(object_to_download, download_filename, download_link_text):
    b64 = base64.b64encode(object_to_download).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
    return href

def process_form_data(name, email, address, cv, about_me, projects, skills, skills_desc, references, get_in_touch, adjectives):
    data = {}
    data['name'] = name
    data['emailid'] = email
    data['address'] = address
    data['cv-link'] = cv
    data['aboutme'] = ai_util.getAboutMe(about_me)
    data['skills_experience'] = ai_util.getSkills(skills_desc)

    skills_parts = skills.split('\n')
    skills_list = []
    for skill_part in skills_parts:
        current_skill = skill_part.split(' ')
        skills_list.append(current_skill)
    data['skills'] = skills_list

    projects_parts = projects.split('\n\n')
    projects_list = []
    for project_part in projects_parts:
        current_project = project_part.split('\n')
        projects_list.append(current_project)
    data['projects'] = ai_util.getProjects(projects_list)

    references_parts = references.split('\n\n')
    references_list = []
    for reference_part in references_parts:
        current_reference = reference_part.split('\n')
        references_list.append(current_reference)
    data['references'] = references_list

    data['get_in_touch'] = ai_util.getGetInTouch(get_in_touch)

    adjectives_part = adjectives.split(",")
    typo_skills_arr = []
    for adjective in adjectives_part:
        adjective = adjective.strip()
        typo_skills_arr.append(adjective)

    data['typo_skills'] = typo_skills_arr

    json_object = json.dumps(data, indent=4)

    fileName = email +'.json'

    f = open('data/'+fileName, 'w')
    f.write(json_object)
    f.close()

    ai_util.makeZip(fileName)
