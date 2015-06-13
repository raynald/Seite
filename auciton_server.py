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
    table = list(_table)
    # for id in _table:
    #      item = my_auc.GetByID(id)
    #      table.append(item)
    return render_template('auction_list.html', table=table)

@app.route('/single_item/<item_id>')
def show(item_id):
    """
    Given the user the detailed info of an item
    """
    item = auction.GetByID(item_id)
    return render_template('single_item.html', item=item)

@app.route('/update_bid/<item_id>,<new_price>')
def update(item_id, new_price):
    """
    Update the price of that product
    """
    auction.PlaceABid(item_id, new_price)
    item = auction.GetByID(item_id)
    return render_template('update_bid.html', item=item, new_price=new_price)

@app.route('/news')
def display():
    """
    Give the bidders the recent news
    """
    return render_template('news.html')

@app.route('/about_us')
def contact():
    """
    Contact US
    """
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run()
