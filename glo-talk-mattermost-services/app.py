"""Flask application for the Glo Talk Mattermost services website."""

import os

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/public",
)

# A secret key is required for flash messages. Replace this in production with
# an environment variable such as os.environ["SECRET_KEY"].
app.secret_key = os.environ.get("SECRET_KEY", "replace-this-development-secret-key")

PACKAGES = {
    "starter": "Starter Setup",
    "business": "Business Setup",
    "enterprise": "Enterprise Setup",
}

PAYMENT_METHODS = {"mpesa", "bank", "card", "invoice"}
HOSTING_OPTIONS = {"existing", "new-server", "need-guidance", "not-sure"}


def has_text(value: str | None) -> bool:
    """Return True when a submitted field contains non-empty text."""
    return bool(value and value.strip())


def is_valid_email(value: str | None) -> bool:
    """Beginner-friendly email check for contact and inquiry forms."""
    return has_text(value) and "@" in value and "." in value.split("@")[-1]


def validate_payment_form(form) -> list[str]:
    """Validate the payment/inquiry form and return readable errors."""
    errors: list[str] = []
    required_fields = {
        "package": "Please choose a package.",
        "customer_name": "Please enter your name.",
        "company_name": "Please enter your company or organization name.",
        "email": "Please enter a valid email address.",
        "phone": "Please enter your phone number.",
        "users": "Please enter the expected number of users.",
        "hosting": "Please choose a preferred hosting option.",
        "payment_method": "Please choose a payment or invoice option.",
    }

    for field, message in required_fields.items():
        if not has_text(form.get(field)):
            errors.append(message)

    if has_text(form.get("email")) and not is_valid_email(form.get("email")):
        errors.append("Please use a valid email address.")

    if has_text(form.get("package")) and form.get("package") not in PACKAGES:
        errors.append("Please choose a valid package option.")

    if has_text(form.get("hosting")) and form.get("hosting") not in HOSTING_OPTIONS:
        errors.append("Please choose a valid hosting option.")

    if has_text(form.get("payment_method")) and form.get("payment_method") not in PAYMENT_METHODS:
        errors.append("Please choose a valid payment option.")

    if has_text(form.get("users")):
        try:
            if int(form.get("users", "0")) < 1:
                errors.append("Number of users must be at least 1.")
        except ValueError:
            errors.append("Number of users must be a whole number.")

    return errors


def validate_contact_form(form) -> list[str]:
    """Validate contact form submissions with simple readable checks."""
    errors: list[str] = []

    if not has_text(form.get("name")):
        errors.append("Please enter your name.")
    if not is_valid_email(form.get("email")):
        errors.append("Please enter a valid email address.")
    if not has_text(form.get("message")):
        errors.append("Please tell us how we can help.")

    return errors


@app.route("/")
def index():
    """Render the main landing page."""
    return render_template("index.html")


@app.route("/pricing")
def pricing():
    """Render the detailed packages page."""
    return render_template("pricing.html")


@app.route("/payment", methods=["GET", "POST"])
def payment():
    """Render and process the package inquiry/payment-intent form."""
    selected_package = request.args.get("package", "")

    if request.method == "POST":
        errors = validate_payment_form(request.form)
        selected_package = request.form.get("package", "")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "payment.html",
                selected_package=selected_package,
                form_data=request.form,
            ), 400

        # Placeholder for CRM, email, invoice, M-Pesa, Stripe, or database logic.
        flash("Thank you. Your Glo Talk request has been received.", "success")
        return redirect(url_for("success"))

    return render_template(
        "payment.html",
        selected_package=selected_package,
        form_data={},
    )


@app.route("/success")
def success():
    """Render the submission confirmation page."""
    return render_template("success.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Render and process the contact form."""
    if request.method == "POST":
        errors = validate_contact_form(request.form)

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("contact.html", form_data=request.form), 400

        # Placeholder for email delivery, CRM capture, or helpdesk integration.
        flash("Thank you. We will reply to your message soon.", "success")
        return redirect(url_for("success"))

    return render_template("contact.html", form_data={})


@app.route("/health")
def health():
    """Simple JSON endpoint for uptime checks."""
    return jsonify({"status": "ok", "service": "Glo Talk"})


if __name__ == "__main__":
    app.run(debug=True)
