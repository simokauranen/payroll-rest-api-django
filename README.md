# Secure Django Payroll REST API

In this project I have created simple REST API (djangorestframework) interface to query employee's salary information, and for staff member to see all employees' info and to change salary for chosen person. The aim has been to configure the authentication framework (JWT Token, djangorestframework-simplejwt) and Django as secure as possible according to OWASP 10 list. 

The actual installation is at the moment under construction as Apache implementation in virtual Ubuntu server with HTTPS and MariaDB; the enclosed package contains only localhost implementation with Django development server. That is why the enclosed code has some less secure configurations. See details in chapter *Implemented security features*.

## Installation

1. Prerequisites: Python 3 installation.

2. Install requirements
    - Go to folder payroll_api_localhost/securesite (where are requirements.txt and django-requestlogs-modified-0.3.1.tar.gz)
    - Enter command `pip install requirements.txt`.

3. Start the server with command `python manage.py runserver`.

## Usage/testing

The solution contains sqlite3 database with prepopulated user/employee data.
The prepopulated credentials (don't worry, these are only for testing):

`admin: 876t&&%FFBuu9786_v`  (for the admin panel)  
`max: 78TyVBFESki=_KLH463`  (regular User/Employee: rights to see his/her own employee info)  
`maxine: lkj9573SD_?/&%` (regular User/Employee: rights to see his/her own employee info)  
`api_superuser: 987TYR#%&fjhR` (Member of Staff: rights to see all employees' info & change salary)


### Django Admin site
You can add employees by logging in to http://127.0.0.1:8000/admin with credentials ('admin', '876t&&%FFBuu9786_v'). (Before that configure `DEBUG = True` to get the CSS working. In Apache the static files are served in more sustainable way.) Employees are normal Django User objects with some additional information, so to add an Employee, add Django User.

### REST API

The actual REST API can be tested with `curl` command (see below) OR with Postman app (www.postman.com/downloads/), the test configurations of which are included in the folder *postman*.

The REST API supports the following scenarios:

- Fetch user/staff token (Regular user/Staff):

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "api_superuser", "password": "987TYR#%&fjhR"}' \
  http://localhost:8000/api/token/

```
This returns:

```
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}

```

- Get my own info (Replace the token with *access* token from the previous phase) (Regular user/Staff):

```
curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/payroll/api/v1/myinfo/

```

- Get all employees' info (Staff):

```
curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/payroll/api/v1/employees/

```

- Get info of a certain employee (id=3, from the previous step) (Staff)

```
curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/payroll/api/v1/employee/3/

```
- Change the salary of an employee (id=3) (Staff)

```
curl \
  -X POST \
   -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyMTQwMjQ0LCJqdGkiOiJjMDk0YmJmOTUwYjY0YzgzOTQ2NGYxMGY1OTk1ZGY0NCIsInVzZXJfaWQiOjJ9._5j4r58w52cvnpNAgsKSV2me2uHB89rH7jagQ_iuPLI" \
  -d '{"salary": "2222.23"}' \
  http://localhost:8000/payroll/api/v1/employee/3/

```
- Refresh the token:

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/token/refresh/

```

## Implemented security features

The REST API authentication (getting tokens in the first place) relies on normal Django authentication:
`django.contrib.auth`, `django.contrib.auth.middleware.AuthenticationMiddleware` and `django.contrib.auth.backends.ModelBackend`.
This can be considered safe as the framework is widely tested.  

For the admin panel, basic authentication has been tuned with `django-axes` (`axes.middleware.AxesMiddleware` and `axes.backends.AxesBackend`) to throttle invalid access attempts (by default after 5 tries) from given IP address and username.  

When the tokens are fetched they are valid only for a limited time (30 min). The refresh tokens are valid for 24 hours, but they can be used only once, after that the `rest_framework_simplejwt.token_blacklist` app blacklists the token.  

The solutions logs every HTTP request with the help of `requestlogs.middleware.RequestLogsMiddleware` that utilizes Django's own logging. The middleware is from pip package `django-requestlogs`, which I have modified to support obfuscating sensitive fields also in nested JSON, and can be found in `django-requestlogs-modified-0.3.1.tar.gz` with licence information.

