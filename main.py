from faker import Faker
from faker.providers import internet
import csv
from flask import Flask
import  requests
app  = Flask(__name__)
file = open('requirements/requirements.txt')
url = 'http://api.open-notify.org/astros.json'
list_rows = []
done_rows = []
@app.route('/')
def main_page():
   return ('Hello Dear friends')


@app.route('/requirements/')
def requirements():
   file = open('requirements/requirements.txt')
   return file.read()


@app.route('/generate-users/')
def generate_users():
   dict_users = {}
   fake = Faker()
   fake.add_provider(internet)
   for i in range(101):
       dict_users[fake.first_name()]=[f'{fake.first_name()}@mail.ru']
   return dict_users


with open('hw.csv') as f:
    reader =csv.reader(f)
    for row in reader:
        a = list_rows.append(row)
for i in list_rows[1:101]:
    a = done_rows.append(i)


@app.route('/mean/')
def convert():
    dict_of_converts = {}
    for i in done_rows:
        inches = float(i[1])
        pounds = float(i[2])
        inches_to_cm = inches*2.57
        pounds_to_kg = pounds/2.205
        for el in range(0,101):
            dict_of_converts[inches_to_cm]=pounds_to_kg
    return dict_of_converts


@app.route('/space/')
def astro():
    r = requests.get(url)

    return r.json()


if __name__ == '__main__':
   app.run(debug = True)















