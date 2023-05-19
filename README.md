


# Project Name

This project uses Airflow and the Dad Joke API to send out daily emails to users.

## Overview

The purpose of this project is to provide users with a daily dose of humor via email. The project leverages Airflow to schedule and send emails, and the Dad Joke API to retrieve random jokes. The project is designed to be flexible and easy to configure, allowing users to specify the email recipients, email subject, and other parameters.

## Installation

To use this project, you will need to have Airflow installed. You can install Airflow using `pip`:

```
pip install apache-airflow

```

The project also requires the `requests` library to interact with the Dad Joke API:

```
pip install requests

```

## Configuration

To configure the project, you will need to edit the `dag.py` file. The file contains a DAG definition that specifies the email schedule and recipients, as well as the email content. You can customize the DAG by modifying the `default_args` and `send_email` tasks.




> Note: it's good practice to use `host.docker.internal` instead of your machine's internal ip address. Also `127.0.0.1` is a special address called loopback address that points to the local machine. Any traffic sent to this address is routed back to the same machine.


## Usage

After configuring the DAG, you can run it using the Airflow CLI:

```
airflow dags trigger send_email

```

This will trigger the DAG and send out the daily email.

## Contributing

Contributions to this project are welcome and encouraged. If you encounter any issues or have suggestions for improvement, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).