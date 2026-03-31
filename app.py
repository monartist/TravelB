from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- ROUTES ---

@app.route('/')
def index():
    # This is the landing page
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to save user would go here
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Mock data for upcoming sessions
    events = [
        {'title': 'Morning Yoga', 'date': 'Oct 12', 'time': '8:00 AM'},
        {'title': 'Run Club', 'date': 'Oct 14', 'time': '6:00 PM'}
    ]
    return render_template('dashboard.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)