# DevOps Infrastructure Provisioning & Configuration Automation Project

## Overview

This project is a Python-based automation tool developed as part of a DevOps course that simulates infrastructure provisioning and service configuration. It demonstrates fundamental DevOps concepts including infrastructure as code, automation, and modular programming practices.

The tool allows users to define virtual machines (VMs) dynamically, validates input using Python with Pydantic, and automates service installation using Bash scripts. While currently operating in simulation mode, the modular architecture is designed to support future integration with real cloud providers like AWS and Terraform.

## Project Objectives

- **Accept and validate user inputs** for defining virtual machines
- **Implement modular code structure** using Python classes and proper imports
- **Automate service installation** using Bash scripts integration
- **Provide comprehensive logging** and error handling throughout the application
- **Simulate infrastructure provisioning** in preparation for real cloud integration

## Project Structure

```
infra-automation/
├── scripts/                    # Bash automation scripts
│   └── install_services.sh    # Nginx installation automation
├── configs/                    # Configuration files (auto-generated)
│   ├── instances.json         # VM specifications storage
│   └── nginx_servers.txt      # Tracking Nginx installations
├── logs/                      # Application logs (auto-generated)
│   └── provisioning.log      # Main application log file
├── src/                       # Python source modules
│   ├── models.py             # Pydantic data models and validation
│   └── machines.py           # Machine creation functionality
├── misc/                      # Additional utilities
│   └── infra_simulator_self_data_validation.py  # Alternative validation approach
├── infra_simulator.py         # Main application entry point
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation
```

## Features

### 🔧 VM Configuration & Validation
- Interactive CLI for defining virtual machine specifications
- Input validation using Pydantic for data integrity
- CPU and RAM specification with validation

### 📝 Configuration Management
- JSON-based configuration storage (`configs/instances.json`)
- Persistent VM specification tracking
- Configuration file auto-generation

### 🚀 Service Automation
- Bash script integration for service installation
- Nginx installation automation with duplicate prevention
- Cross-platform script execution using Python's subprocess module

### 📊 Logging & Monitoring
- Comprehensive logging system using Python's logging module
- Timestamped log entries for troubleshooting
- Error tracking and success confirmation
- Log file: `logs/provisioning.log`

## Prerequisites

- **Python 3.7+** (Python 3.8+ recommended)
- **Python3 venv** (python3 virtual environment package installed)
- **pip** (Python package installer)
- **Bash shell** (for service installation scripts)
- **Git** (for version control)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd infra-automation
```

### 2. Set Up Python Virtual Environment

Creating and using a virtual environment is a best practice that isolates your project dependencies from your system Python installation.

#### On Linux/macOS:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Verify you're in the virtual environment (optional)
which python
# Should show: /path/to/your/project/venv/bin/python
```

### 3. Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
# Check installed packages
pip list

# Should show pydantic and its dependencies
```

## Usage

### Running the Application

Make sure your virtual environment is activated, then run:

```bash
python infra_simulator.py
```

### Interactive Workflow

1. **Start the Application**: The tool will prompt if you want to provision machines
2. **Define VM Specifications**: Enter details for each virtual machine:
   - **VM Name**: Must start with a letter, can contain letters, numbers, hyphens, and underscores
   - **Operating System**: Choose from ubuntu or centos
   - **CPU Cores**: Number of CPU cores (positive number)
   - **RAM**: Memory allocation in GB (positive number)
3. **Validation**: The system automatically validates all inputs using Pydantic
4. **Service Installation**: After VM definition, the tool automatically attempts to install Nginx on each machine
5. **Logging**: All activities are logged to `logs/provisioning.log`

### Example Session

```
Would you like to provision machines? (yes/no) yes

Enter a VM Name: web-server-01
Select the desired OS to be deployed to the VM: (Supported OS: ubuntu/centos) ubuntu
Insert the desired number of VM CPU cores (eg: 4): 2
Insert the desired number of RAM to be allocated to the VM (size unit is in GB. eg: 16): 8

Would you like to provision another machine? (yes/no) no

