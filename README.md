These are the following steps to run project : 
1. Python must be intalled on the system.

2. Installing virtualenv : Run these commands on command prompt
   On macOS and Linux:
    python3 -m pip install --user virtualenv
    
  On Windows:
   py -m pip install --user virtualenv
   
   ![1](https://user-images.githubusercontent.com/60659288/96621154-e87a9f00-1325-11eb-8bc4-f7b171269dce.JPG)

   
3. Creating a virtual environment:To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands.

      On macOS and Linux:
      python3 -m venv env
      
      On Windows:
      py -m venv env
      
      
4. Activating a virtual environment:   
      On macOS and Linux:
          source env/bin/activate
          
      On Windows:
        .\env\Scripts\activate
        
        ![2](https://user-images.githubusercontent.com/60659288/96621287-14962000-1326-11eb-83c0-48e12c093caf.JPG)

        
5. Installing packages
Now that you’re in your virtual environment you can install packages.Go to the project directory i.e., "flipr-"  and run the following command

  pip install -r requirements.txt
  ![3](https://user-images.githubusercontent.com/60659288/96621483-4a3b0900-1326-11eb-81e6-c8e74f742247.JPG)

 
6. Run Server : After installing all the requirements run the following command in the command prompt 
    python manage.py runserver
    
 
    
