# Create a Patient Management Application using the following mandatory requirements -
1. List the patients on a FHIR server, displaying their name, gender and date of birth
2. Create patients by submitting a form with the patient's name, gender, date of birth and phone number. Proper validation needs to be done on all fields.
3. Allow update of all patients who are on the FHIR server by opening them on the same form and updating details.
4. Search patients by their name or phone number.

# Tools to use
1. HTML+ CSS + JavaScript
2. FHIR server (hapi.fhir.org)

# Instructions
Create a patient management application using the above tools and requirements.
- Portal with a welcome/landing page - branding of a clinic named "HealthPlus" using clean and modern design theme using white and olive green colors.
- The web page should have a navigation bar with the following options:
    - Home
    - Patient Search bar and next to it a button to search (olive green color, rounded corners, text in white color).
        - Search by name (Last Name or First Name)
        - Search by phone number
        - Display search results in a table with the following columns:
            - Name
            - Gender
            - Date of Birth
            - Phone Number
            - Last Updated Date and Time
            - Reason for Visit
            - Next Appointment Date and Time if scheduled or "No Appointment" if not scheduled.
            - The results are displayed [10, 50, 100] options with dropdown to select the number of results to display at a time with pagination controls with click options to navigate through the results. Diplay page number and total number of pages.
    - Below the Patient Search bar, there should be a button to Create a new patient (olive green color, rounded corners, text in white color).
    - When you click the Search button, the list of patients should be updated to show the search results.
    - Below the Create Patient and Update Patient buttons, there should be a list of all patients.
        - The application should be able to display the patient's name, gender and date of birth, last updated date and time, Reason for Visit, Next Appointment Date and Time if scheduled or "No Appointment" if not scheduled.
    - There should be an option to select one or more patients from the list to update or delete with checkbox in the first column of the table. Option to select all patients should be available to update or delete selected patients.
    - When you click the Create Patient button, a form should open to create a new patient.
    - When you click the Update Patient button, a form should open to update the selected patient.
        - The form should have the following fields:
            - First Name
            - Last Name
            - Gender
            - Date of Birth
            - Phone Number
            - Address including street, city, state, zip code.
            - List of all visits with date and time and reason for visit and brief notes 
- See the UI design in the website link for reference - https://medduties.com/
