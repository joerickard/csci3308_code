# csci3308
software development group project

### Make things runnable
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
