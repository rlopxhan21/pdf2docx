# PDF2DOCX Project - Backend

DF-DOCX Converter is a personal Django project that allows users to convert PDF and DOCX files to the desired format. The web application is designed to provide a user-friendly interface and an efficient conversion process.

## Tech Stacks:
- Backend: Django, Django REST Framework with amazing python packages like pdf2docx

## Functionality included:
- Convert PDF and DOCX files to the desired format
- User-friendly interface
- Efficient conversion process
- Download the converted files
- Support for multiple file conversions

## How to install:
In terminal:

```
git clone https://github.com/rlopxhan21/pdf2docx.git
```


After the clone is successful, open one terminal in project folder:
Run the following command for creating virtual env and installing all the required dependencies.

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

And also create a file .env in project folder and store SECRET_KEY, DEBUG & ALLOWED_HOSTS.

To run:

On project folder terminal:

```
python3 manage.py runserver
```

## Contributions:
This project is open to contributions from the community. If you find any bugs or want to add new features, feel free to submit a pull request.