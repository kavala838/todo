Created Venv
installed Flask and Flask-SQLAlchemy
created a config.py for application configuration
created the package src and created __init__.py as required
created extension.py toconfigure any flask related extensions
To Create a new db:
    delete existing app.db file
    open 'flask shell'
    from src.extensions import db
    db.drop_all()
    run 'db.create_all'

useful flask shell commands:
    db.engine.table_names()
    User.query.all()

    1. Add a row to a table:
    student_john = Student(firstname='john', lastname='doe',
                       email='jd@example.com', age=23,
                       bio='Biology student')
    db.session.add(student_john)
    db.session.commit()

    2. Adding a row for many-to-many relationship:
        p = Parent()
        c = Child()
        p.children.append(c)
        db.session.add(p)
        db.session.commit()
    
    3. drop a table:
        Label.__table__.drop(db.engine)
    
    4. Create a table:
        Label.__table__.create(db.engine)
        
    
