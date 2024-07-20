# app/routes.py

from flask import jsonify, request, Blueprint
from .models import Employee
from . import db
from .schemas import EmployeeSchema

employee_bp = Blueprint('employee_bp', __name__)
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

@employee_bp.route('/')
def index():
    return "WELCOME TO EMPLOYEE MANAGEMENT SYSTEM"

@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'The request payload is not in JSON format'}), 415
    try:
        # Deserialize and validate the input data
        new_employee = employee_schema.load(data, session=db.session)
        db.session.add(new_employee)
        db.session.commit()
        return employee_schema.jsonify(new_employee), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()
        return employees_schema.jsonify(employees)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@employee_bp.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    try:
        employee = Employee.query.get_or_404(id)
        return employee_schema.jsonify(employee)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@employee_bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'The request payload is not in JSON format'}), 415
    try:
        employee = Employee.query.get_or_404(id)
        # Update fields using the schema
        employee = employee_schema.load(data, instance=employee, session=db.session)
        db.session.commit()
        return employee_schema.jsonify(employee)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
