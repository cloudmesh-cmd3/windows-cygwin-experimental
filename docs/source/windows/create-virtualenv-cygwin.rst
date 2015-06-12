Setting up virtualenv on Cygwin
=============================================

Step 1: Install pip
----------------------------------------------

 a. Download get-pip.py using the Cygwin terminal::

     wget https://bootstrap.pypa.io/get-pip.py
 

 b. Run the following::
   
       python get-pip.py

Step 2: Install virtualenv
------------------------------------------------
   Run the following command::

       pip install virtualenv

Step 3: Create a new Python environment
---------------------------------------- 

a. Create a vitual environment called ENV::

      virtualenv ENV

  Note: Its name can be anything, in this case it was ENV.

b. Activate the virtual environment::
   
      source ENV/bin/activate

  Note: The name of the current vitual environment will now appear on the left of the prompt (ENV) yourComputer: ) 

c. If you want to deactivate the virtual enviroment, run the following command::

        deactivate

d. If you want to delete the virtual environment, run the following command::
  
      rm -rf ENV

e. How to re-create a environment.

  The following command create a requirements.txt file, which contains a list of all packages in the current environment, and their respective versions.::

        pip freeze > requirements.txt

  In order to re-create the environment, you have to do the following::

       pip install -r requirements.txt
