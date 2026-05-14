import os
from flask import Flask, render_template, request, redirect

# Get absolute path (IMPORTANT for Pydroid / Android)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Store tasks in memory
tasks = []

# Home page
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

# Add task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task and task.strip() != "":
        tasks.append({"name": task.strip(), "done": False})

    return redirect("/")

# Mark task as done
@app.route("/done/<int:index>")
def done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    return redirect("/")

# Delete task
@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

# Run app
if __name__ == "__main__":
    app.run(debug=True)