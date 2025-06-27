# FLASK
```

This flowchart outlines the key concepts and structure of the mini-projects in this repository, including login/logout, session management, Jinja2 templating, and form handling (manual and Flask-WTF).

---

## 🗝️ Key Concepts & Their Roles

- **return**:  
  Used in Flask route functions to send a response back to the client (browser).  
  _Example: All route functions in your apps use `return` to send HTML or redirect._

- **response**:  
  The object sent back to the client. Can be a rendered template, a redirect, or a custom message.  
  _Example: `return render_template(...)`, `return redirect(...)`, or `return Response(...)` in `login.py`._

- **redirect**:  
  Sends the user to a different route.  
  _Example: Used after form submission or login/logout to move the user to another page._

- **method**:  
  HTTP methods like GET and POST, used to distinguish between displaying a form and processing its data.  
  _Example: `methods=['GET', 'POST']` in your route decorators._

- **session**:  
  Stores data across requests for a user (like login state).  
  _Example: Used in `login.py` to keep track of logged-in users._

- **HTML**:  
  The markup language for web pages.  
  _Example: All your templates and inline forms use HTML._

- **Jinja2**:  
  The templating engine used by Flask to generate dynamic HTML.  
  _Example: All templates in the `templates/` folders._

- **jinja2 templating**:  
  Writing HTML with embedded Python-like expressions and control structures.  
  _Example: `{{ variable }}` and `{% for ... %}` in your templates._

- **jinja2 inheritance**:  
  Allows templates to extend a base layout, reducing repetition.  
  _Example: `Jinja2Inheritance/templates/base.html` is extended by other templates._

- **templates**:  
  Folder containing HTML files rendered by Flask.  
  _Example: Each app has its own `templates/` directory._

- **static**:  
  Folder for static files like CSS, JS, images (not shown in your current structure, but standard in Flask).  
  _Example: Would be used for styling or scripts if added._

- **render_template**:  
  Flask function to render an HTML template with variables.  
  _Example: Used in all your route functions that return HTML pages._

- **request**:  
  Flask object to access incoming request data (form data, query params, etc.).  
  _Example: `request.form.get(...)` in your form handling routes._

- **Flask Form Handling and Validation**:  
  Handling user input from forms and validating it before processing.
  |
  |-- User Input
      |
      |-- Manual Form Handling
      |   |
      |   |-- Flask Message
      |   |   |
      |   |   |-- Redirected After Submission
      |
      |-- Flask-WTF
          |
          |-- Form Classes
          |-- Field Types
          |-- CSRF Protection
          |-- Built-in Validation

---

## 📁 Directory Overview

FLASK_F1/
│
├── app.py
│   # (Optional) Central or experimental Flask app (not the main entry for subprojects)
│
├── FlashMessageInFlask/
│   ├── flashMessage.py
│   │   # Demonstrates using Flask's flash messaging system for user feedback.
│   └── templates/
│       ├── base.html
│       ├── form.html
│       └── thankyou.html
│       # Templates for the flash message demo.
│
├── Jinja2Inheritance/
│   ├── jinga2_inheritanceDemo.py
│   │   # Shows Jinja2 template inheritance and rendering multiple pages.
│   └── templates/
│       ├── about.html
│       ├── base.html
│       ├── contact.html
│       └── home.html
│       # Templates demonstrating inheritance and content blocks.
│
├── Login/
│   └── LogoutSAmple/
│       ├── login.py
│       │   # Simple login/logout system using Flask sessions.
│       └── login.txt
│           # (May contain sample credentials or notes.)
│
├── MaualFormHandling/
│   ├── manualHandling.py
│   │   # Example of manual form handling and feedback in Flask.
│   └── templates/
│       ├── base.html
│       ├── feedback.html
│       └── thankyou.html
│       # Templates for manual form handling demo.
│
├── sample.html
│   # (Sample HTML file, not tied to a specific demo.)
│
└── README.md
    # Project documentation
