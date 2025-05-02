1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.
Strategy:

The strategy was to implement a simple web application using Django, based on the provided data models for legislators, bills, and votes. The focus was to structure the code clearly to make it easy to understand and extend in the future.

Technologies used:

Django: Used to create the backend and render information on the frontend. Django was chosen for its robustness in building quick APIs (even though it is not applicable in this project, it allows scalability) and seamless integration with HTML templates.

Python: The main language used for efficiently handling CSV files and easy integration with Django.

HTML (with Django templates): Used to create tables displaying data on the web interface.

CSV: The input data is provided in CSV format, which is easily manipulated using Python to load data into the application.

Decisions:

Data Structure: The data structure was implemented to directly reflect the provided model, with classes such as Person (Legislator), Bill, Vote, and VoteResult. Each class represents an aspect of the data handled by the project.

CSV Reading: The csv library was used for reading the data. It is efficient and simple for manipulating CSV files.

Performance: Given the small volume of data (a limited number of legislators, bills, and votes), the solution provides adequate performance. Data retrieval is done sequentially, which is sufficient for this scenario.

Effort and Time Cost:
The majority of the time was spent on correct data modeling, CSV manipulation, and rendering the information in the interface. The problem complexity was relatively low, but it required attention to code structure and testing.

2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
Adapting for New Columns:

To handle future columns like "Bill Voted On Date" or "Co-Sponsors," the solution was designed to be flexible:

Modifying Classes: The model classes (Bill, Person, etc.) could be easily updated to include new attributes to store such data. For example, a voted_on_date field could be added to the Bill class, and a co_sponsors field could be added to store co-sponsors.

CSV Reading Adjustments: The CSV reading function could be easily adapted to handle new fields. Since the data is read as a dictionary, adding new columns wouldn't require significant changes to the code.

Frontend: On the frontend (HTML), new columns can be added to the tables, which can be done with minimal changes in the rendering code. This keeps the system scalable and easily extensible.

3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
Adapting to CSV Generation:

If the data were provided as lists of legislators or bills and the task was to generate CSVs instead of reading from CSVs, the changes would include:

CSV Generation Functions: Implementing functions that accept the lists of objects and convert them into CSV format. The Python csv library would be used to write data to CSV files.

For example, to generate the CSV for legislators, we would iterate over the list of legislators and write their data to the appropriate columns in the CSV.

The same approach would apply to generating CSVs for bills, votes, etc.

Data Structure Adaptation: The data structure of the classes would remain the same, but the main change would be in writing data back to files rather than reading them. The business logic and rendering in the interface would remain the same.

4. How long did you spend working on the assignment?

I spent approximately 2 to 3 hours in total working on this assignment. This includes reading and understanding the requirements, implementing the backend in Django, handling the CSV files, creating the frontend (HTML) for displaying data, and testing everything to ensure it was functioning correctly.