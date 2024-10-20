from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messaging

# Simulating a database with a dictionary
users = {}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['userId']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if user_id in users:
            flash('User ID already exists. Please choose another one.')
        elif password != confirm_password:
            flash('Passwords do not match.')
        else:
            users[user_id] = password
            flash('Registration successful! Please log in.')
            return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['userId']
    password = request.form['password']

    if user_id in users and users[user_id] == password:
        return f"Welcome, {user_id}!"
    else:
        flash('Invalid User ID or Password.')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

