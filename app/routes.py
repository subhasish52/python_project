from flask import jsonify, request, Blueprint
from .models import Employee
from . import db

# Create a Blueprint for employee routes
employee_bp = Blueprint('employee_bp', __name__)

# Route for the home page
@employee_bp.route('/')
def index():
    return "WELCOME TO EMPLOYEE MANAGEMENT SYSTEM"

# Route to create a new employee
@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'The request payload is not in JSON format'}), 415
    try:
        # Create a new Employee object
        new_employee = Employee(name=data['name'], age=data['age'], department=data['department'])
        db.session.add(new_employee)  # Add the employee to the database session
        db.session.commit()  # Commit the session to save the employee
        return jsonify({'message': 'Employee created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return an error message if an exception occurs

# Route to get all employees
@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()  # Query all employees from the database
        output = [employee.to_dict() for employee in employees]  # Convert each employee to a dictionary
        return jsonify({'employees': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message if an exception occurs

# Route to get a specific employee by ID
@employee_bp.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    try:
        employee = Employee.query.get_or_404(id)  # Query the employee by ID or return a 404 error if not found
        return jsonify(employee.to_dict())  # Convert the employee to a dictionary and return it
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message if an exception occurs

# Route to update a specific employee by ID
@employee_bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'The request payload is not in JSON format'}), 415
    try:
        employee = Employee.query.get_or_404(id)  # Query the employee by ID or return a 404 error if not found
        employee.name = data['name']
        employee.age = data['age']
        employee.department = data['department']
        db.session.commit()  # Commit the session to save the updates
        return jsonify({'message': 'Employee updated'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return an error message if an exception occurs

# Route to delete a specific employee by ID
@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        employee = Employee.query.get_or_404(id)  # Query the employee by ID or return a 404 error if not found
        db.session.delete(employee)  # Delete the employee from the database session
        db.session.commit()  # Commit the session to save the changes
        return jsonify({'message': 'Employee deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return an error message if an exception occurs
