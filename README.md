# Flask_restful
1- First you must clone the repository to where you prefer with the command:
- `git clone https://github.com/kaiqueBellmont/Flask_restful.git`

2 - Install the postman application to make requests and tests.

- (If you dont have Snap peckage, install snap with this comand):

- `sudo apt install snapd snapd-xdg-open`


- install postman :

- `snap install postman`

3 - Create a virtual enviroment (if you want...)

- `python3 -m pip install --user virtualenv`
- `python3 -m venv env`
- `source env/bin/activate` (To activate)

4 -  Install the dependences:

` pip install -r requirements.txt`

# Routes:
## SITES
GET `/sites`
- return a list of sites

---
GET `/site/{url}`
- return a selecioned site whose url is in the request
---
POST `/site/{url}`
- create a site in the database whose site is in request
---
DEL `/site/{url}`
- delete a site in the database whose site is in request
---


## Hotels:
- GET `/hotel/{id}` 
- example:
`http://127.0.0.1:5000/hotels?cidade=São pedro&estrelas_min=1`
- Returns a hotel/object like:
- {
    "hotel_id": 1,
    "nome": "Um dia apos o amanha",
    "estrelas": 2.5, 
    "diaria": 300.0,
    "cidade": "São pedro",
    "site_id": 1
 }
---
- GET `/hotels`

- return a list of created hotels
---
POST `/hotels` 
- Create a hotel in the database
- (need to create a site before
)
- like:
- {
    "nome": "hotel name",
    "estrelas": 2.5,
    "diaria": 150.00,
    "cidade": "São Paulo",
    "site_id": 1
}


PUT `/hotel/{hotel_id}`
- edit a field if you want. 

- (you must send the json format through postman and sent the site_id))
- like: 
- {
    "hotel_id": 1,
    "nome": "Um dia apos o amanha",
    "estrelas": 2.5,
    "diaria": 300.0,
    "cidade": "São pedro",
    "site_id": 1
}
---
DEL `/hotel/{id}`
- delete a hotel from the database whose id is in the request

---
##User
POST `/register`

- example:
- {
    "login": "admin",
    "password": "admin"
}
- create a user in the system.
- --
POST `/login`
- returns an access token to make any future requests
- {
    "login": "admin",
    "password": "admin"
}
---
POST `/logout`
- logout of the system
---
GET `user/{user_id}`
- return a json like that:
- {
    "user_id": 1,
    "login": "admin",
    "activated": true
}
---
GET `/confirmation/{user_id}`
- confirm the user in the system
---
DEL `/user/{user_id}`
- end ( for while )
---
