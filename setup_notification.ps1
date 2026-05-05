# Run this ONCE to set up daily automatic notification at 9 AM
# Open PowerShell as Administrator and paste this script

$taskName = "SheshandraLeetCodeReminder"
$scriptPath = "C:\Users\Sheshandra Reddy\OneDrive\Desktop\dsa-practice\run_daily.bat"

# Create the scheduled task
$action = New-ScheduledTaskAction -Execute $scriptPath
$trigger = New-ScheduledTaskTrigger -Daily -At "09:00AM"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -RunLevel Highest `
    -Force

Write-Host "✅ Daily reminder set for 9:00 AM every day!" -ForegroundColor Green
Write-Host "Task name: $taskName" -ForegroundColor Yellow
Write-Host "You can also run manually by double-clicking run_daily.bat" -ForegroundColor Cyan
