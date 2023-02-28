//This PowerShell script connects to the GPT API, asks a question, and retrieves the answer.

//Get your API key here: https://platform.openai.com/account/api-keys


# Set your API key
$apiKey = "YOUR_API_KEY"

# Set the API endpoint URL
$url = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Set the request headers
$headers = @{
    "Authorization" = "Bearer $apiKey"
    "Content-Type" = "application/json"
}

# Set the request body
$body = @{
    "prompt" = "What is Microsoft Sentinel?"
    "temperature" = 0.5
    "max_tokens" = 100
}

# Send the HTTP request to the API endpoint
$response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body ($body | ConvertTo-Json)

# Print the response
Write-Host $response.choices.text
