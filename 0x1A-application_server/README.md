This is a readme file for application server

GUNICORN ports used
---------
AirBnb_clone_v2
---------
> tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'

> tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'

AirBnb_clone_v3
----------
> tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'


AirBnb_clone_v4 (Automated in task 6)
----------
> tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'

Task 4:
-------
Added environment variable here
> sudo vi /etc/profile.d/airbnb_environment.sh


Task 6:
--------
Incase this task failed to start

> find . -name "*.pyc" -exec rm -f {} \;

and restart the service

> sudo systemctl start gunicorn

enable to start on system reboot

> sudo systemctl enable gunicorn

--------------------
What I have learned
--------------------
Each executable python files might use different python environment

You can check the environment by looking at the header of the package<br>
something like this `#!/usr/bin/python3` or else.

If you are using two incompatible packages, one of them might not find packages
installed in the other environment.

> /usr/bin/python3 -m pip install MISSING_PACKAGE
