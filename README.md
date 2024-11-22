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
Test Program: Making Requests
Your test program will need to make three requests to the microservice:
1.	Calculate Total Weight: Sends a POST request to /total-weight with workout data.
2.	Convert Weight: Sends a GET request to /convert-weight to convert lbs to kilograms.
3.	Strength Progress: Sends a GET request to /strength-progress to calculate the difference between the current and initial weight lifted.
Example API Calls
1. Total Weight Calculation
•	Endpoint: POST /total-weight
•	Payload:
•	[
•	  {"reps": 7, "weight": 45},
•	  {"reps": 10, "weight": 20}
]
•	Response:
{"total_weight": 515}
2. Weight Conversion
•	Endpoint: GET /convert-weight
•	Query Parameters:
o	weight: 100
o	to_unit: kg
•	Response:
{"converted_weight": 45.3592}
3. Strength Progress
•	Endpoint: GET /strength-progress
•	Query Parameters:
o	current_weight: 120
o	initial_weight: 100
•	Response:
{"weight_difference": 20}

Additional Information
•	Ensure that Weight_Calculator.py is running before attempting to execute the test requests.
•	Each endpoint response is returned in JSON format, which makes it easy for clients to consume.
Feel free to contact me if you have any questions regarding setup or testing.

![Microservice_A](https://github.com/user-attachments/assets/d77251df-6716-4291-8c39-64de18549c91)

