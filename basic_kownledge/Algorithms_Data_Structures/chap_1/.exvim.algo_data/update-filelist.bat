@echo off
set DEST=.\.exvim.algo_data
set TOOLS=D:\Program\exVim\vimfiles\tools\
set FILE_SUFFIXS=
set GAWK_SUFFIX=exc
set FILE_FILTER_PATTERN=""
set FOLDER_FILTER_PATTERN=".*\\\\__pycache__\\\\.*"
set TMP=%DEST%\_files_gawk
set TMP2=%DEST%\_files
set TARGET=%DEST%\files
set ID_TARGET="%DEST%\idutils-files"
call %TOOLS%\shell\batch\update-filelist.bat