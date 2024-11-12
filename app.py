from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "project.db")}'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    userID = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {[self.userID, self.password, self.role]}>'

class Project(db.Model):
    ID = db.Column(db.String(50), primary_key=True)
    Name = db.Column(db.String(100))
    SDate = db.Column(db.Date)
    EDate = db.Column(db.Date)
    Budget = db.Column(db.Integer)
    CID = db.Column(db.String(50), primary_key=True)
    State = db.Column(db.String(100))
    District = db.Column(db.String(100))
    CityTown = db.Column(db.String(100))
    Pincode = db.Column(db.String(100))
    Status = db.Column(db.String(100))
    Details = db.Column(db.String(1000))

    
    def __repr__(self): 
        return (f'<Project ID: {self.ID}, Name: {self.Name}, SDate: {self.SDate}, ' f'EDate: {self.EDate}, Budget: {self.Budget}, CID: {self.CID}, ' f'State: {self.State}, District: {self.District}, CityTown: {self.CityTown}, ' f'Pincode: {self.Pincode}, Status: {self.Status}, Details: {self.Details}>')

class ProjectEstimation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(50))
    contractor_id = db.Column(db.String(50))
    estimation_cost = db.Column(db.Integer)

    def __repr__(self):
        return f"<ProjectEstimation {self.project_id}, Contractor: {self.contractor_id}, Estimation Cost: {self.estimation_cost}>"


# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userId']
        password = request.form['password']
        user_role = request.form['userRole']

        # Query the database to find the user
        user = User.query.filter_by(userID=user_id, password=password, role=user_role).first()
        
        if user:
            # Redirect to role-specific actions page based on user role
            if user.role == 'Department Representative':
                return redirect(url_for('department_representative_actions'))
            elif user.role == 'Contractor':
                return redirect(url_for('contractor_actions'))
            elif user.role == 'Admin':
                return redirect(url_for('admin_actions'))
        else:
            # Flash an error message if user is not found
            flash('User does not exist, please check your credentials.')
            return redirect(url_for('login'))
    
    return render_template('index.html')

@app.route('/contractor/add_estimation', methods=['GET', 'POST'])
def add_project_estimation():
    if request.method == 'POST':
        project_id = request.form['projectID']
        contractor_id = request.form['contractorID']
        estimation_cost = int(request.form['estimationCost'])

        # Create a new ProjectEstimation object
        new_estimation = ProjectEstimation(
            project_id=project_id,
            contractor_id=contractor_id,
            estimation_cost=estimation_cost
        )

        # Add the estimation to the database
        try:
            db.session.add(new_estimation)
            db.session.commit()
            flash("Estimation added successfully!", "success")
        except Exception as e:
            flash("An error occurred. Please try again.", "error")
            db.session.rollback()

        return redirect(url_for('contractor_actions'))

    return render_template('add_estimation.html')


# Role-specific action pages
@app.route('/department_representative/actions')
def department_representative_actions():
    print('render')
    return render_template('drActions.html')

@app.route('/contractor/actions')
def contractor_actions():
    return render_template('cActions.html')

@app.route('/admin/actions')
def admin_actions():
    return render_template('aActions.html')

# Route for updating project status
@app.route('/contractor/update_project_status', methods=['GET', 'POST'])
def update_project_status():
    if request.method == 'POST':
        # Here you can retrieve the form data and handle it if needed
        project_id = request.form['projectID']
        contractor_id = request.form['contractorID']
        stage = request.form['stage']
        
        # Process the data, e.g., save the stage update to the database if needed
        flash(f"Project status has been updated to {stage} successfully!", "success")
        
        # Redirect back to contractor actions or other page if needed
        return redirect(url_for('contractor_actions'))

    # Render the update_project_status form
    return render_template('update_project_status.html')

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    print("Requested add", request.method)
    if request.method == 'POST':
        try:
            print('HIOuhscka,', request.form)
            # Retrieve form data with exact keys as in the HTML form
            project_id = request.form['projectID']
            name = request.form['projectName']
            s_date = request.form['sDate']
            e_date = request.form['eDate']
            budget = request.form['budget']
            cid = request.form['cid']
            state = request.form['state']
            district = request.form['district']
            city_town = request.form['cityTown']
            pincode = request.form['pincode']
            status = request.form['status']
            details = request.form['details']
            
            # Log retrieved data for debugging
            print("Form Data Retrieved:", project_id, name, s_date, e_date, budget, cid, state, district, city_town, pincode, status, details)
            
            # Create a new Project object with the form data
            new_project = Project(
                ID=project_id,
                Name=name,
                SDate=s_date,
                EDate=e_date,
                Budget=budget,
                CID=cid,
                State=state,
                District=district,
                CityTown=city_town,
                Pincode=pincode,
                Status=status,
                Details=details
            )
            
            # Add the new project to the database
            db.session.add(new_project)
            db.session.commit()
            
            # Flash a success message and redirect
            flash('Project added successfully OK! I')
            return redirect(url_for('department_representative_actions'))  # Or another relevant page

        except Exception as e:
            # Print exception for debugging
            print("An error occurred while adding the project:", str(e))
            flash('An error occurred. Please try again.')
            return redirect(url_for('add_project'))
    
    return render_template('add_project.html')

@app.route('/view_projects')
def view_projects():
    projects = Project.query.all()  # Retrieve all projects from the database
    return render_template('viewProjects.html', projects=projects)

@app.route('/approve_forum')
def approve_forum():
    return render_template('approveForum.html')

if __name__ == '__main__':
    app.run(debug=True)
