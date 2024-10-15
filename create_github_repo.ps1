$env:GITHUB_TOKEN = "Ihr_Token_Hier"  # Setzen Sie dies in der PowerShell-Sitzung, nicht im Skript

$createRepoUrl = "https://api.github.com/user/repos"
$createRepoBody = @{
    name = "Disk-Management-Tool"
    private = $false
} | ConvertTo-Json

$headers = @{
    Authorization = "token $env:GITHUB_TOKEN"
    Accept = "application/vnd.github.v3+json"
}

try {
    Invoke-RestMethod -Uri $createRepoUrl -Method Post -Body $createRepoBody -Headers $headers -ContentType "application/json"
    Write-Host "GitHub repository created successfully."
}
catch {
    Write-Host "Failed to create GitHub repository. Error: $_"
    exit
}

# GitHub-Remote hinzufügen
git remote add origin https://github.com/Blazzcantara/Disk-Management-Tool.git

# Push to GitHub
git push -u origin master

Write-Host "Project successfully pushed to GitHub."

# Token aus der Umgebungsvariable entfernen
Remove-Item Env:GITHUB_TOKEN
