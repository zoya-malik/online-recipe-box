# Online Recipe Box

An online recipe management application built using Django. This application allows users to browse, search, and manage recipes. Admins can manage tags and recipes, while clients can register, browse, save recipes, and leave reviews.

## Prerequisites

Make sure you have the following installed on your machine:
- Python 3.12 or later
- Django 5.1.3
- Anaconda (for managing virtual environments)
- Git

## Installation Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/zoya-malik/online-recipe-box.git
   cd online-recipe-box

2. **Create a virtual environment using Anaconda**
   ```bash
   conda create --name recipebox python=3.12
   conda activate recipebox

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt

## Database Setup

1. **Make Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

## Running the Server

1. **Make Migrations**
   ```bash
   python manage.py runserver

The server will start at http://127.0.0.1:8000/

