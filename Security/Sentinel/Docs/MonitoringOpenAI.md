Diag logging for Azure Open AI https://rodtrent.com/umz

Actions to monitor: https://rodtrent.com/2z0

Tables and designation (KQL):
<br><br>
AzureDiagnostics<br>
| where TimeGenerated >= (24h)<br>
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
<br>
<br>
AzureActivity<br>
| where TimeGenerated >= (24h)<br>
| where OperationNameValue contains "MICROSOFT.COGNITIVESERVICES"<br>
| where CategoryValue == "Administrative"<br>

<br><br>
<img title="Diag Settings" alt="Diag Settings" src="https://github.com/rod-trent/OpenAISecurity/blob/main/Security/Sentinel/Docs/openailogs.png">
