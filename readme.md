To start, simply clone the repository and run the services from the docker_compose file.

If you run the entire docker-compose at once, you may encounter the following problem:

    When starting for the first time, despite the fact that the test container is instructed to wait for the browser 
    container to start, the tests may still go to the browser that has not yet started. So if all tests fail on the 
    first run, try restarting only the test container.

    The reason for this is that the wait is implemented at the container level, and the test container starts only 
    when the browser container is started, but in the started container, the browser itself is still starting. The tests 
    may be able to start the container and start themselves before the browser is ready, causing the problem.
    
    It should be noted separately that such a problem does not arise in CI, as in CI, the browser instances are 
    correctly started in a separate job preceding the tests.

However, this problem can be avoided by starting the browser container first and only then running the test container.

For local tests start, you just needed to start browser container, install requirements and then you can start tests 
in IDE.