# Fantasy Football

* [Project Brief](#Porject-Brief)
    * [My Approach to the application](#My-approach-to-the-application)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Future Improvements](#future-improvements)
* [Authors](#authors)

# Project Brief 
The brief set for this project is to be able to create a CRUD application, with the tools, methodologies and technologies that cover all core modules covered during training.

In order to achieve the brief, the following requirements:<br>
* Trello board
* Relational database - with 2 tables
* Clear documentation including design, architecture, and risk assessment
* A fuctional CRUD app - desainged using python
* Automated tests for the CRUD application - unit and integration testing
* Using Flask to create a functioning front-end website
* Code integrated into a version control system which is built through a CI server, and deployed to a GCP virtual machine. 

## My Approach to the application

In order to achieve the requirements, I decided to create a fantasy football application which allows a user to:
* Create a team that stores a:
    * team name
    * sponsor of the team
* Add players to the team they have created. The following information on a player would be stored:
    * Name
    * Position
    * The club they play for
    * Height
* View and update the team
* Delete the team

# Architecture

## Database Structure 

Below are two different ER diagrams showing the before and after database structures. 

### 1st ER-Diagram  

![ERD-1](https://imgur.com/BB6uGEw.jpeg)<br>

This was the first ER Diagram I made, it shows that one and only one user can add one or many players to their team created. The relationships are modeled incorrectly and the attributes do not portray what the application wants to do.

### 2nd ER-Diagram 

![ERD-2](https://imgur.com/eTk7zF6.jpeg)<br>

The image above shows the final draft of my ER diagram. I removed the user login page as it was not needed. The application models a one-to-many relationship between the Players and Teams entities. One team can have one or many players. 
<br>
<br>

## CI Pipeline


![CI-Pipe-line](https://imgur.com/f5l0gVq.jpeg)<br>

The above image illistrates how I implemented the continuous integration pipeline. This pipeline allows for software tools to handle the automated building, testing, and deployment proceses. 

### How the CI pipeline works
I create code on my local machine which is pushed up to a repository on GitHub, which, via a webhook, will trigger jenkins to start the build on the cloud server. At this point, tests will automatically run and test coverage reposts will be produced. This process is repeated  until there are no more errors. Once, all tests have been passed the app is made live through the cloud VM and ready to be used by the user.   


# Project Tracking
Trello, along with agile methodologies, was used to track the progression of the project and show my workflow, from start to finish. The link to the full trello board can be found [here](https://trello.com/b/MLnU7psY/agile-board).

![Trello-board](https://imgur.com/dAeNJvg.jpeg)
<br>

# Risk Assessment
Below is the risk assessment for the project split into two sections, before and after. The before section outlines the potential risks at that I knew at the start of the project. The after sections outlines the potentials risks that I knew by the end of the project. 

### Before
![Risk-assessment-1](https://imgur.com/JvamcBA.jpeg)
<br>

### After

![Risk-assessment-2](https://imgur.com/m0azlxz.jpeg)

# Testing

I used pytest to run unit tests on the app. These tests validate that each unit of the application performs as designed. Unit testing on my application came to 100% coverage, this is show below from the jenkins console output. If any tests do fail it will be shown here.
pytest has the ability to also produce a coverage report, by running:
```python
python3 -m pytest --cov=application --cov-report term-missing
```
The jenkins output below shows the coverage report produced. Furthermore, running the command above, also shows which parts of the application did not test. 

![pytest-jenkins](https://imgur.com/wJRxyIG.jpeg)

# Front-End Design 

The front-end design of the application is built using basic HTML. However, it is in a stable state that meets the MVP requirements. 

When the user launches app, the URL redirects them to  the home page:

![Home-Page](https://imgur.com/W4XYwbG.jpeg)

Navigating to the "create team" page allows the user to input a name and a spnosr of their choice for their team:

![Create-Team-Page](https://imgur.com/j30RRqE.jpeg)

Once the user has choosen their team name and sponsor they will be redirected to the homepage:

![Homepage](https://imgur.com/ci20SVR.jpeg)

An option of adding players is avaliable to the user, where they can add players to their team. A maximum of 5 players can be addeed to the team. After adding five players a message at the top appears, stating 'can only have five players in a team'. Another message is there which informs the user that if the club and height is not known then leave it blank:

![Add-players](https://imgur.com/47R5Xtp.jpeg)

After adding players to the team the user can return back to home page:

![Homepage](https://imgur.com/ci20SVR.jpeg)

Deleting the team returns you back to home page:

![Home-Page](https://imgur.com/W4XYwbG.jpeg)

# Further Improvements

There are a few number of improvements that i would like to implement:

* Use CSS to make the application look more asthetically pleasing.
* Add images of the players that are being added to the team.  
* Try an implemeent a delete function for removing players. 
* Make the application so that it prevents the user from selecting 2 players from the same club. 

# Authors 
Hitesh Patel
















