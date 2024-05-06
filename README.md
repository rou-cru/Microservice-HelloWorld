# Microservice "Hello World" Template

Components:
  - WebApp --> Vue
    - Nginx <-- Inverse Proxy
  - Backend --> Flask

## WebApp
Just prints the hostname of the backend. On this way, we know that the arquitechture works as expected.
The interface can be accessed through localhost in an Internet Browser without errors related with CORS or Hostnames unresolved.
Implemented with Vue as template to future development of a specific application.

## Backend
API implemented with Flask for simplicity, ist not exposed so just the Vue app can use the API.

## Microservices
We have 2 containers that create 1 microservice based webapp.

The data flow is straightforward
  Browser --> Vue --> Flask
  Browser <-- Vue <-- Flask

The user can access the backend directly
  Browser --X--> Flask

Because we require fetch the isolated API in the User browser, the Vue container adds a Nginx reverse proxy to resolve the backend IP as part of the same container.
Both containers are multistage to reduce the size in the final Images and are build throught a compose file.

## How run it?

  docker compose up --build

After complete the build process, go to __http://localhost/__ in a Web Browser, you should see something similar to "Name:2fdd6fde14cd" in the middle of the website.
