from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "azure-portfolio-secret-key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    artworks = [
        {"img": "art1.jpg", "title": "Abstract Flow"},
        {"img": "art2.jpg", "title": "Cloud Dream"},
        {"img": "art3.jpg", "title": "Azure Sky"}
    ]
    return render_template("gallery.html", artworks=artworks)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now: print to logs (Azure Log Stream)
        print(f"New Contact: {name} | {email} | {message}")

        flash("Thank you! Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
