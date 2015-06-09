Cygwin Installation
===========

We install cygwin via chocolatey. To do so you first have to
install chocolatey.

Please open a cmd.exe window as administrator (you can do this as follows):

....

Step 1: Install Chocolatey
-------------------------

You have to copy and paste **one** of the following comamnds into a terminal (cmd or PowerShell).

If you use cmd.exe::
 
   C:> @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

Or if you prefer to use PowerShell you can say::

  PS> iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))


Step 2: Install Cygwin
------------------------

Put the following line into cmd.exe::
  
  choco install --force -y cygwin 
 
Note: if Cygwin is already installed, --force will reinstall it.

Step 3: Install apt-cyg
--------------------------

Put the following command into Cygwin terminal (its shorcut can be found on your Desktop)::
  
  lynx -source rawgit.com/transcode-open/apt-cyg/master/apt-cyg > apt-cyg

  install apt-cyg /bin

Step 4: Install additional packages
---------------------------

Run the following command in Cygwin terminal::
  
  apt-cyg install wget curl connect-proxy emacs gedit openssh git graphviz grep make nano pico ncurses nc openssl ping pylint rsync keychain tail head vi vim which

Packages can be found `here`_

.. _here: https://cygwin.com/packages/package_list.html



We recommend that you install some packages that you may need in
future. This includes the following packages.

TODO: identify from the package list which are installe dby default in
cygwin and remove them from this list

Security::

  openssl
  opensssh
  keychain

Editors::

  nano  
  pico
  emacs
  vi
  vim

Development::
  
  git
  pylint
  make
  
Linux::

  grep
  head
  ncurses  
  nc
  ping
  rsync
  tail
  wget
  which

Visuzalization::

  graphviz
  dialog






