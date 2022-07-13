# Book Library
This is the Book Library pet project created base on Django framework.
The database diagram (ERD) and the use cases are described in Book Library.pptx

## Installation
In order to pull the repository and run the web application you may follow the next steps:

Create project directory
Linux/Windows:
```bash
mkdir <your_project_directory>
```
Go to created directory:
```bash
cd <your_project_directory/>
```
Clone repository from GitHub via command:
```github
git clone https://github.com/DmytroYahudin/BookLibraryDjango.git
```
In order to build docker container you need installed [Docker Compose](https://docs.docker.com/compose/gettingstarted/) in your system.
Make sure that Docker is installed on your pc and build the container.\
Linux:
```bash
sudo docker-compose up -d
```
Windows:
```bash
docker-compose up -d
```

After container is up and running create admin user to login into the app:
```bash
docker-compose exec -w /app/booklib web python manage.py createsuperuser
```
Enter any email, username and password(most of password validators are disabled, so it can be something simple like 123)

## Usage

You can access to the web application by following the link [http://localhost:8000/](http://localhost:8000/)
Also you can access as an admin to the django admin site by following the link [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## References
[Book Library at GitHub.com](https://github.com/DmytroYahudin/BookLibraryDjango/)
