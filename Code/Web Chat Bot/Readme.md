# Web Chatbot for Azure Open AI

Full explanation and instructions for this code can be found at: [Building Your own Conversational Copilot with Python, Flask, and Azure Open AI SDK](https://rodtrent.substack.com/p/building-your-own-conversational)

Here’s the files that are required from the repo:

* **WebChatBot.py** - this is the primary app. Place this into the app’s primary working directory.

* **index.html** - this is the HTML for the web bot interface. Place the templates folder underneath the app’s primary working directory.

* **mainpage.css** - this is the CSS for the web bot interface. Place the static folder underneath the app’s primary working directory.

* **requirements.txt** - this is the file that is used to maintain the list of required libraries. This will be most important when creating a Web App deployment for Azure App Services.

* **webchatconfig.json** - this is the configuration file that is called from WebChatBot.py. This will need to be modified with your specific Azure Open AI information such as: model name, API key, API base URL, and GTP type.

Make sure you have Python installed. If you’re running a Windows system (like me), you can find the most current version of Python here: https://www.python.org/downloads/

This solution uses the Flask framework and the Azure OpenAI SDK. After you install Python, you can make sure you have both Flask and Azure OpenAI SDK installed by running the following install commands in a CMD window.

* pip install Flask 

* pip install openai 

Once all the requirements are in place, you run the app using the following command in a CMD window:

**python WebAppChatbot.py** 

The app will instruct you to open a browser window to http://127.0.0.1:5000/ to use your new Chatbot.