Trying to install Nginx on 'web-server-01'..
```

### Expected Output Files

After running the application, you'll find:

- **`configs/instances.json`**: Contains your VM specifications in JSON format
- **`configs/nginx_servers.txt`**: Lists machines with Nginx installed
- **`logs/provisioning.log`**: Detailed execution logs with timestamps

## Virtual Environment Management

### Why Use Virtual Environments?

Virtual environments provide isolated Python environments for your projects, preventing dependency conflicts between different projects.

### Managing Your Virtual Environment

```bash
# Activate virtual environment (run this each time you work on the project)
source venv/bin/activate  # Linux/macOS

# Install new packages (only when venv is activated)
pip install package-name

# Update requirements.txt after installing new packages
pip freeze > requirements.txt

# Deactivate virtual environment when done
deactivate

# Remove virtual environment (if needed)
rm -rf venv  # Linux/macOS
```

### Troubleshooting Virtual Environment

If you encounter issues:

```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Code Architecture

### Data Models (`src/models.py`)
- **VMSpec**: Pydantic model with comprehensive validation
- Field validators for name format, OS support, and positive number validation
- Support for Ubuntu and CentOS operating systems

### Machine Management (`src/machines.py`)
- **create_machine()**: Factory function for VM dictionary creation
- Logging integration for machine creation tracking

### Main Application (`infra_simulator.py`)
- User input handling and validation workflow
- JSON configuration management
- Bash script execution via subprocess
- Comprehensive logging setup

### Automation Scripts (`scripts/install_services.sh`)
- Nginx installation automation
- Duplicate installation prevention
- Logging integration with main application

### Additional Utilities (`misc/`)
- **infra_simulator_self_data_validation.py**: Alternative validation approach using custom validation functions

## Logging

The application maintains detailed logs in `logs/provisioning.log` with the following information:
- Application start/stop events
- VM creation and validation results
- Service installation attempts and results
- Error messages with timestamps
- Script execution outcomes

## Error Handling

- **Input Validation**: Pydantic models ensure data integrity
- **File Operations**: Graceful handling of missing or corrupted configuration files
- **Script Execution**: Subprocess error capture and logging
- **Exception Handling**: Try-except blocks with appropriate error messages

## Recent Updates

### Version Updates
- **Removed Windows Support**: The application now supports only Ubuntu and CentOS operating systems
- **Enhanced Project Structure**: Added misc directory for additional utilities
- **Improved Documentation**: Updated README to reflect current project state

## Future Enhancements

This project is designed to evolve with additional DevOps learning:
- **AWS Integration**: Real cloud resource provisioning
- **Terraform Support**: Infrastructure as Code implementation
- **Docker Integration**: Containerized service deployment
- **Configuration Management**: Ansible or similar tool integration
- **Monitoring**: Real-time infrastructure monitoring
- **Multi-Service Support**: Support for additional services beyond Nginx

## Development Guidelines

### Adding New Features
1. Follow the existing modular structure
2. Add appropriate validation using Pydantic
3. Include comprehensive logging
4. Update this README for new functionality

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Include docstrings for complex functions
- Maintain separation of concerns between modules

## Contributing

1. Create a feature branch for new development
2. Follow existing code patterns and structure
3. Add appropriate tests for new functionality
4. Update documentation as needed
5. Submit pull requests for review

## Troubleshooting

### Common Issues

**Virtual Environment Issues:**
```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Permission Issues with Scripts:**
```bash
# Make bash script executable
chmod +x scripts/install_services.sh
```

**Configuration File Issues:**
```bash
# Remove corrupted configuration files (they will be recreated)
rm configs/instances.json
rm configs/nginx_servers.txt
```

### Getting Help

- Check the log file `logs/provisioning.log` for detailed error information
- Verify all prerequisites are installed correctly
- Ensure you're running the application from the correct directory
- Check that the virtual environment is activated

## License

This project is for educational purposes as part of a DevOps course.

---

**Note**: This project simulates infrastructure provisioning for learning purposes. No actual cloud resources are created or modified.
