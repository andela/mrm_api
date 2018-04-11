## Product overview 
 The MRM-api is the backbone of a tool to facilitate room management. It enables  capturing of feedback based on room usage and analyse usage statistics.The MRM-api provides capability to register rooms and give feedback.

## Development set up
<<<<<<< HEAD
- Check that python 3, pip, virtualenv and postgress are installed

=======
- Install python 3
    - ##### Mac
        -  Install Brew in Terminal
        ```
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        ```
        -   Then Install Python 3
        ```
        brew install python3
        ```
    - ##### Windows
        - Download installation setup
        ```
        https://www.python.org/downloads/
        ```
        - Click the icon labeling the  Python file  and follow the prompts
        ```
         for example  python-3.6.2.exe.
        ```
    - ##### Linux
        - Run the following command in the terminal
        ```
        sudo apt-get update
       ```
        ```
        sudo apt-get install python3.6
        ```
        
- Install postgres
    - ##### Mac
    
        ```
        Follow guidelines  at this link (https://gist.github.com/sgnl/609557ebacd3378f3b72).
        ```

    - ##### Windows
        ```
        Follow guidelines  at this link (http://www.postgresqltutorial.com/install-postgresql/).
        ```
 
    - ##### Linux
       ```
       Follow guidelines  at this link (http://postgresguide.com/setup/install.html).
       ```

        
- Install python install package (pip) manager 
    ```
        For guidelines to install pip for your Operating system follow this link (https://pip.pypa.io/en/stable/installing/)
    ```
- Install virtualenv
    ```
    pip install virtualenv
    ```
>>>>>>> 9b996e0d... [Chore #156461913]Add contribution guide
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
    export APP_SETTINGS="Development" # set app Enviroment.
    export SECRET_KEY="some-very-long-string-of-random-characters"
    export DEV_DATABASE_URL="" # Db for Development.
    export TEST_DATABASE_URL="" # Db for Testing
    export DATABASE_URL="" # Db for Production
    ```
- Running migrations

    - Migrate database to new structure. Run the command below:
        ```
        alembic revision --autogenerate -m "Migration message"
        ```
    - Upgrade to new structure.Run the command below:
        ```
        alembic upgrade head
        ```
- Run application.
    ```
    python manage.py runserver
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




