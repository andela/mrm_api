[![CircleCI](https://circleci.com/gh/andela/mrm_api.svg?style=svg)](https://circleci.com/gh/andela/mrm_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/33ed9630b4f81976f784/maintainability)](https://codeclimate.com/repos/5b0c1a7f82b58e02d000118e/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/33ed9630b4f81976f784/test_coverage)](https://codeclimate.com/repos/5b0c1a7f82b58e02d000118e/test_coverage)
## Product overview
 The MRM-api is the backbone of a tool to facilitate room management. It enables  capturing of feedback based on room usage and analyse usage statistics.The MRM-api provides capability to register rooms and give feedback.

## Development set up
- Check that python 3, pip, virtualenv and postgress are installed

- Check that python 3, pip, virtualenv and postgress are installed

- Clone the mrm-api repo and cd into it
    ```
    git clone https://github.com/andela/mrm_api.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in .env file
    ```
    export APP_SETTINGS="development" # set app Enviroment.
    export SECRET_KEY="some-very-long-string-of-random-characters"
    export TEST_DATABASE_URL="" # Db for Testing
    export DATABASE_URL="" # Db for Production
    ```
- Create development database,run migrations and run application.

    -  Run the command below:
        ```
        fab set_up:user="system username"
        ```


## Built with
- Python version  3
- Flask
- Grapghql
- Postgres

## Contribution guide
##### Contributing
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.This Project shall be utilising a [Pivotal Tracker board](https://www.pivotaltracker.com/n/projects/2154921) to track  the work done.

 ##### Pull Request Process
- A contributor shall identify a task to be done from the [pivotal tracker](https://www.pivotaltracker.com/n/projects/2154921).If there is a bug , feature or chore that has not be included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
- The Contributor shall then create a branch off  the ` develop` branch where they are expected to undertake the task they have chosen.
- After  undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
- If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `develop` by the owners of this repository.




