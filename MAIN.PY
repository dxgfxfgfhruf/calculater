from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Calculator 🔢➕➖✖➗</title>
  <style>
    body {
      background: linear-gradient(135deg, #667eea, #764ba2);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: white;
      margin: 0;
    }
    .calculator {
      background: rgba(255, 255, 255, 0.1);
      padding: 30px 30px 40px 30px;
      border-radius: 20px;
      box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
      width: 350px;
      backdrop-filter: blur(8.5px);
      -webkit-backdrop-filter: blur(8.5px);
      border: 1px solid rgba(255, 255, 255, 0.18);
      text-align: center;
    }
    h1 {
      font-size: 2.2rem;
      margin-bottom: 20px;
      user-select: none;
    }
    input[type=text] {
      width: 100%;
      font-size: 28px;
      padding: 12px 15px;
      text-align: right;
      border: none;
      border-radius: 15px;
      margin-bottom: 15px;
      outline: none;
      background: rgba(255, 255, 255, 0.2);
      color: white;
      box-shadow: inset 0 0 5px rgba(255,255,255,0.3);
      transition: background 0.3s ease;
    }
    input[type=text]:focus {
      background: rgba(255, 255, 255, 0.35);
    }
    button {
      font-size: 22px;
      padding: 12px;
      border: none;
      background-color: #6c63ff;
      color: white;
      border-radius: 12px;
      cursor: pointer;
      margin: 6px 8px 0 0;
      width: 65px;
      box-shadow: 0 4px 10px rgba(108, 99, 255, 0.4);
      transition: background-color 0.3s ease, transform 0.2s ease;
      user-select: none;
    }
    button:hover {
      background-color: #5148d6;
      transform: translateY(-2px);
    }
    button:active {
      transform: translateY(1px);
    }
    .result {
      font-size: 22px;
      margin-top: 18px;
      min-height: 36px;
      color: #f0eaff;
      background: rgba(0, 0, 0, 0.25);
      padding: 12px;
      border-radius: 12px;
      text-align: right;
      user-select: text;
      box-shadow: inset 0 0 5px rgba(0,0,0,0.3);
    }
  </style>
</head>
<body>
  <div class="calculator">
    <h1>Calculator 🔢 ➕ ➖ ✖ ➗</h1>
    <form method="POST">
      <input type="text" name="expression" value="{{ expression }}" placeholder="Enter calculation" autocomplete="off" />
      <div>
        <button type="submit">Calculate</button>
        <button type="submit" name="clear" value="1" style="background-color:#ff6b6b;">Clear</button>
      </div>
    </form>
    <div class="result">
      {% if result %}
        Result: {{ result }}
      {% endif %}
    </div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expression = ""

    if request.method == "POST":
        if "clear" in request.form:
            expression = ""
            result = ""
        else:
            expression = request.form.get("expression", "")
            try:
                # حذر عند استخدام eval - للاستخدام التعليمي فقط
                result = eval(expression)
            except ZeroDivisionError:
                result = "Error: Cannot divide by zero"
            except:
                result = "Error: Invalid expression"

    return render_template_string(html_template, result=result, expression=expression)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
