# covid19-simple-api

returns covid19 data for country
## installing on your machine

download the project on github, after that open your terminal and write:

```
$ cd covid19-simple-api
    # enter in the app folder
$ pip install -r requirements.txt
    # install the dependencies
$ python app.py
    # execute the app
```

to stop the server(localhost) press <kbd>Ctrl</kbd><kbd>+</kbd><kbd>C</kbd> or <kbd>Cmd</kbd><kbd>+</kbd><kbd>C</kbd>

# returned json

to use the api, use this link: [https://covid19-simple-api.herokuapp.com/api/{country name}](https://covid19-simple-api.herokuapp.com/api/russia)

***This is an example***
```
{
    "country": "<country name>",
    "total_cases": "<total cases>",
    "deaths": "<total deaths>",
    "recovered": "<total recovered>"
}
```

## License
[MIT](LICENSE)