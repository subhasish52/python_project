import os  # Import the os module for interacting with the operating system

class Config:
    # Get the absolute path of the directory where this config file is located
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Define the URI for the SQLite database using the base directory path
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'employees.db')

    # Disable track modifications to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
