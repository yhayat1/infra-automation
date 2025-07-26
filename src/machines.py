import logging

def create_machine(name, os, cpu, ram):
    """
    Constructs and returns a dictionary representing a VM spec.
    """
    machine = {
        "name": name,
        "os": os,
        "cpu": cpu,
        "ram": ram
    }
    logging.info(f"Machine created: {machine}")
    return machine