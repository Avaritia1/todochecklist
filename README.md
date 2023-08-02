# todochecklist
A simple HTTP API for a ToDo list management using Django and Bulma CSS. This API is primarily designed for managing a ToDo list. The user can add new tasks, mark tasks as complete or incomplete, and delete tasks.
## Front-end
For the frontend layout, I use Bulma's table format to arrange the rows and columns. This part uses Django's template system for the user interface, which means the interface can be easily extended or customized by editing HTML templates.
## Back-end
The API uses Django's built-in database models and forms, making it easier to handle data validation and storage.
## Features
(1) On this app, users can create to-dos, delete to-dos and mark them as completed or incomplete.    
(2) When a to-do is created or deleted, a success message banner for the operation is displayed on the screen to notify the user.  
(3) When a to-do is created, the creation date and time are saved. When the user marks it complete, the date and time it was marked complete will be saved. When an item is not marked complete, there is no completion date or time.  
(4) There is a deleted item list to record all deleted items and when they were deleted.   
(5) The user can also choose to perform a restore operation to restore deleted items to the Checklist.
## Steps
(1) Navigate into this folder and run the following command:
```
python manage.py runserver
```
(2) You can view it from the web browser on port 8000 (http://127.0.0.1:8000/).
## Test
I created unit tests to test related functionality such as home page view, deleting a task, restoring a deleted task, etc.   
Navigate into this folder and run the following command to run the tests:
```
python manage.py test
```
## 
![image](https://github.com/Avaritia1/todochecklist/assets/80332537/fc947085-7405-41c5-b696-77b4c41786ef)


