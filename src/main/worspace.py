from src.main import bp
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_login import login_required, current_user
from src.models.workspace import Workspace
from src.models.task import Task
from src.models.label import Label
from flask import request
from src.extensions import db
from datetime import datetime 

@bp.route('/')
@login_required
def home(isEdit=False, et=None):
    l=list(Workspace.query.filter_by(user_id=current_user.id).all())
    if len(l)==0:
        new_wk=Workspace(name="work", user_id=current_user.id)
        db.session.add(new_wk)
        db.session.commit()
    l=list(Workspace.query.filter_by(user_id=current_user.id).all())
    print(l)
    t=current_user.tasks
    ws=request.args.get('wk') or '0'
    labels=current_user.labels
    name=''
    if ws=='0' and len(l)>int(0):
        t=Task.query.filter_by(user_id=current_user.id, workspace_id=l[0].id, is_done=False).all()
        t2=Task.query.filter_by(user_id=current_user.id, workspace_id=l[0].id, is_done=True).all()
        name=Workspace.query.filter_by(id=l[0].id).first()
    elif int(ws)>0:
        t=Task.query.filter_by(user_id=current_user.id, workspace_id=int(ws), is_done=False).all()
        t2=Task.query.filter_by(user_id=current_user.id, workspace_id=int(ws), is_done=True).all()
        name=Workspace.query.filter_by(id=int(ws)).first()
    else:
        print("why did it come to this")
        

    for x in t:
        t1=x.deadline_datetime - datetime.now()
        x.overdue=False
        if t1.days==0:
            x.timeleft='Today'
        if t1.days==1:
            x.timeleft='Tomorrow'
        if t1.days>1:
            x.timeleft=str(x.deadline_datetime.strftime('%A'))[:3]+', '+str(x.deadline_datetime.strftime('%d'))+' '+str(x.deadline_datetime.strftime('%b'))
        if t1.days==-1:
            x.overdue=True
            x.timeleft='Yesterday'
        if t1.days<-1:
            x.overdue=True
            x.timeleft=str(x.deadline_datetime.strftime('%A'))[:3]+', '+str(x.deadline_datetime.strftime('%d'))+' '+str(x.deadline_datetime.strftime('%b'))
        print(x.timeleft)
    return render_template('home.html', workspaces=l, tasks=t, labels=labels, done_tasks=t2, ws=name, isEdit=isEdit, et=et)

@bp.route('/addTask', methods=['POST'])
@login_required
def task():
    l=list(Workspace.query.filter_by(user_id=current_user.id).all())
    t=current_user.tasks
    labels=request.form.getlist('labels')
    name=request.form.get('taskName')
    date= request.form.get('deadline')
    deadline=datetime(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]), 20,0,0)
    wk=request.form.get('wkspaces')
    task = Task.query.filter_by(name=name, workspace_id=int(wk)).first()
    if task:
        return redirect(url_for('main.home'))
    print(type(date))
    new_task=Task(name=name, deadline_datetime=deadline, workspace_id=int(wk), user_id=current_user.id, created_datetime=datetime.now())
    labels_list=list(map(lambda l: Label.query.filter_by(id=int(l)).first(), labels))
    new_task.labels=labels_list
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.home'))

@bp.route('/completeTask', methods=['POST'])
@login_required
def taskComplete():
    id=int(request.args.get('id'))
    task=Task.query.filter_by(id=id).first()
    task.is_done=True
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.home'))

@bp.route('/uncompleteTask', methods=['POST'])
@login_required
def taskUnComplete():
    id=int(request.args.get('id'))
    task=Task.query.filter_by(id=id).first()
    task.is_done=False
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.home'))

@bp.route('/deleteTask', methods=['POST'])
@login_required
def deleteTask():
    id=int(request.args.get('id'))
    task=Task.query.filter_by(id=id).first()
    if task.user_id==current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.home'))

@bp.route('/getEditTask', methods=['POST'])
@login_required
def getEditTask():
    id=int(request.args.get('id'))
    task=Task.query.filter_by(id=id).first()
    if task.user_id==current_user.id:
        et=Task.query.filter_by(id=id).first()
        et.editdate=et.deadline_datetime.strftime('%Y-%m-%d')
        return home(isEdit=True, et=et)
    return redirect(url_for('main.home'))

@bp.route('/editTask', methods=['POST'])
@login_required
def editTask():
    id=int(request.args.get('id'))
    task=Task.query.filter_by(id=id).first()
    if task.user_id==current_user.id:
        labels=request.form.getlist('editlabels')
        name=request.form.get('edittaskName')
        date= request.form.get('editTaskDeadLine')
        deadline=datetime(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]), 20,0,0)
        wk=request.form.get('editwkspaces')
        task.name=name
        task.deadline_datetime=deadline
        task.workspace_id=int(wk)
        labels=request.form.getlist('editlabels')
        labels_list=list(map(lambda l: Label.query.filter_by(id=int(l)).first(), labels))
        task.labels=labels_list
        db.session.commit()
    return redirect(url_for('main.home'))
