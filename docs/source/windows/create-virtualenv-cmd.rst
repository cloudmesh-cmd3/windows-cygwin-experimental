Setting up virtualenv on windows machine
==========================================

Step 1: Install Python 
------------------------------------------

:ref:`How to install Python on windows machine <install-python-windows>`

Step 2: Install virtualenv
------------------------------------------

Open the cmd terminal, run the the following command in it::

   pip install virtualenv

Step 3: Create a new Python environment
----------------------------------------

a. Create a vitual environment called ENV::

    virtualenv ENV

  Note: Its name can be anything, in this case it was ENV.

b. Activate the virtual environment::

      ENV/Script/activate

  Note: The name of the current vitual environment will now appear on the left of the prompt.

c. If you want to deactivate the virtual enviroment, run the following command::

       deactivate


