# TrollPlaying Bot

To use this, you need to install Docker and Docker Compose.

You will have to copy `src/config.yml.sample` to `src/config.yml` and put your actual discord API key in there.

Once you have them, run `docker-compose build` and `docker-compose up` within this folder.

If you just want to run the tests, use `python3 -m unittest`. If you're doing this locally instead of inside the container, you'll need to install the requirements with `python3 -m pip install -U -r requirements.txt`.

To run the tests inside the container (**recommended**) use `docker-compose run trollbot python3 -m unittest`

ENJOY

To modify this, you probably want to read [The Discord.py API](http://discordpy.readthedocs.io/en/latest/api.html)
