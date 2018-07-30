@echo off
set DEST=.\.exvim.algo_data
set TOOLS=D:\Program\exVim\vimfiles\tools\
set EXCLUDE_FOLDERS=__pycache__ 
set TMP=%DEST%\_ID
set TARGET=%DEST%\ID
call %TOOLS%\shell\batch\update-idutils.bat
