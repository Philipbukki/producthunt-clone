# producthunt-clone

### How it works 
An authenticated user to add a product.
Unauthenticated users are only able view all the product listings but not add products

##### clone this repository
```console
https://github.com/Philipbukki/producthunt-clone.git

```

##### create a virtual environment
```console
python3 -m venv venv
```

##### activate virtual env

```console
source venv/bin/activate

```

##### change directories into your repository
```console
cd ProductHuntDjango
```

##### install the packages needed.
```console

pipenv install -r requirements.txt
```

##### Make migrations
```console
python3 manage.py makemigrations
python3 manage.py migrate
```


##### Run the application
``` console
python manage.py runserver
```

Navigate to http://localhost:8000 in your web browser to view the application.
