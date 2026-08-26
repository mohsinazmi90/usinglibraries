# import os
# from flask import Flask, request, jsonify, render_template_string
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# app = Flask(__name__)

# # --- 1. DATABASE CONFIGURATION ---
# app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///advanced_demo.db'
# app.config['SQLAlchemy_TRACK_MODIFICATION'] = False
# db = SQLAlchemy(app)

# # --- 2. DATABASE MODELS ---
# class Project(db.model):
#     id = db.column(db.integer, primary_key = True)
#     title = db.column(db.string(100), nullable = False)
#     category = db.column(db.string(50), nullable = False)
#     status = db.column(db.string(20), default = 'Active')
#     created_at = db.column(db.DateTime(), default = datetime.utcnow())
    
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "category": self.category,
#             "status": self.status,
#             "created_at": self.created_at.strftime("%Y-%m-%d %H:%m:%s")
#         }
    
# # --- 3. INITIALIZE DATABASE WITH SEED DATA ---
# with app.app_context():
#     db.create_all()    
#     if not Project.query.first():
#         sample_projects = [
#             Project(title="AI Neural Core System", category="Machine Learning", status="Active"),
#             Project(title="Quantum Encryption Protocol", category="Cybersecurity", status="Pending"),
#             Project(title="High-Frequency Trading Bot", category="Fintech", status="Completed")
#         ]
        
#     db.session.add_all(sample_sample_projects if 'sample_sample_projects' in locals() else sample_projects)
#     db.session.commit()
    
# # 4. --- ADVANCED ANIMATED HTML/CSS/JS TEMPLATE ---
# pull_site_template = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <title>Python Web App</title>
#    <style>
#         /* --- ADVANCED CSS & ANIMATIONS --- */
#         :root {
#             --bg-gradient: linear-gradient(135deg, #0f172a, #1e1b4b, #311042);
#             --glass-bg: rgba(255, 255, 255, 0.05);
#             --glass-border: rgba(255, 255, 255, 0.12);
#             --accent-cyan: #06b6d4;
#             --accent-pink: #ec4899;
#             --text-main: #f8fafc;
#         }

#         * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        
#         body {
#             background: var(--bg-gradient);
#             background-size: 400% 400%;
#             animation: gradientBG 15s ease infinite;
#             color: var(--text-main);
#             min-height: 100vh;
#             overflow-x: hidden;
#             position: relative;
#         }

#         @keyframes gradientBG {
#             0% { background-position: 0% 50%; }
#             50% { background-position: 100% 50%; }
#             100% { background-position: 0% 50%; }
#         }

#         /* Floating Background Particles Canvas */
#         #particles-canvas {
#             position: fixed;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             pointer-events: none;
#             z-index: 0;
#         }

#         /* Layout Container */
#         .app-container {
#             position: relative;
#             z-index: 1;
#             max-width: 1100px;
#             margin: 0 auto;
#             padding: 40px 20px;
#         }

#         /* Animated Glassmorphism Header */
#         header {
#             background: var(--glass-bg);
#             backdrop-filter: blur(16px);
#             -webkit-backdrop-filter: blur(16px);
#             border: 1px solid var(--glass-border);
#             border-radius: 20px;
#             padding: 30px;
#             text-align: center;
#             box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
#             animation: slideDown 1s cubic-bezier(0.16, 1, 0.3, 1);
#             margin-bottom: 30px;
#         }

#         @keyframes slideDown {
#             from { transform: translateY(-50px); opacity: 0; }
#             to { transform: translateY(0); opacity: 1; }
#         }

#         header h1 {
#             font-size: 2.5rem;
#             background: linear-gradient(to right, var(--accent-cyan), var(--accent-pink));
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-bottom: 10px;
#         }

#         /* Grid Layout */
#         .content-grid {
#             display: grid;
#             grid-template-columns: 1fr 2fr;
#             gap: 25px;
#         }

#         @media (max-width: 768px) {
#             .content-grid { grid-template-columns: 1fr; }
#         }

#         /* Card Panels */
#         .panel {
#             background: var(--glass-bg);
#             backdrop-filter: blur(16px);
#             -webkit-backdrop-filter: blur(16px);
#             border: 1px solid var(--glass-border);
#             border-radius: 20px;
#             padding: 25px;
#             box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
#             animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) both;
#         }

#         @keyframes fadeInUp {
#             from { transform: translateY(40px); opacity: 0; }
#             to { transform: translateY(0); opacity: 1; }
#         }

