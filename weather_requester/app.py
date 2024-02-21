#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# basics of planned web app, TBA

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    files = os.listdir("/workspaces/vscode-remote-try-python/weather_requester/topics")
    return render_template('index.html', files=files)
    #return "<p>Hello, World!</p>"

#def log():

    # Show directory contents
#    files = os.listdir("/workspaces/vscode-remote-try-python/weather_requester/topics")

    #with open("logs.txt", "r") as f:
    #    content = f.read()
#    return render_template('index.html', files=files)
