import re
import logging
import json
import os
from src.machines import create_machine

# Define script paths
base_dir = os.path.dirname(os.path.abspath(__file__))
# instances.json config file path config
configs_dir = os.path.join(base_dir, "configs")
json_config_file = os.path.join(configs_dir, "instances.json")
# provisioning.log file path config
logs_dir = os.path.join(base_dir, "logs")
logs_file = os.path.join(logs_dir, "provisioning.log")

# Create log and config dirs if not exists
os.makedirs(configs_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)
   
# Define logging configuration
logging.basicConfig(
    level=logging.INFO,                            # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Omit milliseconds
    filename=logs_file,                            # Send teh logs to the log file
    filemode='a'                                   # For appending the data in file
)

logging.info("Application started")

# VM name input validation
def validate_vm_name(vm_name):
    vm_name = vm_name.strip()

    if not vm_name:
        logging.warning(f"An empty string '{vm_name}' was inserted as an input for the VM name which is prohibited.")
        return False
    if vm_name.isdigit():
        logging.warning(f"A pure number string '{vm_name}' was inserted as an input for VM name which is prohibited")
        return False  # Pure numbers are invalid
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9\-_]*$', vm_name):
        logging.warning(f"The inserted VM name input '{vm_name}' is not according to the following VM name convention: VM name must start with a letter, allow letters, numbers, hyphens, and underscores.")
        return False  # Must start with a letter, allow letters, numbers, hyphens, and underscores
    
    # If all above validations passed successfully
    logging.info(f"Inserted VM name: '{vm_name}'")
    return True

# OS name input validation
def validate_os_name(os_name):
    os_list = ["ubuntu", "centos", "windows"]
    if os_name in os_list:
        logging.info(f"Inserted OS name: '{os_name}'")
        return True
    else:
        logging.warning(f"Inserted OS input value '{os_name}' doesn't exist or not included in the list of supported OS for the VM creation. \nThe app only accepts one of the follwoing operation systems: 'Ubuntu', 'Centos' or 'Windows'.")
        return False

# CPU and RAM input validation        
def validate_specs(spec_type, spec_amount):
    try:
        spec_amount = float(spec_amount)
        if spec_amount <= 0:
            logging.warning(f"The inserted input value '{spec_amount}' for '{spec_type}' Value must be higher than 0. ")
            return False
        else:
            logging.info(f"{spec_type}: '{spec_amount}'")
            return True
    except ValueError:
        logging.warning(f"Invalid '{spec_type} 'input '{spec_amount}' was inserted. Please enter a numeric value.")
        return False

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
        user_input = input("Would you like to provision machines? (yes/no) ").lower().strip()
        if user_input == "yes":
        #user_input = "yes"
            while True:
                # Take user input for VM deatils and specs            
                name = input("\nEnter a VM Name: ")
                os = input("Select the desired OS to be deployed to the VM: (Supported OS: ubuntu/centos/windows) ").lower().strip()
                cpu = input("Insert the desired number of VM CPU cores (eg: 4): ").strip()
                ram = input("Insert the desired number of RAM to be allocated to the VM (size unit is in GB. eg: 16): ").strip()

                # VM name validation input
                name_return_status = validate_vm_name(name)
                # OS name validation input
                os_return_status = validate_os_name(os)
                # Validate CPU input
                cpu_specs_return_status = validate_specs("VM CPU cores allocation", cpu)
                # Validate RAM input
                ram_specs_return_status = validate_specs("VM RAM allocation", ram)
                
                # If all validations were passed successfully
                while True:
                    if name_return_status and os_return_status and cpu_specs_return_status and ram_specs_return_status:                       
                        # Call the "create machine" module to return a dict from values
                        vm_specs = create_machine(name, os, cpu, ram)
                        
                        # Append VM config to the json config file
                        append_vm_spec(json_config_file, vm_specs)

                        # Check if the user wants to define another machine                       
                        user_input_another_vm = input(f"\nThe VM named '{name}' was created, would you like to define another machine? (yes/no) ")
                        if user_input_another_vm == "yes":
                            break 
                        elif user_input_another_vm == "no":
                            print("\nNo further actions are required")
                            return
                        else:
                            print("\nInvalid answer, try again")
                            continue
                    else:
                        print(f"\nA VM name '{name}' wasn't created due to one or more errors. see '{logs_file}' for details.")
                        logging.critical(f"VM name '{name}' wasn't created due to one or more errors.")
                        exit()
        elif user_input == "no":
            print("\nOk. Exiting\n")
            break
        else:
            print("\nInvalid answer. Try again.\n")
            continue

provision_machines()

print("Script contination")
logging.info("Application run has been completed")
