# An implementation of threaded comments upon Django using `django-mptt`.
You're at the right place if you're wondering how threaded comments on [uniqna](https://uniqna.com) work.


## Installation
1) Create a virtual environment and activate it
```
virtualenv -p python3 alpha
cd alpha
source bin/activate
```
2) Clone this repository
```
git clone https://www.github.com/jeremyphilemon/comment-threading
```
3) Install django-mptt and Run the code
```
pip install django-mptt
cd comment-threading
python3 manage.py runserver
```
4) Open your browser and go to [localhost:8000](https://localhost:8000). Also check out [django-mptt](https://github.com/django-mptt/django-mptt) for documentation and more information.

## Contributing
Fork the repo and feel free to submit pull requests :D

## Preview
<img src="https://cloud.githubusercontent.com/assets/17938322/25272855/0e2ca672-26a7-11e7-8282-06d8773366d1.png" width="30%">
