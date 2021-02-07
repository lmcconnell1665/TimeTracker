# Time Tracker
![Continuous Integration Pipeline](https://github.com/lmcconnell1665/TimeTracker/workflows/Continuous%20Integration%20Pipeline/badge.svg)

## Overview
A django web app with a fully functioning login page that is integrated with the Plot.ly Dash library for creating visualizations in Python. There is also a function that pulls personal time sheet data from the Timeular API.

## Building and Testing
There is a GitHub Actions CI/CD pipeline that runs every time code is pushed to a branch of a pull request is created. This builds the python modules and runs some very simple tests on them as well as builds the django web app, postgres database, and runs some equally simple django tests.

## Future Plans
I want to develop this application to be easy to deploy to a production environment from the codebase. This exercise was done to get experience with django as well as setting up CI/CD pipelines.

### Specific ideas
* Turn the python functions that pull and clean data from the API into a click command line tool
* Add abilities to refresh the API data from the front end
* Update the python functions to push straight to postgres database instead of saving as csv's
