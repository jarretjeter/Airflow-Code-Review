# _Airflow-Code-Review_

#### By _**Jarret Jeter**_

#### _This is a basic example of how to install Apache Airflow locally on your computer and then run a custom DAG_

## Technologies Used

* _Python_
* _Apache Airflow_

## Description

I included a bash script with instructions on how to set up Airflow locally on a machine. The Dag's tasks use simple bash commands and python functions.

## Setup/Installation Requirements

* _Make sure you have a text editor such as Visual Studio Code installed and also a linux bash terminal to use.
* _Clone this repository (https://github.com/jarretjeter/Airflow-Code-Review) onto your local computer from github_
* _In VS Code or another text editor, open this project_
* _Read the contents of setup.sh and then run it in your bash terminal_
* _Next, in your terminal run the command 'airflow standalone'_
* _Once you have Airflow up and running, go to your browser and enter the address 'localhost:8080'. You'll be prompted to enter a user which is 'admin' by default and a password. Look in the standalone_admin_password.txt file that was generated during the Airflow installation for your password._
* _Once logged in you can click on the DAG 'ch6_code_review_taskflow', toggle it on and run it to see it work. You can click on the individual tasks and then their logs to see their output after running._

## Known Bugs

* _No known bugs_

## License

_If you have any questions, please email me at jarretjeter@gmail.com_

[MIT](https://github.com/jarretjeter/Airflow-Code-Review/blob/main/LICENSE.txt)

Copyright (c) _6/23/2022_ _Jarret Jeter_