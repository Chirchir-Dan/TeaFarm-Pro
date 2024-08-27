from app import db

class Farmer(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    employees = db.relationship('Employee', backref='farmer', lazy=True)
    tasks = db.relationship('Task', backref='farmer', lazy=True)
    productions = db.relationship('Production', backref='farmer', lazy=True)
    costs = db.relationship('Cost', backref='farmer', lazy=True)
    metrics = db.relationship('Metric', backref='farmer', lazy=True)
    reports = db.relationship('Report', backref='farmer', lazy=True)

class Employee(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # role = db.Column(db.String(50), nullable=False)
    farmer_id = db.Column(db.String(32), db.ForeignKey('farmer.id'), nullable=False)
    tasks = db.relationship('Task', backref='employee', lazy=True)
    productions = db.relationship('Production', backref='employee', lazy=True)

class Task(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    employee_id = db.Column(db.String(32), db.ForeignKey('employee.id'), nullable=False)
    farmer_id = db.Column(db.String(32), db.ForeignKey('farmer.id'), nullable=False)

class Production(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    section = db.Column(db.String(50), nullable=True)
    employee_id = db.Column(db.String(32), db.ForeignKey('employee.id'), nullable=False)
    farmer_id = db.Column(db.String(32), db.ForeignKey('farmer.id'), nullable=False)

class Cost(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    section = db.Column(db.String(50), nullable=True)
    farmer_id = db.Column(db.String(32), db.ForeignKey('farmer.id'), nullable=False)

    """class Metric(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    period = db.Column(db.String(50), nullable=False)
    farmer_id = db.Column(db.String(32), db.ForeignKey('farmer.id'), nullable=False) """
"""
This shall be implemented as a future module  and perhaps it wont be necessary
to have it as a model on its own.

class Report(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)
    generated_at = db.Column(db.DateTime, nullable=False)
    data = db.Column(db.Text)
    farmer_id = db.Column(db.String(32), db.ForeignKey('farmer.id'), nullable=False) """