#         /* Animated Input Form */
#         .form-group { margin-bottom: 20px; }
#         .form-group label { display: block; margin-bottom: 8px; font-size: 0.9rem; color: #cbd5e1; }
#         .form-control {
#             width: 100%;
#             padding: 12px 16px;
#             background: rgba(0, 0, 0, 0.2);
#             border: 1px solid var(--glass-border);
#             border-radius: 10px;
#             color: #fff;
#             outline: none;
#             transition: all 0.3s ease;
#         }
#         .form-control:focus {
#             border-color: var(--accent-cyan);
#             box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
#             transform: scale(1.02);
#         }

#         /* Animated Pulsing Button */
#         .btn-submit {
#             width: 100%;
#             padding: 14px;
#             border: none;
#             border-radius: 10px;
#             background: linear-gradient(45deg, var(--accent-cyan), var(--accent-pink));
#             color: white;
#             font-weight: bold;
#             font-size: 1rem;
#             cursor: pointer;
#             transition: all 0.3s ease;
#             box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);
#         }

#         .btn-submit:hover {
#             transform: translateY(-3px) scale(1.01);
#             box-shadow: 0 8px 25px rgba(236, 72, 153, 0.6);
#         }

#         /* Dynamic Database Items Container */
#         .project-card {
#             background: rgba(255, 255, 255, 0.03);
#             border: 1px solid var(--glass-border);
#             border-radius: 12px;
#             padding: 15px 20px;
#             margin-bottom: 15px;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
#             animation: popIn 0.5s ease-out;
#         }

#         @keyframes popIn {
#             0% { transform: scale(0.8); opacity: 0; }
#             100% { transform: scale(1); opacity: 1; }
#         }

#         .project-card:hover {
#             transform: translateX(10px) scale(1.02);
#             background: rgba(255, 255, 255, 0.08);
#             border-color: var(--accent-cyan);
#         }

#         .badge {
#             padding: 5px 10px;
#             border-radius: 20px;
#             font-size: 0.75rem;
#             text-transform: uppercase;
#             font-weight: bold;
#         }
#         .badge-active { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
#         .badge-pending { background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid #eab308; }
#         .badge-completed { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid #a855f7; }

#         .btn-delete {
#             background: transparent;
#             border: none;
#             color: #ef4444;
#             cursor: pointer;
#             font-size: 1.1rem;
#             transition: transform 0.2s;
#         }
#         .btn-delete:hover { transform: scale(1.3) rotate(90deg); }
#     </style>
# </head>
# <body>

#     <canvas id="particles-canvas"></canvas>

#     <div class="app-container">
#         <header>
#             <h1><i class="fa-solid fa-atom fa-spin"></i> Advanced Python Control Center</h1>
#             <p>Single-file full-stack demo with Flask, SQLite & dynamic CSS/JS animations</p>
#         </header>

#         <div class="content-grid">
#             <!-- Left Column: Add Data -->
#             <div class="panel" style="animation-delay: 0.2s;">
#                 <h2><i class="fa-solid fa-plus-circle"></i> Create Entry</h2>
#                 <hr style="border-color: var(--glass-border); margin: 15px 0;">
#                 <form id="projectForm">
#                     <div class="form-group">
#                         <label>Project Title</label>
#                         <input type="text" id="title" class="form-control" placeholder="e.g. Neural Pipeline" required>
#                     </div>
#                     <div class="form-group">
#                         <label>Category</label>
#                         <input type="text" id="category" class="form-control" placeholder="e.g. Data Science" required>
#                     </div>
#                     <div class="form-group">
#                         <label>Status</label>
#                         <select id="status" class="form-control">
#                             <option value="Active">Active</option>
#                             <option value="Pending">Pending</option>
#                             <option value="Completed">Completed</option>
#                         </select>
#                     </div>
#                     <button type="submit" class="btn-submit">
#                         <i class="fa-solid fa-bolt"></i> Push to SQLite
#                     </button>
#                 </form>
#             </div>

#             <!-- Right Column: Database Feed -->
#             <div class="panel" style="animation-delay: 0.4s;">
#                 <h2><i class="fa-solid fa-database"></i> Database Stream</h2>
#                 <hr style="border-color: var(--glass-border); margin: 15px 0;">
#                 <div id="projectList">
#                     <!-- Dynamic Items Appended Here via JS -->
#                 </div>
#             </div>
#         </div>
#     </div>

#     <!-- FRONTEND JAVASCRIPT ANIMATIONS & API INTERACTION -->
#     <script>
#         // --- 1. PARTICLES CANVAS ANIMATION ---
#         const canvas = document.getElementById('particles-canvas');
#         const ctx = canvas.getContext('2d');
#         let particles = [];

