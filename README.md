## TestReports


### Make migrations and migrate

```shell 
python manage.py makemigrations
python manage.py migrate
```

### Script for creating users in DB

```shell
python manage.py shell
```

```python
from main.models import Profile
from faker import Faker

faker = Faker()

num_users = 100

def make_username(f):
    return "_".join(f.name().split()).lower()


for i in range(num_users):
    username = make_username(faker)
    email = faker.email()
    date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=80)
    city = faker.city()
    user = Profile.objects.create_user(username=username, email=email, date_of_birth=date_of_birth, city=city)
    print(f"{i} - {user}")
```

### Run site
```shell
python manage.py runserver
```
