import openai
import shutil
import os

# Set up your OpenAI API credentials
openai.api_key = 'api-key'

# Define the prompt for the conversation

def getAboutMe(prompt):
  aboutme_prompt_template = "Write a professional introduction of me with given below information. Answer it in 1st person singular. Make sure the the pagassage is around {words_limit} words. \n {prompt}"
  prompt = aboutme_prompt_template.format(words_limit=100, prompt=prompt)
  return getResponse(prompt)

def getSkills(prompt):
    skills_prompt_template = "Write a section in my portfolio named \"My creative skills & experiences.\" with given below information. Answer it in 1st person singular. Make sure the the pagassage is around {words_limit} words. \n {prompt}"
    prompt = skills_prompt_template.format(words_limit=100, prompt=prompt)
    return getResponse(prompt)

def getProjects(projects):
  processed_projects = []
  for project in projects:
    project_promt_template = "Write a brief info about the project titled {title}. Make sure the the pagassage is around {words_limit} words. Use the given below info \n {prompt}"
    prompt = project_promt_template.format(title=project[0], words_limit=100, prompt=project[1])
    current_project = []
    current_project.append(project[0])
    current_project.append(getResponse(prompt))
    processed_projects.append(current_project)

  return processed_projects

def getGetInTouch(prompt):
    getintouch_prompt_template = "Write a section in my portfolio named \"Get in touch\" with given below information. Answer it in 1st person singular. Make sure the the pagassage is around {words_limit} words. \n {prompt}"
    prompt = getintouch_prompt_template.format(words_limit=80, prompt=prompt)
    return getResponse(prompt)

def createCoverLetter(job_title, jd, info):
    coverletter_prompt_template = "Write a cover letter for the job titled {job_title}. Make sure the the pagassage is around {words_limit} words. Given below is the Job description:\n{jd}\n\n Given below is the canditate info \n {info}"
    prompt = coverletter_prompt_template.format(job_title=job_title, words_limit=300, jd=jd, info=info)
    return getResponse(prompt)

def getResponse(prompt):
  response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the engine (e.g., "text-davinci-003")
    prompt=prompt,
    max_tokens=1000  # Adjust the maximum number of tokens in the response as needed
  )
  answer = response.choices[0].text.strip()
  return answer


def makeZip(fileName):
    template_folder = 'template'
    output_file = 'temp'

    fileName.replace(' ', '\ ')
    file_name = 'data/'+fileName
    data_file_name = 'temp/data.json'

    shutil.copytree(template_folder, output_file)
    shutil.copy2(file_name, data_file_name)
    print(os.path.abspath(file_name))
    print(os.path.abspath(data_file_name))

    shutil.make_archive(output_file, 'zip', output_file)
    shutil.rmtree(output_file)

