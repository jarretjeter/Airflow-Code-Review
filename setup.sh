# If your terminal does not give you permissions to run this script, enter "chmod +x setup.sh" to grant execution permission

# Change path to the location in your computer that you downloaded this project 
export AIRFLOW_HOME=~/data-engineering-bootcamp/workspace/airflow-code-review

AIRFLOW_VERSION=2.3.2
PYTHON_VERSION=3.7

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

pip install -r requirements.txt

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
# Run "airflow standalone" in your terminal after the setup.sh finishes

# To change change user and password for the GUI after initializing Airflow, in your terminal enter, "airflow users create --role Admin --username [your user name] --email [your email] --firstname [first name] --lastname [last name] --password [your password]"

# When Airflow is up and running, in your browser go to "localhost:8080" to access the Airflow GUI