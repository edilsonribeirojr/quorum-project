# Quorum Coding Challenge

## Overview
This is a Django web application that processes legislative data to answer the following questions:
1. For each legislator, how many bills did they support or oppose?
2. For each bill, how many legislators supported or opposed it? Who was the primary sponsor?

## Requirements
- Python 3.8 or higher
- Django 3.2

## Installation

1. Clone the repository:

   git clone https://github.com/edilsonribeirojr/quorum-project.git
   cd quorum-project

2. Create and activate a virtual environment:

   python -m venv venv
   venv\Scripts\activate  # on Windows
   source venv/bin/activate  # on Mac/Linux

3. Install the requirements dependencies:

   pip install -r requirements.txt

4. Run the development server:

   python manage.py runserver

5. Visit http://127.0.0.1:8000/dashboard/ to see the dashboard with legislator and bill information.

How to run the project
This project loads data from CSV files (bills.csv, legislators.csv, votes.csv, and vote_results.csv) and processes it to show the required statistics on a dashboard page. Ensure that the CSV files are located in the data/ folder.

Project Structure
core/: Contains the main logic for handling the CSV files, counting votes, and rendering the dashboard view.

templates/: Contains the dashboard.html template used to render the data.

Notes
All data is loaded from the provided CSV files.

This project doesn't use a traditional database as it was designed to only process CSV files.

Future Enhancements
Add additional features to allow filtering by legislator or bill.

Provide more advanced visualizations (charts, graphs) for the statistics.

License
This project is open-source and available under the MIT License.
   