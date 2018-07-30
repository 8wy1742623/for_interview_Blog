@echo off
set DEST=.\.exvim.algo_data
set TOOLS=D:\Program\exVim\vimfiles\tools\
set TMP=%DEST%\_inherits
set TARGET=%DEST%\inherits
call %TOOLS%\shell\batch\update-inherits.bat
