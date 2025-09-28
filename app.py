from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# --- Home Route (/) ---
@app.route('/')
def index():
    """Renders the main page with the form."""
    # Assuming 'index.html' contains the registration form
    return render_template('index.html')

# --- Form Handling Route (/submit) ---
@app.route('/submit', methods=['POST'])
def submit():
    """Handles the form submission."""
    if request.method == 'POST':
        # 1. Get data from the submitted form (using the 'name' attributes from the HTML form)
        username = request.form.get('username')
        email = request.form.get('email')
        
        # 2. Basic Server-side validation (optional, but recommended)
        if not username or not email:
            # Handle error, maybe flash a message, and redirect back to the form
            return redirect(url_for('index'))
        
        # 3. Connect to a database (e.g., SQLite) and store data
        # (Database connection/logic would go here)
        # Example: save_user_to_db(username, email)
        
        # 4. Redirect to the success page, passing the user's name as a variable
        return redirect(url_for('success', name=username))
    
    # If a GET request is made to /submit (shouldn't happen with standard form), redirect to home
    return redirect(url_for('index'))

# --- Success Route (/success) ---
@app.route('/success')
def success():
    """Renders the success page, showing confirmation."""
    # Get the 'name' variable passed from the 'submit' route
    user_name = request.args.get('name', 'User')
    
    # Render the template, passing the variable for Jinja2 to display
    return render_template('success.html', name=user_name)

# --- Run the application ---
if __name__ == '__main__':
    # Set debug=True for easier development
    app.run(debug=True)