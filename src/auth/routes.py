from src.auth import bp
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, flash
from src.extensions import db
from flask_login import login_user, login_required, logout_user
from src.models.user import User 
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

@bp.route('/login')
def login():
    return render_template("login.html")

@bp.route('/login', methods=['POST'])
def login_us():
    username=request.form.get('username')
    password= request.form.get('pass')
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash('errCredentials did not match! Please Try again with different values.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=True, duration=datetime.timedelta(minutes=30))
    return redirect(url_for('main.home'))

@bp.route('/signup')
def signup():
    return render_template("signup.html")

@bp.route('/isUserIdAvailable')
def isAvailable():
    username=request.args.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"data":"1"})
    return jsonify({"data":"0"})

@bp.route('/signup', methods=['POST'])
def signup_user():
    username=request.form.get('userId')
    password= request.form.get('pass')
    name=request.form.get('name')

    if len(username)<5:
        flash('errUsername is too short')
        return redirect(url_for('auth.signup'))
    
    user = User.query.filter_by(username=username).first()
    if user:
        flash('errUsername Exists, Please try different one')
        return redirect(url_for('auth.signup'))
    
    new_user=User(username=username, name=name, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    flash('sucSuccessful Sign Up!')
    return redirect(url_for('auth.login'))