# webfortune

##Run application from command line
In order to run this from the command line you must run "pip install Flask" the start the flask application with the command "flask run --host=0.0.0.0 --port={PORT #}"

The application may be accessed at "http://127.0.0.1:{PORT #}" as your URL

##Run application through Docker
To run this through Docker you must first build the container with "docker build -t klsadler/webfortune ."
 
Then run the program with "docker run -dp {PORT #}:5000 klsadler/webfortune" 

This can be accessed in your address bar with "{PORT #}:5000"

##Routes for the application
This program has four routes: "/", "/fourtune/", "/cowsay/{message}/", and "/cowfortune/".

"/" and "/fortune/" both return a page that give your a fortune using the fortune command. "/" redirects to "/fortune/"

"/cowsay/{message}/" returns a page with a cow saying the message prompted by the message in the address bar.

"/cowfortune/" displays a page of a cow saying a fortune from the fortune command

##Test application
When testing the application from the command line use the command "pytest"
