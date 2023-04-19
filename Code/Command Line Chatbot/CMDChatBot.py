# if needed, install and/or upgrade to the latest version of the OpenAI Python library
# pip install --upgrade openai

# import os module & the OpenAI Python library for calling the OpenAI API
import os
import openai
import json
import requests

# Load config values
with open(r'config.json') as config_file:
    config_details = json.load(config_file)

# Load question file
with open(r'question.json') as q_file:
    q_details = json.load(q_file)
    
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

# Question to ask
openai.msg = q_details['CHATGPT_MSG']

# A sample API call for chat completions looks as follows:
# Messages must be an array of message objects, where each object has a role (either "system", "user", or "assistant") and content (the content of the message).
# For more info: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference#chat-completions

try:
    response = openai.ChatCompletion.create(
                  engine=chatgpt_model_name,
                  messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": openai.msg}
                    ]
                )

    # print the response
    print(response['choices'][0]['message']['content'])
    
except openai.error.APIError as e:
    # Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")

except openai.error.AuthenticationError as e:
    # Handle Authentication error here, e.g. invalid API key
    print(f"OpenAI API returned an Authentication Error: {e}")

except openai.error.APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")

except openai.error.InvalidRequestError as e:
    # Handle connection error here
    print(f"Invalid Request Error: {e}")

except openai.error.RateLimitError as e:
    # Handle rate limit error
    print(f"OpenAI API request exceeded rate limit: {e}")

except openai.error.ServiceUnavailableError as e:
    # Handle Service Unavailable error
    print(f"Service Unavailable: {e}")

except openai.error.Timeout as e:
    # Handle request timeout
    print(f"Request timed out: {e}")
    
except:
    # Handles all other exceptions
    print("An exception has occured.")