#         function resizeCanvas() {
#             canvas.width = window.innerWidth;
#             canvas.height = window.innerHeight;
#         }
#         window.addEventListener('resize', resizeCanvas);
#         resizeCanvas();

#         class Particle {
#             constructor() {
#                 this.x = Math.random() * canvas.width;
#                 this.y = Math.random() * canvas.height;
#                 this.size = Math.random() * 3 + 1;
#                 this.speedX = Math.random() * 1 - 0.5;
#                 this.speedY = Math.random() * 1 - 0.5;
#                 this.color = Math.random() > 0.5 ? 'rgba(6, 182, 212, 0.4)' : 'rgba(236, 72, 153, 0.4)';
#             }
#             update() {
#                 this.x += this.speedX;
#                 this.y += this.speedY;
#                 if (this.x > canvas.width) this.x = 0;
#                 if (this.x < 0) this.x = canvas.width;
#                 if (this.y > canvas.height) this.y = 0;
#                 if (this.y < 0) this.y = canvas.height;
#             }
#             draw() {
#                 ctx.fillStyle = this.color;
#                 ctx.beginPath();
#                 ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
#                 ctx.fill();
#             }
#         }

#         for (let i = 0; i < 70; i++) particles.push(new Particle());

#         function animateParticles() {
#             ctx.clearRect(0, 0, canvas.width, canvas.height);
#             particles.forEach(p => { p.update(); p.draw(); });
#             requestAnimationFrame(animateParticles);
#         }
#         animateParticles();

#         // --- 2. REST API INTERACTIONS (AJAX FETCH) ---
#         async function fetchProjects() {
#             const res = await fetch('/api/projects');
#             const data = await res.json();
#             const container = document.getElementById('projectList');
#             container.innerHTML = '';

#             data.forEach((item, index) => {
#                 const badgeClass = `badge-${item.status.toLowerCase()}`;
#                 const card = document.createElement('div');
#                 card.className = 'project-card';
#                 card.style.animationDelay = `${index * 0.1}s`;
#                 card.innerHTML = `
#                     <div>
#                         <h4 style="font-size: 1.1rem;">${item.title}</h4>
#                         <small style="color: #94a3b8;">${item.category} • ${item.created_at}</small>
#                     </div>
#                     <div style="display: flex; align-items: center; gap: 15px;">
#                         <span class="badge ${badgeClass}">${item.status}</span>
#                         <button class="btn-delete" onclick="deleteProject(${item.id})">
#                             <i class="fa-solid fa-trash-can"></i>
#                         </button>
#                     </div>
#                 `;
#                 container.appendChild(card);
#             });
#         }

#         // Handle Form Submission
#         document.getElementById('projectForm').addEventListener('submit', async (e) => {
#             e.preventDefault();
#             const payload = {
#                 title: document.getElementById('title').value,
#                 category: document.getElementById('category').value,
#                 status: document.getElementById('status').value
#             };

#             await fetch('/api/projects', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify(payload)
#             });

#             document.getElementById('title').value = '';
#             document.getElementById('category').value = '';
#             fetchProjects();
#         });

#         // Handle Delete Action
#         async function deleteProject(id) {
#             await fetch(`/api/projects/${id}`, { method: 'DELETE' });
#             fetchProjects();
#         }

#         // Initial Load
#         fetchProjects();
#     </script>
# </body>
# </html>
# """

# # --- 5. BACKEND API ROUTES ---
# @app.route("/")
# def index():
#     return render_template_string(pull_site_template)

# @app.route("/api/projects", methods=["GET"])

# def get_projects():
#     projects = Project.query.order_by(Project.id.desc().all())
#     return jsonify([p.to_dict() for p in projects])

# @app.route("/api/projects", methods=["POST"])

# def add_project():
#     data = request.json
#     new_project = Project(title = data.get("title"),
#                           category = data.get('category'),
#                           status = data.get("status"),
#                           )
#     db.session.add(new_project)
#     db.session.commit()
#     return jsonify(new_project.to_dict()), 201

# @app.route("/api/projects/<int:project_id>", methods=["DELETE"])

# def delete_project(project_id):
#     project = Project.query.get_or_404(project_id)
#     db.session.delete(project)
#     db.session.commit()
#     return jsonify({"Success": True})

# if __name__ == "__main__":
#     app.run(debug=True)

import os
from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advanced_demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- DATABASE MODELS ---
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
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

