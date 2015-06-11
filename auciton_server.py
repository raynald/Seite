#!/usr/bin/env python
# coding=utf-8
import auction
import flask
from flask import Flask
from flask import render_template, session, request

app = Flask(__name__)
app.debug = True
app.secret_key='this key is very secret indeed'

@app.route('/')
@app.route('/welcome_page')
def welcome():
    """
    Render the welcome page
    """
    return render_template('welcome_page.html')

@app.route('/auction_list')
def room(step):

    # Render the auction room page
    return render_template('auction_list.html', step=step, **args)

@app.route('/single_item/<item_num>')
def shows():
    """
    Give the user the results of the quiz
    """

    user = None
    migros.SavePreferences( user, session['question_list'], session['answers'] )
    x = migros.PersonalityTest( session['question_list'], session['answers'] )

    return render_template('results.html', **args)

if __name__ == '__main__':
    app.run()
