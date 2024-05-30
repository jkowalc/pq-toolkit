# Perceptual Qualities Python Toolkit

Toolkit for preparing and conducting experiments that asses
perceptual qualities of audio.

## Project for course WIMU 23Z

Project members:
- Bartłomiej Piktel
- Paweł Müller
- Grzegorz Rusinek

### Further developed by

- ZPRP 24L course members:
  - Igor Matynia
  - Jakub Woźniak
  - Jan Kowalczewski
- #TODO WIMU

## Project structure

- docs - project documentation
- src - source files organised by modules
    - pq-toolkit - Python toolkit interface
    - pq-toolkit-ui - frontend for conducting experiments
    - pq-toolkit-api - backend service with api
    - deployments - docker compose and env files

## Usage

This project consists of test creation Python plugin and web application
testing platform.

### How to use Python plugin

Installation details are available in [pq-toolkit README](src/pq-toolkit/README.md), as well as in the [docs](docs/README.md).

The Python plugin can be used to interact with the PQ Toolkit API backend the same way as the web application and can also be used to read test results.

### How to start web application

1. Deployment:
   - Go to `src/deployments`
   - Fill in required configuration in `.env.*` files according to your specification
   - Build docker image by running `make build-[flavor]`
   - Deploy docker image by running `make start-[flavor]`
   - (To stop an image use `make stop-[flavor]`)
2. Uploading experiments
   - Using Python script
   - Using admin panel available at `/admin`
3. Verifying configuration using admin panel (`/admin/[experiment-name]`)
4. For users `/[experiment-name]`
5. Getting results using Python script

Available flavors:
- prod
- stage
- dev

## WIMU notes

Changes regarding design proposal:
- xml files, xmlbuilder2 -> json files + zod validation

Known issues:
- crude UI
- missing feedback components (e.g. comment for each sample)

Potential improvements:
- authorization for admin endpoints/panel
- better UI
- more options for test configurations (new tests or more helper components like feedback fields)
- separate backend for data handling, storage on larger scale (relational database)
- automatic mkdocs deployment

Project was on schedule up to Christmas, then slight delays in finishing remaining test types
and polishing features.

## ZPRP-24L notes

#TODO