In the Apache implementation the setting `DEBUG = False`, but in this localhost version it has to be set temporarily to `True` to get the Admin Panel CSS working. Also in Apache/Ubuntu `settings.SECRET_KEY` is hidden to an environment variable as well as database credentials. Please search text *APACHE_IMPL* in file `settings.py` to see the difference between local and Apache implementations. Also on Ubuntu the command `sudo mysql_secure_installation` has been run for the MariaDB and HTTPS (self-signed SSL Cert) implemented.


### OWASP 10

Let's have a quick look to the solution from the OWASP 10 point of view:  
(Reference: [1] https://nvisium.com/blog/2019/04/18/django-vs-the-owasp-top-10-part-1.html)

1.	Injection

    In this Payroll implementation URL patterns like 

        /payroll/api/v1/employee/<int:id>/

    where <int:id> allow only integers as input, eliminates possibilities for injection. 

2.	Broken Authentication

    In this application there are no possibilities to change password through Forgotten Password web interface, which decreases the vulnerability to broken authentication. Admin can change passwords in admin panel, so the admin password must be strong. If admin fails to login with 5 tries `django-axes` will lock the IP address and the username and it can be only be unlocked by another admin in Admin panel's Axes section or by CLI command `python manage.py axes_reset ...`.

3.	Sensitive Data Exposure

    Payroll application has several sensitive database fields: user *password*, employee *ssn* and *salary*.  

    To save passwords Django uses by default PBKDF2 algorithm with SHA256 hash function (policy recommended by National Institute of Standards and Technology (NIST) in USA). The passwords are never shown in plain text, not even in Admin panel.  

    Only Staff can see *ssn* and *salary* information through REST API or through Admin panel. Since the HTTP requests are logged to log file, these fields has to be obfuscated along with tokens *access* and *refresh*.  

    In the Ubuntu/Apache environment the following settings are in use with HTTPS:

    `SECURE_SSL_REDIRECT = True` This will redirect all HTTP traffic to HTTPS  
    `SESSION_COOKIE_SECURE = True` This ensures that the session cookie is only sent over HTTPS  
    `CSRF_COOKIE_SECURE = True` This will ensure that the CSRF Token is only sent over HTTPS2  

4.	XML External Entities (XXE)

    “Django version 2.2 is not vulnerable to XXE attacks on its own because the XML deserializer does not allow DTDs, fetching of external entities, or the ability to perform entity expansion.” [1]

5.	Broken Access Control

    “If django.contrib.auth is in the list of INSTALLED_APPS located in the settings.py file, then Django will automatically create, add, change, delete, and view permissions for each Model in the application.“ [1]

6.	Security Misconfiguration

    The best way to prevent error messages to give too much information is to set `DEBUG = False`. Now the `djangorestframework-simplejwt` might give too much information through response messages. For example, if you try to get Staff information as regular User, `simplejwt` does not allow it, but conveys whether access token is valid (for possible other actions). Fixing this is not in the scope of this project.

7.	Cross-Site Scripting (XSS)

    The component `djangorestframework` was vulnerable to XSS attacks before version 2.4.4. In this solution the version on the package is 3.11.0. Furthermore, the user input is validated before deserializing, so no malicious content can be injected.

8.	Insecure Deserialization  

    In general this on more complex, since Django has only basic check for deserialization:

    “When deserializing, the framework will check if the fields in the serialized data exist on a model. If the fields do not match, an error will be raised. This is the only protection that Django provides against Insecure Deserialization attacks. The best way to prevent these attacks is not to accept serialized data from untrusted sources.” [1]

    In the Payroll application, only authenticated Staff user can send POST request JSON (change salary) that will be deserialized as Employee object. If the parameter is not in the float number format, the REST API will give error message "Parameters not valid".

9.	Using components with known vulnerabilities

    Not known vulnerabilities according to OWASP Dependency-Check tool. However, as small as this project is, it has 96 dependencies!

10.	Insufficient logging and monitoring 

    By default, when `DEBUG = False`, Django logs *ERROR* and *CRITICAL* events.
    
    The Payroll application has two more logging utilities: 
    - `django-axes` logs the access attempts to Admin Panel Axes section
    - `django-requestlogs` logs all HTTP requests and responses, so we can see for example, when Staff member has changed salary.

    `django-requestlogs` is not optimal for high-volume production environments as such, since it logs too much: it should be restricted to only POST requests. In localhost solution the log file might be easily accessible, but in Ubuntu, Linux access rights take care that only certain groups can access the log file. Furthermore, sensitive information is obfuscated.




