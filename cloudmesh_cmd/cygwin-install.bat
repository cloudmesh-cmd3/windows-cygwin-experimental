REM do NOT run this file. Must be run cygwin-install.py instead. 
@ECHO OFF
SETLOCAL
  FOR /F %%D in ("%CD%") DO SET DRIVE=%%~dD

  SET DFLTSITE=http://mirror.csclub.uwaterloo.ca/cygwin/

  SET DFLTLOCALDIR=c:\Temp\cygwindownload
  SET DFLTROOTDIR=%DRIVE%\cygwin

  SET SITE=-s %DFLTSITE%
  SET LOCALDIR=-l %DFLTLOCALDIR%
  SET ROOTDIR=-R %DFLTROOTDIR%
  
REM add packages here
SET PACKAGES=-P emacs-w32,curl,openssh

REM installs cygwin
ECHO [INFO] C:\Temp\cygwindownload\setup.exe -q -D -L %SITE% %LOCALDIR% %PACKAGES%
C:\Temp\cygwindownload\setup.exe -q -D -L %SITE% %LOCALDIR% %PACKAGES%

REM removes Temp folder
rd /s /q "C:\Temp\"
ECHO [INFO] Cygwin installation is complete