# Initialize Database with Seed Data
with app.app_context():
    db.create_all() 
    if not Project.query.first():
        sample_projects = [
            Project(title="AI Neural Core System", category="Machine Learning", status="Active"),
            Project(title="Quantum Encryption Protocol", category="Cybersecurity", status="Pending"),
            Project(title="High-Frequency Trading Bot", category="Fintech", status="Completed")
        ]
        db.session.add_all(sample_projects)
        db.session.commit()

# --- ADVANCED ANIMATED HTML/CSS/JS TEMPLATE ---
FULL_SITE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Advanced Animated Python Web App</title>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        /* --- ADVANCED CSS & ANIMATIONS --- */
        :root {
            --bg-gradient: linear-gradient(135deg, #0f172a, #1e1b4b, #311042);
            --glass-bg: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.12);
            --accent-cyan: #06b6d4;
            --accent-pink: #ec4899;
            --text-main: #f8fafc;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        
        body {
            background: var(--bg-gradient);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: var(--text-main);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Floating Background Particles Canvas */
        #particles-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }

        /* Layout Container */
        .app-container {
            position: relative;
            z-index: 1;
            max-width: 1100px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        /* Animated Glassmorphism Header */
        header {
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            animation: slideDown 1s cubic-bezier(0.16, 1, 0.3, 1);
            margin-bottom: 30px;
        }

        @keyframes slideDown {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        header h1 {
            font-size: 2.5rem;
            background: linear-gradient(to right, var(--accent-cyan), var(--accent-pink));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        /* Grid Layout */
        .content-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 25px;
        }

        @media (max-width: 768px) {
            .content-grid { grid-template-columns: 1fr; }
        }

        /* Card Panels */
        .panel {
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        @keyframes fadeInUp {
            from { transform: translateY(40px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        /* Animated Input Form */
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-size: 0.9rem; color: #cbd5e1; }
        .form-control {
            width: 100%;
            padding: 12px 16px;
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid var(--glass-border);
            border-radius: 10px;
            color: #fff;
            outline: none;
            transition: all 0.3s ease;
        }
        .form-control:focus {
            border-color: var(--accent-cyan);
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
            transform: scale(1.02);
        }
        .form-control option {
            background-color: #1e1b4b;
            color: #fff;
        }

        /* Animated Pulsing Button */
        .btn-submit {
            width: 100%;
            padding: 14px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(45deg, var(--accent-cyan), var(--accent-pink));
            color: white;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);
        }

        .btn-submit:hover {
            transform: translateY(-3px) scale(1.01);
            box-shadow: 0 8px 25px rgba(236, 72, 153, 0.6);
        }

        /* Dynamic Database Items Container */
        .project-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 15px 20px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: popIn 0.5s ease-out;
        }

        @keyframes popIn {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

        .project-card:hover {
            transform: translateX(10px) scale(1.02);
            background: rgba(255, 255, 255, 0.08);
            border-color: var(--accent-cyan);
        }

        .badge {
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: bold;
        }
        .badge-active { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
        .badge-pending { background: rgba(234, 179, 8, 0.2); color: #fde047; border: 1px solid #eab308; }
        .badge-completed { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid #a855f7; }

        .btn-delete {
            background: transparent;
            border: none;
            color: #ef4444;
            cursor: pointer;
            font-size: 1.1rem;
            transition: transform 0.2s;
        }
        .btn-delete:hover { transform: scale(1.3) rotate(90deg); }
    </style>
</head>
<body>

    <canvas id="particles-canvas"></canvas>

    <div class="app-container">
        <header>
            <h1><i class="fa-solid fa-atom fa-spin"></i> Advanced Python Control Center</h1>
            <p>Single-file full-stack demo with Flask, SQLite & dynamic CSS/JS animations</p>
        </header>

        <div class="content-grid">
            <!-- Left Column: Add Data -->
            <div class="panel" style="animation-delay: 0.2s;">
                <h2><i class="fa-solid fa-plus-circle"></i> Create Entry</h2>
                <hr style="border-color: var(--glass-border); margin: 15px 0;">
                <form id="projectForm">
                    <div class="form-group">
                        <label>Project Title</label>
                        <input type="text" id="title" class="form-control" placeholder="e.g. Neural Pipeline" required>
                    </div>
                    <div class="form-group">
                        <label>Category</label>
                        <input type="text" id="category" class="form-control" placeholder="e.g. Data Science" required>
                    </div>
                    <div class="form-group">
                        <label>Status</label>
                        <select id="status" class="form-control">
                            <option value="Active">Active</option>
                            <option value="Pending">Pending</option>
                            <option value="Completed">Completed</option>
                        </select>
                    </div>
                    <button type="submit" class="btn-submit">
                        <i class="fa-solid fa-bolt"></i> Push to SQLite
                    </button>
                </form>
            </div>

            <!-- Right Column: Database Feed -->
            <div class="panel" style="animation-delay: 0.4s;">
                <h2><i class="fa-solid fa-database"></i> Database Stream</h2>
                <hr style="border-color: var(--glass-border); margin: 15px 0;">
                <div id="projectList">
                    <!-- Dynamic Items Appended Here via JS -->
                </div>
            </div>
        </div>
    </div>

    <!-- FRONTEND JAVASCRIPT ANIMATIONS & API INTERACTION -->
    <script>
        // --- 1. PARTICLES CANVAS ANIMATION ---
        const canvas = document.getElementById('particles-canvas');
        const ctx = canvas.getContext('2d');
        let particles = [];

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 3 + 1;
                this.speedX = Math.random() * 1 - 0.5;
                this.speedY = Math.random() * 1 - 0.5;
                this.color = Math.random() > 0.5 ? 'rgba(6, 182, 212, 0.4)' : 'rgba(236, 72, 153, 0.4)';
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.x > canvas.width) this.x = 0;
                if (this.x < 0) this.x = canvas.width;
                if (this.y > canvas.height) this.y = 0;
                if (this.y < 0) this.y = canvas.height;
            }
            draw() {
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        for (let i = 0; i < 70; i++) particles.push(new Particle());

        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => { p.update(); p.draw(); });
            requestAnimationFrame(animateParticles);
        }
        animateParticles();

        // --- 2. REST API INTERACTIONS (AJAX FETCH) ---
        async function fetchProjects() {
            try {
                const res = await fetch('/api/projects');
                const data = await res.json();
                const container = document.getElementById('projectList');
                container.innerHTML = '';

                if (!data || data.length === 0) {
                    container.innerHTML = '<p style="color: #94a3b8; text-align: center;">No projects found.</p>';
                    return;
                }

                data.forEach((item, index) => {
                    const statusStr = (item.status || 'Active').toLowerCase();
                    const badgeClass = `badge-${statusStr}`;
                    
                    const card = document.createElement('div');
                    card.className = 'project-card';
                    card.style.animationDelay = `${index * 0.1}s`;
                    card.innerHTML = `
                        <div>
                            <h4 style="font-size: 1.1rem; color: #fff;">${item.title}</h4>
                            <small style="color: #94a3b8;">${item.category} • ${item.created_at}</small>
                        </div>
                        <div style="display: flex; align-items: center; gap: 15px;">
                            <span class="badge ${badgeClass}">${item.status}</span>
                            <button class="btn-delete" onclick="deleteProject(${item.id})">
                                <i class="fa-solid fa-trash-can"></i>
                            </button>
                        </div>
                    `;
                    container.appendChild(card);
                });
            } catch (err) {
                console.error("Error fetching projects:", err);
            }
        }

        // Handle Form Submission
        document.getElementById('projectForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const payload = {
                title: document.getElementById('title').value,
                category: document.getElementById('category').value,
                status: document.getElementById('status').value
            };

            try {
                const res = await fetch('/api/projects', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (res.ok) {
                    document.getElementById('title').value = '';
                    document.getElementById('category').value = '';
                    await fetchProjects();
                } else {
                    console.error("Failed to add project:", await res.text());
                }
            } catch (err) {
                console.error("Error posting project:", err);
            }
        });

        // Handle Delete Action
        async function deleteProject(id) {
            try {
                const res = await fetch(`/api/projects/${id}`, { method: 'DELETE' });
                if (res.ok) {
                    await fetchProjects();
                }
            } catch (err) {
                console.error("Error deleting project:", err);
            }
        }

        // Initial Load
        fetchProjects();
    </script>
</body>
</html>
"""

# --- BACKEND API ROUTES ---
@app.route("/")
def index():
    return render_template_string(FULL_SITE_TEMPLATE)

@app.route("/api/projects", methods=["GET"])
def get_projects():
    projects = Project.query.order_by(Project.id.desc()).all()
    return jsonify([p.to_dict() for p in projects])

@app.route("/api/projects", methods=["POST"])
def add_project():
    data = request.json or {}
    new_project = Project(
        title=data.get("title"),
        category=data.get("category"),
        status=data.get("status", "Active")
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.to_dict()), 201

@app.route("/api/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True, port=8080)