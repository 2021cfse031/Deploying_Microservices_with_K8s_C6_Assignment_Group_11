# Microservices_C4_Assignment_Group_9
This is GitHub repository of Microservices Assignment designed by Group 9

# Project Title 

# Microservices Application for fetching Student Details 

This project aims to develop microservices for student_score details using database per service design pattern.The data will be stored and retrieved from SQLite database in JSON format. The API is open to all the users who have access to the codebase.


# Technology Stack

This project uses Django to develop endpoints for students and their scores. It uses SQLite Database to store the data received from endpoints. 

## Project Screenshots


![student_domain_endpoints](https://user-images.githubusercontent.com/94062868/170861117-4e51ff94-e2bf-4355-8bd7-6a3711e53ffa.PNG)
![scores_domain_endpoints](https://user-images.githubusercontent.com/94062868/170861125-06ef4df2-e9a0-4f48-bfd9-5a3442248f17.PNG)
![all_details_endpoint](https://user-images.githubusercontent.com/94062868/170861129-32e45e42-fbd8-4a02-9a73-461348531d65.PNG)
![student_list](https://user-images.githubusercontent.com/94062868/170861089-6e851a7b-4851-4ee3-a064-210bb705e4ff.PNG)
![student_list_all](https://user-images.githubusercontent.com/94062868/170861091-19162ce8-374a-40b9-ac1c-caf927daaa75.PNG)
![student_list_success](https://user-images.githubusercontent.com/94062868/170861094-addf57de-db12-418c-aa5d-27467c381567.PNG)
![student_detail_view](https://user-images.githubusercontent.com/94062868/170861111-f16c0d27-1934-4360-ad04-458ab33aa4f6.PNG)
![scores_list](https://user-images.githubusercontent.com/94062868/170861157-960425ba-45ef-4be5-93bd-a5e99be87e3d.PNG)
![scores_lists_all](https://user-images.githubusercontent.com/94062868/170861159-f8c4bb6f-afc9-4ce0-ac89-e3f3f42be295.PNG)
![scores_filter](https://user-images.githubusercontent.com/94062868/170861179-742202a3-ff40-465c-820e-31eeb2607e83.PNG)
![scores_list_success](https://user-images.githubusercontent.com/94062868/170861158-ad5c8032-04f2-4181-8ef4-813b65361ce4.PNG)
![scores_detailed_view](https://user-images.githubusercontent.com/94062868/170861204-aa40c372-ed67-4558-aa7c-7d4652a3e8b0.PNG)
![all-details](https://user-images.githubusercontent.com/94062868/170861209-3ebaa8ce-0b90-4f2c-823f-2417557ac667.jpeg)

## Execution Instructions

Assuming Python and Django is already installed on your local machine, below are the execution instructions for the project;

1. Clone the repository: <br>
   The code is maintained in GitHub and can be pulled to our local machine using the below command. <br>
   <b><i>git clone https://github.com/2021cfse031/Microservices_C4_Assignment_Group_9.git</i></b>

2. Launch the application and navigate to endpoints: <br> 
   Each microservice will be running on a different server. The server’s here are isolated using different ports for respective microservices. <br>
   a. Student’s Domain is configured on port 7000 <br>
   b. Scores Domain is configured on port 8000 <br>
   c. All Details Domain is configured on port 9000 <br>

   To start the server navigate to manage.py file in project folders and execute the below command <br>
   <b><i>python manage.py runserver port_number</i></b>
