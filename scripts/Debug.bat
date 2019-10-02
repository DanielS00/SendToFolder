@echo off
cls
:start
python ..\src\sendtofolder.py %*
pause
goto start