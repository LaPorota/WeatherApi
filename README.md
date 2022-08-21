# WeatherApi

Welcome to my weather API!

## How it works?

The **Weather Api** works with **Openweather**'s Rest API. It filters the information brought by the server to give you a good forecast avoiding the miscellany.




https://user-images.githubusercontent.com/101206218/185814644-fcd88747-5708-4801-a1bd-bc082dcb999a.mp4




## How to use it?

**Weather Api** works with flask, so try to use it with your host up. You can use it without a runing server but I don't give guarantees that it will work :joy:

When your host is up you just can go to your favourite app (postman, imsomnia, web browser, etc) and do a **GET** request by adding url parameters on the **host/weather** path.

You'll have two files: **app file** and **config file**.

### Config File:

Here you will find two constants: **API_KEY** and **OW_URL**

**API_KEY**: here you put your OW API_KEY

**OW_URL**: It's the base URL to ask to the OW server.

### App file:

It's the one who give the functionalities and responses. (just watch the code)

You'll have two functional parameters: **city** and **country**

#### city:

The city parameter is essential and it works by itself allowing you to use it as unique parameter.

##### ex:

http://127.0.0.1:5000/weather?city=london

#### country:

This is an optional parameter, allows you to filter by city and country in case a you're looking for a city that has a namesake in different countries

##### ex:

http://127.0.0.1:5000/weather?city=london&country=gb







I hope it will be usefull to you and have a nice weather :joy:



