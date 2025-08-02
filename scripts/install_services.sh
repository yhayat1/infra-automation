#!/bin/bash

# Bash script to install services on provisioned machines

# Get absolute path to the directory of this script
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Script paths
log_file="$script_dir/../logs/provisioning.log"
nginx_machines_file="$script_dir/../configs/nginx_servers.txt"

vm_name=$1

# Create a text file to list machines with Nginx installed if not exists.
if [[ ! -f "$nginx_machines_file" ]]; then
    touch "$nginx_machines_file"
fi

# Install Nginx only on machines that don't have Nginx installed already.
if grep -q "^$vm_name$" "$nginx_machines_file"; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - INFO - '$vm_name' found in '$(readlink -f $nginx_machines_file)'. Skipped Nginx install on '$vm_name'" >> "$log_file"
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - INFO - '$vm_name' not found in '$(readlink -f $nginx_machines_file)'. Installing Nginx on '$vm_name'" >> "$log_file"
    echo "$vm_name" >> "$nginx_machines_file"
fi
