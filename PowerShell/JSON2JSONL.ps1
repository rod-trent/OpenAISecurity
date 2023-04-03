$jsonFilePath = "path\to\json\file"
$jsonlFilePath = "path\to\jsonl\file"

# Read the content of JSON file
$jsonContent = Get-Content $jsonFilePath -Raw

# Convert the JSON content to an array of objects
$jsonObjects = ConvertFrom-Json $jsonContent

# Convert each object to a JSONL string and write it to the JSONL file
$jsonObjects | ForEach-Object { $_ | ConvertTo-Json -Depth 1 | Out-File -FilePath $jsonlFilePath -Append }
