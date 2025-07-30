#!/bin/bash

# Bash script to install services on provisioned machines

vm_name=$1

# If statement to install Nginx only on machines that includes 'server' in their name
if [[ "$vm_name" == *"server"* ]]; then
    echo -e "\nServer detected, installing Nginx on '$vm_name'"   
else
    echo -e "\nSkipping Nginx installation. '$vm_name' is not a server - only machines that includes the string 'server' in their names are considered as servers"
fi
