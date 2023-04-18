# Docker-Swarm-web-server, Docker Swarm Load Balancer (lb01) Setup

This repository contains a Python script that automates the setup of a Docker Swarm load balancer (lb01) on a manager node in Linode, with worker nodes in AWS.

## Prerequisites

- Manager node in Linode with Docker installed
- Worker nodes in AWS with Docker installed
- SSH access to the manager and worker nodes
- Python and Paramiko-(pip install paramiko) library installed locally

## Setup

1. Clone this repository to your local machine.
2. Update the Python script `main.py` with the correct hostnames, IPs, and SSH key paths for your manager and worker nodes.
3. Make sure you have the necessary SSH private key files for the manager and worker nodes, and update the `manager_ssh_key_path` and `worker_ssh_key_paths` variables in the script accordingly.
4. Run the Python script with `python main.py` to automate the setup of Docker Swarm and load balancer.

## Usage

The Python script automates the following steps:

1. Initializes Docker Swarm on the manager node using `docker swarm init` command.
2. Joins the worker nodes to the Docker Swarm using `docker swarm join` command.
3. Deploys a load balancer service using Nginx on the manager node with `docker service create` command.

The load balancer service listens on port 80 and uses the "global" mode to ensure that one instance of the service runs on each worker node, providing load balancing across the worker nodes.

## Troubleshooting

If you encounter any issues during the setup, please ensure that:

- SSH access to the manager and worker nodes is properly configured.
- Docker is installed and running on the manager and worker nodes.
- The Python script has the correct hostnames, IPs, and SSH key paths for the manager and worker nodes.

## Contributions

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## License

This repository is licensed under the [MIT License](LICENSE).

