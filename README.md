# reactDataDoodle-flask
This is the backend server handling data that is being sent from the reactDataDoodle frontend ([reactDataDoodle](https://github.com/gustavfahraeus/reactDataDoodle)). 

We are connected to a MongoDB document database where we store some user data related to the user's top tracks, artists, and genres. 
We also store the id so we can connect a user to multiple entries, as well as the date when these entries were uploaded to the database. 
There is a cooldown of 1 entry per 24h, so no one can spam my little poor Python server.

Peace & Love

