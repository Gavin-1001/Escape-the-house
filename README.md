# Escape The House

## Table of Contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Bugs](#bugs)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## Introduction
A text based terminal game where the user can play the game from the command line. The aim of the game is to find the drone and find a way out. Find items to use to defend against mobs and unlock doors to explore. 

## Design
#### Modular Code
* Because of the scale of this project, modularised code is essential as it allows for code reuseability.

* The project [Flow chart](https://github.com/Gavin-1001/Escape-the-attic/blob/main/assets/flowchart/Flowchart.pdf)


### Goals
The goal of this application was to create an adventure text-based game using the command line. The goal is to create an application that would play similar to the iconic text-based game, Zork.

### Audience
There is no specific target audience for this project. But I do believe that it would be attractive to users born between the 1960's and 1990's as they would of grown up with text-based games. 

## Technologies
* [Python](https://www.python.org/)
* Python modules([sys](https://docs.python.org/3/library/sys.html), [time](https://docs.python.org/3/library/time.html), [os](https://docs.python.org/3/library/os.html))

### Other libraries used
* Github
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Git](https://git-scm.com/)
* [Heroku](https://www.heroku.com/)

## Bugs
* The only issue in the project is that there is a import statement that has been imported locally, although it is not best practice, I removed the import and placed it at the top along with the other imports and I got a circular import error, I removed all imports and reimported everything again and still got the same error . The local import statements are listed below:
  1. forest.py line 45
  2. forest.py line 83
  3. house.py line 37
  4. helperFunction.py line 217

* Another bug I have encountered is clearing the terminal between sessions. I have the function calls, but it is not executing when ran.


## Testing
### Pep8 validation
* My chosen IDE for this project was PyCharm, which has a built in PEP 8 validator, the only PEP8 errors I encountered were W605 escape sequences which were associated with the acsii art in helperFunctions.py, and to remove redundant parentheses. I have kept the brackets in place as I have come from 5 years of Java and my brain is hardwired to brackets around flow control structures. 
* Screenshots can be found [here](https://github.com/Gavin-1001/Escape-the-attic/tree/main/assets/images)

## Deployment
As part of the project, this application had to be deployed on Heroku. Below are the steps to successfully deploy this application to Heroku. 

### Creating the Heroku app

* Before you begin deploying to Heroku, please check that your code in error free before continuing. 
* In the terminal you need to enter the command below, as Heroku will use the .txt file to import the required dependencies. 
 `pip3 freeze > requirements.txt`
* If you do not have a Heroku account create one [here](https://signup.heroku.com/). Or alternatively you can login to your Heroku account. 
* Once you have created your account or signed in. Navigate to the Heroku dashboard. 
* From the dashboard select the "New" button in the top right hand side of the screen. 
* Click "Create new app"
* Choose a unique name for your app, and choose your region. 
* Once that is done, click "Create app"

### Configuring Heroku App
* Once you have created the app in the section above, you now have to configure the app.
* To begin, navigate to the settings tab in the ribbon of the dashboard, scroll down to "Buildpacks" 
* For this application you will need to add two buildpacks, Python and Node.js. It is very important that Python is the first buildpack that you select, and then Node.js, as this will cause issues when you go to deploy the app, see below for a visual description of the buildpack structure.  
1. `heroku/python`
2. `heroku/nodejs`
* Next, if you have any files with sensitive information such as API keys or credentials they should be stored in the Config Vars section. 
* You must then create a _Config Var_ called `PORT`. Set this to `8000`

### Deploy Heroku App
* To deploy the application to Heroku, navigate to the deploy tab on the ribbon.
* In the "Deployment method" section select GitHub, after a few seconds click on the "Conntect to Github" button. This will take you to Github login, enter your email and password as usual and continue. 
* Enter your repository name in Github that you want to deploy on Heroku. 
* Finally you will be asked to choose if you want to deploy automatically or deploy manually.
* If you select "Automatic Deploy" Heroku will rebuild your project everytime you make a change to the code. 
* If you select "Manual Deploy" you will be responsible for rebuilding the project everytime you name a new change to the project. 
* Once the application has build successfully you will have the opportunity to visit your newly deployed application live site.
* To view the application live, navigate to the application dashboard, from there click "Open app" on the right hand side of the screen.

### Deploy Heroku App via CLI
As of 20/04/2022 Github has been hacked and OAuth tokens have been stolen, to stop further attacks Heroku has disabled users from deploying from Github and has asked users to deploy applications from the Heroku CLI. Until further notice, the section above "Deploy Heroku App" will not be accepted when trying to deploy.  

*  As the Heroku CLI has pre-requisites, I have left a link to the [install](https://devcenter.heroku.com/articles/heroku-cli) guide for the CLI, and pre-requisites
*  Once you have installed the CLI and pre-requisites, follow the section above on creating a Heroku app.
*  Next follow the "Configuring Heroku App", then return to here to continue. 
*  From the terminal, login in using the command
  `heroku login -i`
* You will be prompted to enter your heroku login and password. 
* Next you will be asked commit the project to Git. 
  `git init`
  `git add .`
  `git commit <--insert commit message-->`
* Once you have committed the application to Git, it is now time to deploy the application to Heroku.
  `git push heroku main`
* If you run into errors open the logs to check the issue. 
* To access the logs, navigate to the application dahsboard and click "More" located beside the "Open app" on the right hand side of the screen.
* Here the logs will display any issues that have prevented deployment. 
* One of the most common issue is that, when configuring the Buildpacks, some users put Node.js before Python, as mentioned in that section, this is one of the "issues".  

## Credits
#### 1. [Ascii Art](https://ascii.co.uk/art/) 
To add some graphic to the application, I decided to use ascii art to give some effect to the user experience. 

#### 2. [Stack Overflow](https://stackoverflow.com/questions/20302331/typing-effect-in-python)
During the initial design phase of the project, I wanted to make the application as nostalgic as possible. I wanted to give the impression that the text begin displayed was a narriator talking to the user. To do this I created a typing effect function called terminal_typing_effect which took text and the speed of the output text as parameters. This would take each char and sleep it for 0.05 seconds and then display it, giving the narriator effect.

#### 3. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
As this project is being hosted on Heroku, the boilerplate code is provided by Code Institute in order to be compatiable with Heroku, and display a terminal on screen for the user to access the application




