from src.models import VMSpec
from src.machines import create_machine
import logging
import json
import os
import subprocess
import time

# Define script base dir
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define script files paths
def define_path(dir, file):
    dir = os.path.join(base_dir, dir)
    os.makedirs(dir, exist_ok=True)
    file = os.path.join(dir, file)    
    return file

json_config_file = define_path("configs", "instances.json")
logs_file = define_path("logs", "provisioning.log")
bash_script_file = define_path("scripts", "install_services.sh")   

# Define logging configuration
logging.basicConfig(
    level=logging.INFO,                            # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Omit milliseconds
    filename=logs_file,                            # Send teh logs to the log file
    filemode='a'                                   # For appending the data in file
)

# Check for existing json config file   
def load_existing_config(json_config_file):
    if not os.path.exists(json_config_file):
        return []  # No file, return empty list
    try:
        with open(json_config_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []  # If corrupted or missing, fallback safely
    
def append_vm_spec(config_file, vm_specs):
    config = load_existing_config(config_file)
    config.append(vm_specs)
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)

def provision_machines():
    while True:
        user_input = input("\nWould you like to provision machines? (yes/no) ").lower().strip()
        if user_input == "yes":
        #user_input = "yes"
            while True:
                # Take user input for VM deatils and specs            
                name = input("\nEnter a VM Name: ").strip() 
                os = input("Select the desired OS to be deployed to the VM: (Supported OS: ubuntu/centos/windows) ").lower().strip()
                cpu = input("Insert the desired number of VM CPU cores (eg: 4): ").strip()
                ram = input("Insert the desired number of RAM to be allocated to the VM (size unit is in GB. eg: 16): ").strip()
                                
                # Validate data using the Pydantic class
                try:
                    vm_specs = VMSpec(name=name, os=os, cpu=cpu, ram=ram)
                    logging.info(f"'{vm_specs.name}' VM specification is valid.")
                    # Call the "create machine" module to return a dict from values
                    vm_specs = create_machine(name, os, cpu, ram)  
                    # Append VM config to the json config file
                    append_vm_spec(json_config_file, vm_specs)

                except Exception as e:
                    logging.error(f"VM Validation error: {e}")
                    print(f"\nVM name '{name}' validation test failed. The VM won't be provisioned")

                while True:
                    # Check if the user wants to define another machine                       
                    user_input_another_vm = input(f"\nWould you like to provision another machine? (yes/no) ")
                    if user_input_another_vm == "yes":
                        break 
                    elif user_input_another_vm == "no":
                        return
                    else:
                        print("\nInvalid answer, try again")
                        continue
        elif user_input == "no":
            print("\nOk. Exiting\n")
            exit()
        else:
            print("\nInvalid answer. Try again.\n")
            continue

def run_bash_script():
    # Load and parse instances.json file as a json object
    with open(json_config_file, 'r') as f:
        machines = json.load(f)
    for machine in machines:
        name = machine['name']
        print(f"\nTrying to install Nginx on '{name}'..")
        # time.sleep(1)
        result = subprocess.run([bash_script_file, name], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Script failed for '{name}': {result.stderr}")
        else:
            logging.info(f"Script executed for '{name}': {result.stdout.strip()}")

logging.info("Application started")

print(f"\nSee '{logs_file}' for execution information, errors, and results.")
#time.sleep(3)
provision_machines()
run_bash_script()

logging.info("Application run has been completed")