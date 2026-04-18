from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        result = a + b

    return f"""
    <h1>Simple Addition Web App</h1>
    <form method="post">
        <input type="number" name="a" placeholder="Enter first number" required><br><br>
        <input type="number" name="b" placeholder="Enter second number" required><br><br>
        <button type="submit">Add</button>
    </form>
    <h2>Result: {result if result is not None else ""}</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
