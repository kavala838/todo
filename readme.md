# ToDo Application README

## Introduction
This is a simple ToDo Application developed using Python and Flask framework. The application allows users to manage their tasks efficiently by providing features like adding, completing, editing, and deleting tasks. Users can also categorize their tasks using labels and organize them within workspaces.

## Project Description
The ToDo Application is built using the Flask framework, a lightweight WSGI web application framework in Python. Flask offers simplicity and flexibility, making it ideal for developing web applications. The application utilizes Flask's built-in features along with Jinja2, a modern and designer-friendly templating engine for Python, to render dynamic HTML content and create a seamless user experience.

## Database
The application utilizes SQLite as its database engine and Flask SQLAlchemy as the ORM (Object-Relational Mapper) for interacting with the database. Below are the models used in the application:

### User
- Represents a user of the ToDo application.
- Attributes:
  - `id`: Primary key, unique identifier for the user.
  - `username`: Unique username of the user.
  - `password`: Hashed password of the user.
  - `name`: Name of the user.

### Task
- Represents a task that a user needs to complete.
- Attributes:
  - `id`: Primary key, unique identifier for the task.
  - `name`: Name/title of the task.
  - `workspace_id`: Foreign key referencing the workspace where the task belongs.
  - `user_id`: Foreign key referencing the user who owns the task.
  - `created_datetime`: Timestamp indicating when the task was created.
  - `deadline_datetime`: Deadline for completing the task.
  - `is_done`: Boolean field indicating whether the task has been completed.

### Workspace
- Represents a workspace where tasks can be organized.
- Attributes:
  - `id`: Primary key, unique identifier for the workspace.
  - `name`: Unique name of the workspace, specific to a user.
  - `user_id`: Foreign key referencing the user who owns the workspace.

### Label
- Represents a label that can be assigned to tasks for categorization.
- Attributes:
  - `id`: Primary key, unique identifier for the label.
  - `name`: Unique name of the label, specific to a user.
  - `user_id`: Foreign key referencing the user who owns the label.

### Relationships
- The User-Label has a one-to-many relationship.
- The User-Workspace has a one-to-many relationship.
- The User-Task has a one-to-many relationship.
- The Workspace-Task has a one-to-many relationship.
- The Label-Task has a many-to-many relationship.

## Authentication
Authentication in this application is implemented using Flask-Login, a session management library that uses cookies. Users can register for an account, log in, and securely manage their tasks within their account.

## Installation

To run the ToDo application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/kavala838/todo.git
    ```

2. Create a virtual environment:

    ```bash
    py -m venv ./venv
    ```

3. Activate the virtual environment:

    ```bash
    # On Windows
    .\venv\Scripts\activate

    # On Unix or MacOS
    source venv/bin/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set the variables for the app:

    ```bash
    # On Windows
    set FLASK_APP=src
    set FLASK_ENV=development

    # On Unix or MacOS
    export FLASK_APP=src
    export FLASK_ENV=development
    ```

6. Initiate the database:

    - Enter Flask shell:

    ```bash
    flask shell
    ```

    - Inside the Flask shell, run the following commands:

    ```python
    from src.extensions import db
    db.create_all()
    ```

    This will create an `app.db` file in the root directory of the project.

    - Exit from the Flask shell:

    ```bash
    exit()
    ```

7. Run the application:

    ```bash
    flask run
    ```

8. Access the application in your web browser(default port) at [http://localhost:5000](http://localhost:5000).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

