@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
C:/Integrity_Test/TestGenius/Integrity/End_Script.py > C:/Integrity_Test/TestGenius/Integrity/logs/%mydate%.txt