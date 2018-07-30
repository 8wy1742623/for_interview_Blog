@echo off
set DEST=.\.exvim.algo_data
set TOOLS=D:\Program\exVim\vimfiles\tools\
set TMP=%DEST%\_symbols
set TARGET=%DEST%\symbols
call %TOOLS%\shell\batch\update-symbols.bat
