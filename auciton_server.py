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

@app.route('/auction_room')
def room():
    """
    Render the auction room page
    """
    _table = auction.GetAll()
    table = list()
    for id in _table:
        item = auction.GetByID(id)
        table.append(item)
    return render_template('auction_list.html', table=table)

@app.route('/single_item/<item_id>')
def show(item_id):
    """
    Given the user the detailed info of an item
    """
    item = auction.GetByID(item_id)
    return render_template('single_item.html', item_id=str(item_id), item=item)

if __name__ == '__main__':
    app.run()
