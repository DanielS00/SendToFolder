@echo off
cls
echo SendToFolder installation
powershell -executionpolicy bypass -file ".\scripts\install.ps1"
if exist %appdata%\Microsoft\Windows\SendTo\Folder.lnk (
    echo Installation successful!
) else (
    echo Something went wrong.
)
pause