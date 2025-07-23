
@echo off
echo [+] Clearing logs...
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /f
del /F /Q "%APPDATA%\Microsoft\Windows\Recent\*"
del /F /Q "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"
del /F /S /Q "%TEMP%\*.*"
del /F /S /Q C:\Windows\Prefetch\*.*
