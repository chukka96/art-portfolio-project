from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = "azure-portfolio-secret-key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    gallery_data = {
        "Certifications": [
            {"img": "cert1.jpg", "title": "AZ-104 Azure Administrator"},
            {"img": "cert2.jpg", "title": "AZ-400 DevOps Engineer"}
        ],
        "Posters": [
            {"img": "poster1.jpg", "title": "Event Poster"},
            {"img": "poster2.jpg", "title": "Movie Poster"}
        ],
        "Edits": [
            {"img": "edit1.jpg", "title": "Photo Manipulation"},
            {"img": "edit2.jpg", "title": "Color Grading Edit"}
        ]
    }

    return render_template("gallery.html", gallery_data=gallery_data)


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
