# ctr-invoice1-django

Basic invoice CRUD using Django.

Part of the CTR series of public Proofs Of Concepts experimenting with languages, tools and approaches.

## Scope

Interface and actions:

* Added to the Django admin interface

Invoice data is based in Invoice1 from the CTR project flattened to use only one model/table

```Javascript
{
    num: 1, // auto
    value: 1000.00, // float
    issueDate: "2000-01-02", // string representing date in yyyy-mm-dd
    parts_seller_name: "Example Ltd", // string between 3 and 30 chars
    parts_buyer_name: "Cedar stores Ltd.", // string between 3 and 30 chars
    status: "open" // "open", "canceled" or "paid"
}
```

## Run

In the folder with manage.py:

```shell
python manage.py runserver
```

## Stack

Python and main dependencies are:

* Python3
* Django
* venv
* pylint (to test invoice1 app)

Full list of dependencies in requirements.txt

## Dev notes

* When add a new depedency, run $ pip freeze > requirements.txt
* When change a models.py, run $ python manage.py makemigrations, $ python manage.py migrate
