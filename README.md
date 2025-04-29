#  Task Management System


## Overview
My project is a tool for creating, updating, sorting, and searching a task management system.

## File Details
   ### Main File
   The file "project.py" contains one main function and four other functions called add_task, update_task, view_tasks, and search_tasks. The main function presents the user with a menu to choose what they want to do to the database or exist the program, then checks the input to match with one of the options and then based on the input, calls the option's function. The add function prompts the user for each input necessary to create a new row in the database and then adds that information to the database. The update function asks the user to choose how they would like to find the file they want to write over and then prompts the user for that specific identifier, finds the file, and prompts the user to input the information needed to update that row then adds that information to the database. The view function shows the user the full list of tasks and gives them the option to sort by title (a-z and z-a), date (ascending and descending numerically), and ID numerically. The search function allows the user to search by due_date, completion (yes or no), and ID.

   ### Supporting Files
   The file "tasks_db.py" contains the formatting for the tasks table in my database and creates the table when run.

   The file "tasks.db" contains my tasks database that is used throughout my project.py file.

   The file "test_project.py" contains many functions to test my project.py file. I primarily use patch so I can input multiple pieces of information into my project and then StringIO to gather my output. I use assert to compare my output to the expected output since I gave my user print statements along the way to ensure everything is running correctly.

## Design
I did debate with myself about using a csv file instead of a database, but I chose database because of the enforcement of data types and constraints. I know the csv might have been simpler to set up overall, but the challenge of the database seemed worthwhile in terms of learning and potential career development. I want to learn more about data analysis and data science, and  the more I can reinforce those concepts and work with data, the more prepared I should be in the future.

As I was writing my README.md file and describing the capabilities of the functions, I realized that I wanted my view to have a sorting option and for my add to check that there are no duplicate tasks existing based on title and ID.

## Challenges & Solutions
I initially set up my database with 2 tables, believing my categories should be wholly seperate from the rest of my information, but later found that to be an unnecessary step since I'd later have to join the tables anyway. I found that using DATETIME was also unncessary information for what I was trying to make happen so I went back and restructured my tasks table to include category and only use DATE, then recreated my database.

Working with testing the database was new because of all the inputs and outputs, potential errors, etc. I did get CS50's duck to help me figure that part out. I learned a lot in doing so about how I can use the decorator of patch to replace the input to create mock scenarios for my program and then capture the output with StringIO so I can later compare the output with the expected output using assert.





