# DataGenius Challenge Backend

This project is developed using Django REST framework in order to serve as a Restful api for a supermarket checkout management solution.

## Getting Started

```sh
git clone https://github.com/achsofiene10/Challenge-rest-api.git
cd Challenge-rest-api
python3 -m venv env       // create a virtual environment to isolate our package dependencies
source env/bin/activate   // activate the virtual environment
pip install django
pip install djangorestframework
pip install django-cors-headers
python manage.py runserver
```

**Note** : you can use others virtual environments like conda for example or you can simply install dependencies locally.


Now open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
Connect to the dashboard using : 
- Username : DG-admin
- Password : admin

 
## Projet structure   

This repository is composed of :
- folder Challenge : which contains Django project configuration files.
- folder myapi : contains our api configuration files(views,serializers,models,...).
- folder tickets : contains pdf files of tickets sent from Front-end.
- db.sqlite3 : file of sqlite database ( in general it should not be pushed to remote repo).
- manage.py : Django file that allows to run administrative tasks.
- README.md : contains information about the project.


### Models 

we created two models : Product, Ticket

```sh
class Product(models.Model):
  name = models.CharField(max_length=200)      
  description = models.CharField(max_length=300)
  quantity=models.IntegerField()    
  price=models.FloatField()
  discount=models.IntegerField()
  offer=models.BooleanField()
  image=models.CharField(max_length=300)
```

-the field discount indicate the percentage of discount in the product.
-the field offer indicate if there is an offer(2 products= 1 for free) for this product or not,if we need to make the offer dynamic of every product we need another model Offer where we have to describe exactly what is the offer of the product using a foreign key from product model.

```sh
class Ticket(models.Model):
  date = models.DateTimeField(default=timezone.now)
  file_path=models.CharField(max_length=300)
```

-the field file_path indicate the path of pdf file of ticket.


### Routes 

- http://127.0.0.1:8000/admin : to access admin dashboard
- http://127.0.0.1:8000/getallproducts : to get all products from the database
- http://127.0.0.1:8000/addticket : to create a new ticket and save the pdf file


## Some screenshots 

<p align="center">
<img src="https://i.ibb.co/hY6QygY/Login.png" />
</p>


<p align="center">
<img src="https://i.ibb.co/WvZDRvg/Home.png" />
</p>


<p align="center">
<img src="https://i.ibb.co/vYcQSG5/Product-Model.png" />
</p>


<p align="center">
<img src="https://i.ibb.co/YyxTCYS/Ticket-Model.png" />
</p>


<p align="center">
<img src="https://i.ibb.co/BNcztqz/Api-test.png" />
</p>






