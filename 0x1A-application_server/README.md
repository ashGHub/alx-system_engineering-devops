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


AirBnb_clone_v4
----------
> tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'

Task 4:
-------
Added evnronment variable here
> sudo vi /etc/profile.d/airbnb_environment.sh
