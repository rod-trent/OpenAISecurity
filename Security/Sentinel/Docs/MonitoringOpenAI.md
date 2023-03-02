Diag logging for Azure Open AI https://rodtrent.com/umz

Actions to monitor: https://rodtrent.com/2z0

Tables and designation (KQL):
<br>
AzureDiagnostics<br>
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
<br>
<br>
AzureActivity
| where TimeGenerated >= (24h)
| where OperationNameValue contains "MICROSOFT.COGNITIVESERVICES"
