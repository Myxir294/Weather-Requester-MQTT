#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

def log():
    with open("logs.txt", "r") as f:
        content = f.read()
    return render_template('log.html', content=content)