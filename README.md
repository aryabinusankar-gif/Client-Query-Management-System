##############################################################################################

            # Client Query Management System

##############################################################################################

This project is a complete web-based application built using the Streamlit framework for UI,
SQLite for database management, and Pandas for handling data efficiently.
It demonstrates the end-to-end workflow of designing a simple yet powerful client query submission and support system.

Below, I have explained the step-by-step flow—starting from how the database is created,
to how the user interacts with the system as a Client or Support Agent.

This project includes the following major stages:

    1. Database & Tables Creation
    2. Main Page Development
    3. Login & Registration Logic
    4. Client Page Functionality
    5. Support Dashboard Creation

Steps to Developing the Client Query Management System

==============================================================

Preparation of the Virtual Environment

Install Python (version compatible with Streamlit and SQLite).

Install all required packages (Streamlit, Pandas, SQLite, etc.).

Activate your virtual environment and begin the project setup.

Step I: Database & Table Creation

In this project, we begin by creating a SQLite database along with two essential tables:

users

queries

The schema for both tables is defined clearly inside the schema.sql file.

The file init_db.py is used to initialize the database by executing the schema.

After running the script, the project automatically creates the required database structure.

This ensures all future operations like registration, login, and query submission work smoothly.

Step II: Main Page Creation

The main page is built using Streamlit.

Page configuration is set to provide a clean, wide layout for better user experience.

A sidebar menu is created containing:

Home

Register

Login

The user can register as either Client or Support Agent.

After login, the system automatically redirects the user to their respective dashboards.

Step III: Login & Authentication Logic

The login logic includes database validation and password verification.

Passwords are securely hashed using the helper functions (hash_password, verify) from auth.py.

Functions like register_user and get_user_by_username manage user data in the database.

On successful login, the user session is stored, enabling dynamic page switching.

Step IV: Client Page Functionality

The client interface is built using Streamlit components like text inputs and forms.

Clients can submit a new query by providing:

Query Title

Description

A unique Query ID (Example: CQ-20240102123456) is automatically generated using UTC timestamp logic.

Submitted queries are stored in the queries table along with:

User ID

Status (open by default)

Creation timestamp

Clients receive a confirmation message upon successful submission.

Step V: Support Page (Dashboard)

The support dashboard enables support agents to manage all queries.

Libraries used:

Streamlit

Pandas

SQLite3

Datetime

A complete table of all queries is displayed for quick reference.

Support agents can:

View all queries

Filter based on status (open / closed)

Close a query by entering its Query ID

Closing a query updates the database with the current UTC timestamp.

The dashboard provides a clean and structured overview, helping support teams stay organized.

**Thus, the Client Query Management System project is completed successfully!

Thank you for exploring this project.**
