@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
Path/To/End_Script.py > Path/To/Integrity/logs/%mydate%.txt
