## How to run

Simple run
``py run.py``


Init db with users but without application:
``rm -f instance/database.db && py db_init.py && py run.py``


Initialise db with users and an application:
``rm -f instance/database.db && py db_init.py -a && py run.py``
