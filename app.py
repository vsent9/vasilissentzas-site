from flask import Flask, render_template
import os
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gallery/<category>")
def gallery(category):

    folder = f"static/images/{category}"

    image_ext = (".jpg", ".jpeg", ".png")
    video_ext = (".mp4", ".mov", ".webm")

    files = os.listdir(folder)
    files = sorted(files)

    

    items = []
    for f in files:
        if f.lower().endswith(image_ext):
            filetype = "image"
        elif f.lower().endswith(video_ext):
            filetype = "video"
        else:
            continue

        items.append({
            "filename": f,
            "type": filetype
        })

    with open("titles.json", "r", encoding="utf-8") as f:
        titles = json.load(f)

    return render_template("gallery.html", items=items, titles=titles, category=category)


@app.route("/exhibitions")
def exhibitions():
    with open("exhibitions.json", "r", encoding="utf-8") as f:
        exhibitions = json.load(f)
    return render_template("exhibitions.html", exhibitions=exhibitions)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/press')
def press():
    return render_template('press.html')


if __name__ == "__main__":
    app.run(debug=True)

