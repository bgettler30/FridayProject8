# FridayProject8
This project is a simple customer feedback application that combines a database with a graphical user interface (GUI). It allows customers to submit their name, email, and feedback, which is then stored in a local SQLite database. Additionally, users can retrieve all feedback entries in a password-protected manner.

Project Features
Feedback Submission: Customers can enter their name, email, and feedback message.
Data Storage: All feedback entries are stored in a local SQLite database (feedback.db).
Password-Protected Data Retrieval: Users can retrieve all stored feedback entries by entering a password. Only users with the correct password can access this data.

Python 3.x is required.
The following libraries are used and should be available with Python:
sqlite3
tkinter

Usage:

Submit Feedback:

Enter the Name, Email, and Feedback message in the respective fields.
Click Submit to save the feedback to the database.
Retrieve Data:

Click the Retrieve Data button to view all feedback entries.
You will be prompted to enter a password.

The password to retrieve feedback data is: password

The application saves all data in a local database file named feedback.db.
If you need to clear feedback entries, you can manually delete feedback.db (a new one will be created when you next run the program).