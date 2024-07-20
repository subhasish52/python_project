# run.py

from app import create_app
# Import the db object from the app package
from app import db

# Create the Flask application instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
