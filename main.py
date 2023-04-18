import paramiko
import time

# Define the hostnames, IPs, and SSH key paths for the manager and worker nodes
manager_hostname = 'manager-node.example.com'
manager_ip = '192.0.2.1'
manager_ssh_key_path = '/path/to/manager-ssh-key.pem'

worker_hostnames = ['worker-node1.example.com', 'worker-node2.example.com']
worker_ips = ['192.0.2.2', '192.0.2.3']
worker_ssh_key_paths = ['/path/to/worker1-ssh-key.pem', '/path/to/worker2-ssh-key.pem']

# SSH into the manager node
manager_ssh = paramiko.SSHClient()
manager_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
manager_ssh.connect(manager_ip, username='root', key_filename=manager_ssh_key_path)

# Initialize Docker Swarm on the manager node
stdin, stdout, stderr = manager_ssh.exec_command('docker swarm init --advertise-addr ' + manager_ip)
manager_token = stdout.readlines()[1].strip()  # Get the manager token for adding worker nodes
print('Manager node initialized with token:', manager_token)

# SSH into the worker nodes and join them to the Docker Swarm
for i in range(len(worker_hostnames)):
    worker_ssh = paramiko.SSHClient()
    worker_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    worker_ssh.connect(worker_ips[i], username='root', key_filename=worker_ssh_key_paths[i])

    # Join the worker node to the Docker Swarm
    worker_ssh.exec_command('docker swarm join --token ' + manager_token + ' ' + manager_ip)

    print('Worker node', worker_hostnames[i], 'joined the Docker Swarm')

# Wait for a few seconds to allow time for the worker nodes to join the Swarm
time.sleep(5)

# Deploy a Docker service for the load balancer on the manager node
manager_ssh.exec_command('docker service create --name lb01 --publish 80:80 --mode global nginx')

print('Load balancer service "lb01" created successfully')

# Close SSH connections
manager_ssh.close()
for worker_ssh in worker_sshes:
    worker_ssh.close()

print('Setup completed successfully!')
