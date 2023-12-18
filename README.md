# LEADS PROJECT

The Leads Project API is an application designed for the efficient management of processing elements. Developed using the FastAPI framework in Python, this API provides CRUD operations to manipulate actionable items. The application integrates with SQLAlchemy to effectively interact with a PostgreSQL database.

## Contenido

1. [Access to the Application](#access-to-the-application)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Project Structure](#project-structure)
5. [Authors and Contact](#authors-and-contact)
6. [Project Architecture](#project-architecture)

## Access to the Application

You can access the deployed application through the following link: [Leads Project - Access to the Application](https://leads-project-api.onrender.com/docs)

In addition, interactive API documentation is available at:

- [Swagger UI (ReDoc)](https://leads-project-api.onrender.com/redoc): Swagger's interactive user interface.
- [Swagger UI](https://leads-project-api.onrender.com/docs): Swagger's interactive user interface.

## Installation

Follow the instructions in the README.md file to install and run the project locally. API documentation will be available at http://localhost:5001/docs after execution.

1. **Clone the Repository:**

```bash
git clone https://github.com/danielcinome/leads-project.git
cd leads-project
```

2. **Virtual Environment Configuration (Optional, but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # For Unix-based systems (Linux/Mac)
```

3. **Installs Units:**

```bash
pip install -r requirements.txt
```

4. **Environment Variables Configuration:**

```
SECRET_KEY
ALGORITHM                       # Use case -> HS256
ACCESS_TOKEN_EXPIRE_MINUTES
SQLALCHEMY_DATABASE_URL
```

* To generate the SECRET_KEY you can use:
    ```bash
    openssl rand -hex 32
    ```

5. **Initialize the Database:**


```bash
alembic revision --autogenerate -m "create tables" # To generate the first migration
alembic upgrade head
```

6. **(Optinal):**

If you want to make use of docker, run the following command

```bash
docker-compose up --build
```

## How to Use

To execute the project use the command:

```bash
# Example of command or code
python runner.py
```

![F1-1](https://i.ibb.co/jWz1YGt/Captura-de-pantalla-2023-12-17-a-la-s-7-47-07-p-m.png)

To use the elements creation, update and deletion services, authentication is required:

- `/elements/create`
- `/elements/update`
- `/elements/delete/{uuid}`

To do this, if you do not have your own user, you must generate a registration from `/register`.

- Then click on Authorize and enter your authentication credentials, once authenticated you will be able to use the mentioned services.

    ![F2-2](https://i.ibb.co/rt7FsgL/Captura-de-pantalla-2023-12-17-a-la-s-7-47-50-p-m.png)


## Project Structure

The current structure of the project is organized as follows:

```plaintext
│── alembic/
│── app/
    │── api/
    │   │── elements/
    │   │── users/
    │   │── common/
    │── db/
    │   │── postgres/
    │       │── connector.py
    │── models/
    │   │── schemas.py
    │── main.py
│── requirements.txt
│── docker-compose.yaml
│── Dockerfile
│── README.md
│── runner.py
```

- **alembic/**: Contains files related to Alembic, a database migration tool for SQLAlchemy. It is used to manage changes in the database schema.
- **app/**: Main directory of the application source code.

  - **api/**: Contains modules that define the API paths.
    - **elements/**: Routes and logic related to element management.
    - **users/**: Paths and logic related to user authentication management.

  - **db/**: Contains modules related to database management.
    - **postgres/**: Contains `connector.py`, which implements the connection to a PostgreSQL database.

  - **models/**: Contains `schemas.py`, where the data models used in the application are defined.

  - `main.py`: Main entry point of the application.

- **requirements.txt**: File that lists the project dependencies.
- **docker-compose.yaml**: Configuration for Docker Compose.
- **Dockerfile**: File to build the Docker image.
- **README.md**: Main documentation of the project.
- `runner.py`: File to run or start the application.

## Project Architecture

The project architecture is based on a backend application developed in Python using the FastAPI framework. The authentication is done through JSON Web Tokens (JWT) using OAuth2PasswordBearer. The design is oriented to provide a RESTful API that allows the management of process elements  and users.

![F1-1](https://i.ibb.co/MZTDYKd/Captura-de-pantalla-2023-12-17-a-la-s-10-04-15-p-m.png)

## Authors and Contact
- Daniel Chinome
- Contact: danielchinomedev@gmail.com
- [LinkedIn](https://www.linkedin.com/in/danielchinome/)