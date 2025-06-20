from flask import Flask, request

app = Flask(__name__) #start aplikasi selalu flask

@app.route('/')
def form(): #tampilan utama website
    return '''
        <html>
        <head>
            <title>Register</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #414a4c;
                    padding: 50px;
                    text-align: center;
                }
                h2 {
                    color: #0e1111;
                }
                p {
                    color: #232b2b;
                }
                form {
                    background-color: #3b444b;
                    padding: 20px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 2px 5px #232b2b;
                    text-align: left;
                }
                input[type=text], input[type=number] {
                    width: 100%;
                    padding: 8px;
                    margin: 8px 0;
                    box-sizing: border-box;
                }
                input[type=submit] {
                    background-color: #4CAF50;
                    color: #F9F6EE;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type=submit]:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h2>Register Your Account</h2>
            <form action="/biodata" method="post">
                <p>Email: <input type="text" name="email"></p>
                <p>Username: <input type="text" name="username"></p>
                <p>Password: <input type="text" name="password"></p>
                <p>Confirm Password: <input type="text" name="confirm_password"></p>
                <input type="submit" value="Kirim">
            </form>
        </body>
        </html>
    '''

@app.route('/biodata', methods=['POST'])
def biodata():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    return f'''
        <html>
        <head>
            <title>Hasil Biodata</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 50px;
                    text-align: center;
                }}
                h2 {{
                    color: #333;
                }}
                .card {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    display: inline-block;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
                    text-align: left;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #4CAF50;
                }}
            </style>
        </head>
        <body>
            <h2>Hasil Biodata</h2>
            <div class="card">
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Username:</strong> {username}</p>
                <p><strong>Password:</strong> {password}</p>
                <p><strong>Confirm Password:</strong> {confirm_password}</p>
            </div>
            <br>
            <a href="/">← Kembali Isi Biodata</a>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
