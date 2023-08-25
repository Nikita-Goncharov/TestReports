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

```shell
from main.models import Profile
from faker import Faker
import random

faker = Faker()
random.seed(42)

num_users = 100 

for i in range(num_users):
    username = faker.name()
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