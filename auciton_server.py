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
class AuctionTable():
    image = 0
    title = 0
    start_price = 0

def room(step):
    # Render the auction room page
    table = AuctionTable()
    return render_template('auction_list.html', table)

@app.route('/single_item/<item_num>')
def shows():
    """
    Given the user the detailed info of an item
    """
    user = None

    return render_template('single_item.html')

if __name__ == '__main__':
    app.run()
