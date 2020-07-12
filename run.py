#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import create_app
from dotenv import load_dotenv
import os

# load environmental variables
path = os.path.join(os.path.dirname(__file__), '.env')
# dotenv is a python package
load_dotenv(path)

# http://flask.pocoo.org/docs/1.0/api/
if __name__ == "__main__":
    app = create_app()
    # the run method runs the  dev application server - the variables in run aren't working for some reason so i use command line arguments
    #app.run(host='0.0.0.0', port=5000, debug=True, load_dotenv=True)
    app.run()
