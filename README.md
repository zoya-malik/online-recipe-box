To create a virtual environment:

python3 -m venv recipebox_env
source recipebox_env/bin/activate

install dependencies:

pip install django mysqlclient Pillow

start the development server:

python manage.py runserver

recipebox_app/
└── templates/
    ├── registration/
    │   ├── register.html
    │   ├── login.html
    │   └── logged_out.html
    ├── recipe/
    │   ├── recipe_list.html
    │   ├── recipe_detail.html
    │   ├── recipe_form.html
    │   └── recipe_confirm_delete.html
    ├── ingredient/
    │   ├── ingredient_list.html
    │   ├── ingredient_detail.html
    │   ├── ingredient_form.html
    │   └── ingredient_confirm_delete.html
    ├── recipelibrary/
    │   ├── recipelibrary_list.html
    │   ├── recipelibrary_detail.html
    │   ├── recipelibrary_form.html
    │   └── recipelibrary_confirm_delete.html
    ├── folder/
    │   ├── folder_list.html
    │   ├── folder_detail.html
    │   ├── folder_form.html
    │   └── folder_confirm_delete.html
    ├── review/
    │   ├── review_list.html
    │   ├── review_detail.html
    │   ├── review_form.html
    │   └── review_confirm_delete.html
    ├── tag/
    │   ├── tag_list.html
    │   ├── tag_detail.html
    │   ├── tag_form.html
    │   └── tag_confirm_delete.html
    └── shoppinglist/
        ├── shoppinglist_list.html
        ├── shoppinglist_detail.html
        ├── shoppinglist_form.html
        └── shoppinglist_confirm_delete.html
