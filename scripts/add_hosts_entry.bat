@echo off
:: Right-click this file and select "Run as administrator"
echo Adding website.oil and website.h2o to hosts file...
echo 127.0.0.1 website.oil >> %WINDIR%\System32\drivers\etc\hosts
echo 127.0.0.1 website.h2o >> %WINDIR%\System32\drivers\etc\hosts
echo [SUCCESS] Added website.oil and website.h2o to %WINDIR%\System32\drivers\etc\hosts!
pause
