# Mevit back-end #
> Note: `The project step in a deep development stage`

This repository stores the files of the backend part of the Mevit medical project. The microservices responsible for image processing were created based on the modules of the desktop C++ application.

At the moment, the project has the following functionality:
* Particle size -> 1.png
* Cell deformability -> 2.png
* Aggregation of erythrocytes cell -> 3.png
* Aggregation of platelet cell -> 4.png

# How to start app? #
## Custom ##
You can run each microservice separately, but you must install the required python modules. This method suitable if you want to change the code and see how it will work with the changes.

## Docker ###
If you are using docker, then you need to run compose file in the root directory of the project with the command:
```sh
docker compose up
```
[![Docker hub page](https://hub.docker.com/r/serg228/med)](https://hub.docker.com/r/serg228/med)

# How to use? #
Once you have launched the application, go to
```sh
http://0.0.0.0:5100/docs
```
On the page you can see description of the functional, the data that is accepted by input methods.
The necessary files for tests are present in the /filsrv/origimg directory.
