@echo off
del /s /q *.pyo
del kodi18.zip
setlocal
cls
endlocal
7z.exe a kodi18.zip "*.*" -r

