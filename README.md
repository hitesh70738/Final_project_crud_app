CRUD application project:<br>

-Clean up trello board<br>
-Update ERD<br>
-Risk assessment<br>
-testing<br>
-jenkins<br>
-finish trello board<br> 

# Fantasy Football

# Project Brief 
The breif set for this project is to be able to create a CRUD application, with the tools, methodologies and technologies that cover all core modules covered during training.

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

![ERD-2](https://imgur.com/yijwL3Z.jpeg)<br>

The 2nd ER diagram shows the final draft of my ER diagram. I removed the user login page as it was not needed. The application models a one-to-many relationship between the Players and Teams entities. One team can have one or many players. This will allow the user to create a team with one or many players in that team.











