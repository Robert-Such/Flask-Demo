import os
from flask import Flask, request, Response, redirect, Markup, make_response, jsonify
from flask import render_template, url_for
from forms import ContactForm, SignupForm

app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.Config")
app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    """Serve homepage template."""
    return render_template(
        "index.jinja2",
        title='Flask-Login Tutorial.',
        body="You are now logged in!"
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template",
        title="Contact Form"
    )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(
                    name=name,
                    email=email,
                    password=generate_password_hash(
                        password,
                        method='sha256'
                    ),
                    website=website
                )
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template(
        "signup.jinja2",
        title='Create an Account | Flask-Login Tutorial.',
        form=SignupForm(),
        template='signup-page',
        body="Sign up for a user account."
    )


@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template(
        "success.jinja2",
        template="success-template"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
