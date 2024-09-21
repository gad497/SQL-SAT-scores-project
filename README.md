This is project in python which uses MySQL database to store data of SAT scores of students and has following features:

- Must have a menu to select option from
1. Insert data
2. View all data
3. Get rank
4. Update score
5. Delete one record
6. Calculate Average SAT Score
7. Filter records by Pass/Fail Status.
8. Put the inserted data in json format in a file.

- Insert data - this needs to handle input data for the following Object and store in memory:
SAT Results
- Name (Unique Identifier)
- Address
- City
- Country
- Pincode
- SAT score
- Passed - this needs to be calculated in the backend as follows - if SAT score > 30% = Pass else Fail
- View all data - this should display all the data from the memory in Json format
- Get rank - this takes the name and returns their rank according to the data from the memory
- Update score - this allows to update SAT score for a candidate by name
- Delete one record - this deletes a record by name
- Calculates and displays the average SAT score of all candidates.
- Filters and displays records based on whether candidates passed or failed
