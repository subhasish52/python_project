from . import db

class Employee(db.Model):
    # Define the columns for the Employee table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String(64), nullable=False)  # Name column, cannot be null
    age = db.Column(db.Integer, nullable=False)  # Age column, cannot be null
    department = db.Column(db.String(64), nullable=False)  # Department column, cannot be null

    # Method to convert the employee object to a dictionary
    def to_dict(self):
        return {
            'id': self.id,  # Employee ID
            'name': self.name,  # Employee name
            'age': self.age,  # Employee age
            'department': self.department  # Employee department
        }
