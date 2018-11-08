from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5cc98d63e402f74b38425d0b5b6cab85'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    validation_result = form.validate_on_submit()

    if validation_result:
        flash('Account created for {0}!'.format(form.username.data), category='success')
        return redirect(url_for('home'))
    else:
        print("something is wrong")
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    validation_result = form.validate_on_submit()

    if validation_result:
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login was unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)