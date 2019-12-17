# csci3308
software development group project. This allows users to send files to a host and then retrieve them both from a GUI and a UI. Currently only works on localhost but does allow for file sharing between users. A demonstration of this can be found here: https://youtu.be/G3KCmDdc1_E 

### Deployment
1. `git clone https://github.com/joerickard/csci3308_code`
1. `cd csci3308_code`
1. `psql postgres`
1. `\i database/initialization`
1. `\q`
1. Navigate to `./webserver/db_creds.py` and put your username and password

### Running the Program
1. `python3 webserver/api.py` in one terminal instance (this is the local webserver)
1. `python3 cli/budget_google_drive.py`  in another terminal instance (this is the CLI)
  - You can also navigate to `http://127.0.0.1:5000/api/login` to use the GUI
  
### Repository Orginization

The database initialization files are located in the database folder. The CLI is found within the cli folder. All other notable files (relavent to the software) are located in the webserver file. The app.py is the only file needed to be ran directly from that folder. The html resides in the templates folder and the javascript is in static/js/. All milestones are within the milestones folder.
