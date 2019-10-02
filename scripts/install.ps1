$WshShell = New-Object -comObject WScript.Shell
$scriptDir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
$Shortcut = $WshShell.CreateShortcut("$env:APPDATA\Microsoft\Windows\SendTo\Folder.lnk")
$Shortcut.TargetPath = "$scriptDir\run.bat"
$Shortcut.WindowStyle = 7
$Shortcut.IconLocation = "%SystemRoot%\System32\SHELL32.dll,-235"
$Shortcut.WorkingDirectory = "$scriptDir"
$Shortcut.Save()