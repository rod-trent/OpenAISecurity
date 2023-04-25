# Web Chatbot for Azure Open AI

Full explanation and instructions for this code can be found at: 

[Building Your own Conversational Copilot with Python, Flask, and Azure Open AI SDK](https://rodtrent.substack.com/p/building-your-own-conversational)

Here’s the files that are required from the repo:

* **WebChatBot.py** - this is the primary app. Place this into the app’s primary working directory.

* **index.html** - this is the HTML for the web bot interface. Place this inside a Templates folder underneath the app’s primary working directory.

* **requirements.txt** - this is the file that is used to maintain the list of required libraries. This will be most important when creating a Web App deployment for Azure App Services.

* **webchatconfig.json** - this is the configuration file that is called from WebChatBot.py. This will need to be modified with your specific Azure Open AI information such as: model name, API key, API base URL, and GTP type.
