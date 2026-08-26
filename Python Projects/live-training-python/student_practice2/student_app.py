import os 
from flask import Flask, jsonify, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# ---- DATABASE CONFIGURATION ----
app.config["SQLAlchemy_DATABASE_URI"] = "sqlite:///advanced_demo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ---- DATABASE MODEL ----
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default="Active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "status": self.status,
            "created_at": self.created_at
        }
        
with app.app_context():
    db.create_all()
    if not Project.query.first():
        sample_project = [
            Project(title="AI Neural Core System", category="Machine Learning", status="Active"),
            Project(title="Quantum Encryption Protocol", category="Cybersecurity", status="Pending"),
            Project(title="High-Frequency Trading Bot", category="Fintech", status="Completed")
        ]
        db.session.add_all(sample_project)
        db.session.commit()
