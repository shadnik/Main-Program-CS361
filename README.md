This project implements a microservice that allows users to perform the following tasks:
1.	Calculate the total weight moved for a workout session.
2.	Convert weights between pounds and kilograms.
3.	Track strength progress by comparing the current weight lifted to an initial weight.
   
How to Run the Microservice
Setup
1.	Clone the Repository: Download or clone the repository to your local machine.
2.	Install Dependencies: Install the required packages by running:
1.	Flask: pip install Flask
2.	requests: pip install requests
   
Running the Flask Server
Start the Flask microservice by executing the following command:
python Weight_Calculator.py
After running this command, you should see output indicating that the server is running on http://127.0.0.1:5000/.

Making Requests to the Microservice
Your program will need to make three requests to the microservice endpoints to interact with the available functionality. Below is a summary of how to interact with each endpoint programmatically:
1.	Calculate Total Weight:
o	Endpoint: POST /total-weight
o	Description: Send workout data (sets and reps) to calculate the total weight moved during a workout session.
o	Payload Example:
	[ {"reps": 7, "weight": 45}, {"reps": 10, "weight": 20}]
o	Response Example: {"total_weight": 515}
2.	Convert Weight:
o	Endpoint: GET /convert-weight
o	Description: Convert a given weight from one unit (e.g., lbs) to another (e.g., kg).
o	Query Parameters:
	weight: The weight to convert.
	to_unit: The unit to convert to (kg or lbs).
o	Response Example: {"converted_weight": 45.3592}
3.	Strength Progress:
o	Endpoint: GET /strength-progress
o	Description: Calculate the progress by comparing the current weight lifted to an initial weight.
o	Query Parameters:
	current_weight: The current weight being lifted.
	initial_weight: The initial weight lifted.
o	Response Example: {"weight_difference": 20}

Additional Information
•	Ensure that Weight_Calculator.py is running before attempting to execute the test requests.
•	HTTP Methods: Ensure you are using the correct HTTP method (POST or GET) for each endpoint.
•	Payload and Query Parameters: Follow the structure given in the examples to ensure that your requests are formatted correctly.
•	Each endpoint response is returned in JSON format.
Feel free to contact me if you have any questions regarding setup or testing.


![Microservice_A](https://github.com/user-attachments/assets/d77251df-6716-4291-8c39-64de18549c91)

