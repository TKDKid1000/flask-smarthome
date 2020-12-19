# flask-smarthome
A simple flask app for control of the Samsung Smartthings. Also has some other stuff for the system shell and an online python compiler.

# Functions
This basic flask app contains 4 functions currently. A login system, a lighting control system, a system shell access system, and an online python executor.

# Modules
This flask app uses flask (obviously) found [here](https://flask.palletsprojects.com/en/1.1.x/). It also uses [flask login](https://github.com/maxcountryman/flask-login) for a login and verification system. The final module this sytem uses is called [pysmartthings](https://pypi.org/project/pysmartthings/) which is a set of http requests for accessing samsung smartthings!

# Usage
Anyone that wants to use it can use it. Its quite simple. Just download every file and extract them. Next you have to run it. Double click on "startserver.sh" and is all up and running, kinda. You have to edit the last line of the startserver.sh to fit your needs. Change the `-p 80` to `-p any port` and then change the `-h localhost`to `-h any host`. If you want it accessible from the outside you will have to change the host to `0.0.0.0`
