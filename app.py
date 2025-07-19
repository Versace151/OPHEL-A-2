        from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OPHELİA</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #0a0a0a;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: 'Arial', sans-serif;
        }

        .heart-container {
            position: relative;
            width: 300px;
            height: 300px;
        }

        .left-heart, .right-heart {
            position: absolute;
            width: 50%;
            height: 100%;
            border-radius: 50%;
            border: 5px solid transparent;
            box-shadow: 0 0 20px #00f;
        }

        .left-heart {
            left: 0;
            border-right: none;
            border-top: 5px solid #00f;
            transform: rotate(-45deg);
            box-shadow: 0 0 20px #00f;
        }

        .right-heart {
            right: 0;
            border-left: none;
            border-top: 5px solid #f0f;
            transform: rotate(45deg);
            box-shadow: 0 0 20px #f0f;
        }

        .text {
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div class="heart-container">
        <div class="left-heart"></div>
        <div class="right-heart"></div>
        <div class="text">I love You</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)
