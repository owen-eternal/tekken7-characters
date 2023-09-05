# Tekken 7 Characters API

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/owen-eternal/tekken7-characters/main-workflow.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/e6dd5c041e9e45a4d548/maintainability)](https://codeclimate.com/github/owen-eternal/tekken7-characters/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/e6dd5c041e9e45a4d548/test_coverage)](https://codeclimate.com/github/owen-eternal/tekken7-characters/test_coverage)

![tekken](https://github.com/owen-eternal/tekken7-characters/assets/68030544/e16d6d73-ea8a-4e27-a25b-06c5624bf0c2)

This is a Django Project that's based on my favourite combat video game of all time - Tekken 7. The aim for starting this project is to showcase my Software/Platform engineering skills and hopefully impress my future employer.

## Topics covered by this Projects:

- **REST API Development using DJango Rest Framework:**
  - ModelSerialisers to encode/decode Queryset objects into JSON and vice versa 
  - ModelViewsets to process Retrieve and List requests. 
- **Unit testing using Django TestCase Client.**
- **Managing Environment Variables**
- **Containerization:**
  - Creating a Dockerfile for the Tekken API and serving the app through Gunicorn.
  - Creating Dockerfile for the reverse proxy to serve traffic using nginx.
  - Orchestrating container using Docker compose for local development and testing.
- **CICD Pipeline:**
  - Running Code Quality tests.
  - Running Unit test and generating a test coverage report on push to master.
  - Building, Scanning with Snyk and uploading Docker Image to ECR
  - Uploading Test coverage to CodeClimate.
  - Generating Maintainability, Build and test Coverage Badges.

