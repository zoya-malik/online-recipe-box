- To create a virtual environment:
	
	python3 -m venv recipebox_env
	source recipebox_env/bin/activate

- install dependencies:
	
	pip install django mysqlclient Pillow
	

- Ensure MySQL is installed:

	brew install mysql
	brew services start mysql


- Open MySQL by running:
	mysql -u root -p

- Inside the MySQL shell run:
  
	CREATE DATABASE recipebox;
	CREATE USER 'recipeadmin'@'localhost' IDENTIFIED BY 'securepassword';
	GRANT ALL PRIVILEGES ON recipebox.* TO 'recipeadmin'@'localhost';
	FLUSH PRIVILEGES;
	EXIT;

- Apply the migrations:
	python manage.py makemigrations
	python manage.py migrate

- start the development server:

	python manage.py runserver
