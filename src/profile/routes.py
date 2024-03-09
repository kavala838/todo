from src.profile import bp
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from src.extensions import db
from src.models.label import Label
from src.models.workspace import Workspace

@bp.route('/profile')
@login_required
def home():
    l=list(Label.query.filter_by(user_id=current_user.id).all())
    w=list(Workspace.query.filter_by(user_id=current_user.id).all())
    return render_template('profile.html', name=current_user.name, labels=l, workspaces=w, username=current_user.username)

@bp.route('/addLabel', methods=['POST'])
@login_required
def addLabel():
    
    name=request.form.get('label')
    if len(name)==0:
        flash('Label is not valid')
        return redirect(url_for('profile.home'))
    label=Label.query.filter_by(name=name).first()
    if label:
        flash('Label already Present')
        return redirect(url_for('profile.home'))
    new_label=Label(name=name, user_id=current_user.id)
    db.session.add(new_label)
    db.session.commit()
    return redirect(url_for('profile.home'))

@bp.route('/addWorkspace', methods=['POST'])
@login_required
def addWorkspace():
    name=request.form.get('workspace')
    if len(name)==0:
        flash('Workspace is not valid')
        return redirect(url_for('profile.home'))
    wk=Workspace.query.filter_by(name=name).first()
    if wk:
        flash('Workspace already Present')
        return redirect(url_for('profile.home'))
    new_wk=Workspace(name=name, user_id=current_user.id)
    db.session.add(new_wk)
    db.session.commit()
    return redirect(url_for('profile.home'))

@bp.route('/editWorkspace', methods=['POST'])
@login_required
def editWorkspace():
    editName=request.form.get('editworkspace')
    wk=request.form.get('wkspaces')
    w=Workspace.query.filter_by(id=int(wk)).first()
    if w.user_id==current_user.id and w.name!=editName:
        w1=Workspace.query.filter_by(name=editName).first()
        if not w1:
            w.name=editName
            db.session.commit()
    return redirect(url_for('profile.home'))

@bp.route('/deleteWorkspace', methods=['POST'])
@login_required
def deleteWorkspace():
    wk=request.form.get('wkspacesdelete')
    print(wk)
    w=Workspace.query.filter_by(id=int(wk)).first()
    if w and  w.user_id==current_user.id:
        db.session.delete(w)
        db.session.commit()
    return redirect(url_for('profile.home'))