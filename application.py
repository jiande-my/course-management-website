# My own Library
from course import get_course_all, get_course_no_repeat, get_course_section, get_course_detail

# Library from Flask
from flask import Flask, render_template, request, redirect, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://mzqzzqbbqshuyu:8dac9f5ddbfbc9f7556554c9d4d7b101acc45c7b2d8bce1c9ae90931f464c22f@ec2-54-205-61-191.compute-1.amazonaws.com:5432/d55vjv88et7bmh"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.String(10), nullable=False, unique=True)
    phash = db.Column(db.String(120), nullable=False)

class registers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.String(10), nullable=False)
    courseID = db.Column(db.String(10), nullable=False)
    section = db.Column(db.Integer, nullable=False)

@app.route('/')
@app.route('/home')
def home():
    studentID = None
    course_registered = []
    if 'user' in session:
        studentID = session['user']

        user_course = registers.query.filter_by(studentID=studentID).all()
        for course in user_course:
            course_registered.append(get_course_detail(course.courseID, str(course.section)))

    return render_template('home.html', studentID=studentID, courses=course_registered)

@app.route('/course')
def course():
    list_courses = get_course_no_repeat()
    return render_template('course.html', courses=list_courses)

@app.route('/section')
def section():
    # Get Method
    courseID = request.args.get('courseID')
    section_list = get_course_section(courseID)
    
    return render_template('section.html', sections=section_list, courseID=courseID)

@app.route('/enrollment')
def enrollment():
    courseID = request.args.get('courseID')
    section = request.args.get('section')

    if not 'user' in session:
        flash("Please Login to Enrol in the Course!")
        return redirect(url_for('login'))

    studentID = session['user']
    course_registered = registers.query.filter_by(studentID=studentID).filter_by(courseID=courseID).first()

    if course_registered:
        flash(f"Error! {courseID} already registered!",)
        return redirect(url_for('course'))

    course = registers(studentID=studentID, courseID=courseID, section=section)
    db.session.add(course)
    db.session.commit()

    flash(f"{courseID} register successfully.", "register")
    return redirect(url_for('home'))

@app.route('/remove', methods=['GET', 'POST'])
def remove():
    studentID = None
    if 'user' in session:
        studentID = session['user']

    if request.method == "GET":
        user_courses = []
        db_user_courses = registers.query.filter_by(studentID=studentID).all()
        for course in db_user_courses:
            user_courses.append(course.courseID)
    
        return render_template('remove.html', courses=user_courses)
    
    else:
        courseID = request.form.get('course')
         
        course = registers.query.filter_by(studentID=studentID).filter_by(courseID=courseID).first()
        db.session.delete(course)
        db.session.commit()

        flash(f"{courseID} removed.", "remove")
        return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    else:
        studentID = request.form.get('inputStudentID')
        password = request.form.get('inputPassword')

        user_result = users.query.filter_by(studentID=studentID).first()

        if not user_result:
            flash('StudentID or Password incorrect!')
            return redirect(url_for('login'))

        elif check_password_hash(user_result.phash, password):
            session['user'] = studentID
            return redirect(url_for('home'))

        else:
            flash('StudentID or Password incorrect!')
            return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')

    else:
        studentID = request.form.get('inputStudentID')
        password = request.form.get('inputPassword')
        retype = request.form.get('inputRetype')
        phash = None

        if password == retype:
            phash = generate_password_hash(password)

            # Check student used or not
            user_result = users.query.filter_by(studentID=studentID).first()

            if user_result:
                flash("Student ID have been register! Please SignIn")
                return redirect(url_for('register'))

        elif len(studentID) > 9:
            flash("Student ID Invalid! Please try again.")
            return redirect(url_for('register'))

        else:
            flash("Password not same! Please try again.")
            return redirect(url_for('register'))

        # Create new user in database
        user = users(studentID = studentID, phash = phash)
        db.session.add(user)
        db.session.commit()
        
        # Update user in session
        session['user'] = studentID

        flash("Account Created", "register")
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))