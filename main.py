# Importing Modules
import requests
import click
import datetime

# Data Function
def get(id):
    # Getting API Endpoint
    url = f"https://users.roblox.com/v1/users/{int(id)}"

    # Getting Endpoint Headers
    headers = {
        "User-Agent": "Python Requests",
        "Content-Type": "application/json"
    }

    # Sending Requests To Endpoint
    response = requests.request("GET", url, headers=headers)

    # Checking Response Code
    if response.status_code == 200:
        # Displaying Data
        data = response.json()
        print(f" User: {data['name']}\n Desc: {data['description']}\n Created: {data['created']}\n Banned: {data['isBanned']}")
    else:
        # Erorr Message
        print(f"Error: {response.status_code} : {response.text}")

# Commands
@click.command()
@click.option("--c", "--command", type=str, default="nil")
def data(c):
    if c == "data":
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("- Getting User Data", fg="red", bold=True)

        # Getting User ID
        id = input("User ID: ")

        get(id)

    else:
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("Error: Unknown Command : Typo?", fg="red", bold=True, blink=True)

if __name__ == "__main__":
    data()
