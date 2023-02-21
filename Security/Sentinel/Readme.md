# ChatGPT-Sentinel

<b>Add Recommendations to Microsoft Sentinel Incidents from ChatGPT<br><br></b>
This Playbook sends the title and description of a Sentinel Incident to ChatGPT through the OpenAI API/Logic App connector (GPT3) and then writes the returned recommendations to the Incident's Activity Log pane.

An OpenAI API key is required: https://beta.openai.com/account/api-keys <br>

Even though it requests your API key during deployment, after deploying to Azure, you'll still need to make the API connection as shown:

![Alt text](https://github.com/rod-trent/SentinelPlaybooks/blob/master/ChatGPT/chatgpt.jpg?raw=true "ChatGPT Connection")

Requesting the API key during deployment stores the API key (so you don't lose it or forget it) in a Logic App Parameters value.

***This is based off original work by [Zubair Rahim](https://rodtrent.com/h15)
