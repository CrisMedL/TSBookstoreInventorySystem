# Project Instructions

## 1. Cloning the Repository

To clone the repository to your local machine, run the following command in your terminal or command prompt (make sure git is installed):
`git clone https://github.com/CrisMedL/Bookstore-Inventory-System.git`

This will create a local copy of the repository in a folder named `Bookstore-Inventory-System`.

## 2. Setting Up the MySQL Database Connection

Before running the project, you need to set up the MySQL database connection. Follow these steps:

### 2.1 Install MySQL Connector

`pip install mysql-connector-python`

### 2.2 Set Up the `.env` File

Create a `.env` file in the root directory of the project. This file will store your database credentials securely. Here is an example of how it should look:

``` 
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=bookstore
DB_PORT=3306
```

**IMPORTANT**

- If you have not done so, create the database using the `bookstore_schema.sql` file provided in the [db directory](../db/bookstore_schema.sql).
- Replace `your_mysql_password` with your actual MySQL root password
- **Do not upload your .env file** to GitHub. Make sure the file is added to your `.gitignore` file to keep sensitive information private.

### 2.3 Create a `.gitignore` File and Add `.env` To It

To ensure the `.env` file is not uploaded to GitHub, create a `.gitignore` file if it does not exist already in your project root directory. Add the `.env` by writing `.env` in your `.gitignore` file. 

### 2.4 Install `python-dotenv` to Load Environment Variables

In case you haven't installed `python-dotenv` do the following step, otherwise you can skip this.

To make Python recognize and use the `.env` file, you need to install the `python-dotenv` package. Run the following command to install it:

`pip install python-dotenv`

### 2.5 Load Environment Variables in Python

To use the values from the `.env` file in your Python code, you need to load them using `python-dotenv`. Here's how you can do that.

```
# Example of how to verify if python recognizes your .env file

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables using os.getenv()
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

print(f"Host:{db_host},\nUser: {db_user},\nPassword: {db_password},\nDatabase: {db_name},\nPort:{db_port}")  

```
**NOTE**: For the code above to work, make sure your `.env` file is in the root directory of your project.

## 3. Setting up the project

Make sure to have all dependencies installed. For our case, there is a file called `requirements.txt` in the `Config` directory of our repo. You can install it by running this in the command line:

`pip install -r Config/requirements.txt`

## 4. Working with Git: Basic Commands

Below are essential Git commands to help you manage your workflow:

1. **Checking the Status**

`git status`

2. **Creating a New Branch**

Ensure you have `main` and `dev` branches:

`git branch -a`

If you need to create the `dev` branch:

`git checkout -b dev`

Switch to it:

`git checkout dev`

3. **Pulling Updates**

Ensure your local `dev` branch is up-to-date:

`git pull origin dev`

4. **Adding Changes to Staging**

`git add <filename>` or `git add .` (to add all changes)

5. **Committing Changes**

`git commit -m "Your commit message"`

Example: `git commit -m "Added database connection functionality"`

6. **Pushing Changes**

`git push origin dev`

## 5. Merging `dev` into `main`

1. **Ensure `dev` is Pushed and Switch to `main`**

`git push origin dev`

`git checkout main`

2. **Pull Latest Changes from `main`**

`git pull origin main`

3. **Merge `dev` into `main`**

`git merge dev`

4. **Push Changes to Remote `main`**

`git push origin main`

## 6. Additional Git Tips

- **Removing a File from Staging**

`git reset <filename>`

- **Undoing Changes in a File**

`git checkout -- <filename>`

- **Deleting a Branch**

`git branch -d dev`

## 7. Important Notes

- Always pull the latest changes from `dev` before starting work to avoid conflicts.
- Ensure your `.env` file is never uploaded to GitHub.
- Refer to [Work Guidelines](Work_Guidelines.md) for collaboration practices.