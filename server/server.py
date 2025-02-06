from flask import Flask, request, render_template_string

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])  
def login():
    message = None  
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'password':
            message = 'Login successful'
        else:
            message = 'Invalid credentials'
    
    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
