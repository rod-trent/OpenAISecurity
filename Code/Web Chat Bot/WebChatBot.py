import os  
import openai  
import json 
from flask import Flask, request, render_template  
  
app = Flask(__name__)  
  
# Load config values
with open(r'webchatconfig.json') as config_file:
    config_details = json.load(config_file)
    
# Setting up the deployment name
chatgpt_model_name = config_details['CHATGPT_MODEL_NAME']

# This is set to `azure`
openai.api_type = "azure"

# The API key for your Azure OpenAI resource.
openai.api_key = config_details['OPENAI_API_KEY']

# The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
openai.api_base = config_details['OPENAI_API_BASE']

# Currently Chat Completion API have the following versions available: 2023-03-15-preview
openai.api_version = config_details['OPENAI_API_VERSION']

openai.gpt_type = config_details['OPENAI_GPT_TYPE']
  
# Define the function to communicate with Azure OpenAI ChatGPT  
def generate_response(prompt):  
    model_engine = chatgpt_model_name  
    response = openai.Completion.create(  
        engine=model_engine,  
        prompt=prompt, 
        temperature=0.4, 
        max_tokens=500,
        top_p=0.45,  
        frequency_penalty=0,
        presence_penalty=0,
        stop=None           
    )  
    return response.choices[0].text.strip()  
  
@app.route('/', methods=['GET', 'POST'])  
def index():  
    if request.method == 'POST':  
        user_question = request.form['question']  
        generated_response = generate_response(user_question)  
        return render_template('index.html', response=generated_response)  
    return render_template('index.html')  
  
if __name__ == '__main__':  
    app.run(debug=True)  
