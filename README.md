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
├── scripts/                                    # Bash automation scripts
│   └── install_services.sh                   # Nginx installation automation
├── configs/                                   # Configuration files (auto-generated)
│   ├── instances.json                        # VM specifications storage
│   └── nginx_servers.txt                     # Tracking Nginx installations
├── logs/                                      # Application logs (auto-generated)
│   └── provisioning.log                     # Main application log file
├── src/                                       # Python source modules
│   ├── models.py                             # Pydantic data models and validation
│   └── machines.py                           # Machine creation functionality
├── infra_simulator.py                         # Main application entry point (Pydantic version)
├── infra_simulator_self_data_validation.py   # Backup of original custom validation version
├── requirements.txt                           # Python dependencies
└── README.md                                 # Project documentation
```

## Features

### 🔧 VM Configuration & Validation
- Interactive CLI for defining virtual machine specifications
- Input validation using Pydantic for data integrity
- Support for multiple operating systems (Ubuntu, CentOS, Windows)
- CPU and RAM specification with validation

### 📝 Configuration Management
- JSON-based configuration storage (`configs/instances.json`)
- Persistent VM specification tracking
- Configuration file auto-generation

### 🚀 Service Automation
- Bash script integration for service installation
- Nginx installation automation with intelligent duplicate prevention
- Cross-platform script execution using Python's subprocess module
- Service tracking to avoid redundant installations

### 📊 Logging & Monitoring
- Comprehensive logging system using Python's logging module
- Timestamped log entries for troubleshooting
- Error tracking and success confirmation
- Log file: `logs/provisioning.log`

## Project Evolution

This project has evolved through several development phases, demonstrating iterative improvement and best practices adoption:

### Phase 1: Custom Validation (Preserved in `infra_simulator_self_data_validation.py`)
- **Initial Implementation**: Custom input validation using regular expressions and manual checks
- **Learning Focus**: Basic Python validation techniques and error handling
- **File Preserved**: The original implementation is maintained as a backup for educational reference

### Phase 2: Pydantic Integration (Current `infra_simulator.py`)
- **Modern Validation**: Migration to Pydantic for robust data validation and type safety
- **Enhanced Error Handling**: Automatic validation with detailed error messages
- **Code Simplification**: Reduced code complexity through Pydantic's built-in validators

### Phase 3: Enhanced Service Management
- **Smart Installation Logic**: Bash script now tracks installed services to prevent duplicates
- **Improved Logging**: Better integration between Python and Bash script logging
- **Service Persistence**: Maintains state of installed services across runs

This evolution demonstrates the progression from basic Python concepts to industry-standard practices, making it an excellent learning resource for DevOps development.

## Prerequisites

- **Python 3.7+** (Python 3.8+ recommended)
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

#### On Windows:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Verify you're in the virtual environment (optional)
where python
# Should show: C:\path\to\your\project\venv\Scripts\python.exe
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
# Run the current Pydantic-based version (recommended)
python infra_simulator.py

# Alternative: Run the original custom validation version (for educational comparison)
python infra_simulator_self_data_validation.py
```

> **Note**: The main application (`infra_simulator.py`) uses modern Pydantic validation, while the backup version (`infra_simulator_self_data_validation.py`) demonstrates custom validation techniques. Both versions produce the same functionality but showcase different validation approaches.

### Interactive Workflow

1. **Start the Application**: The tool will prompt if you want to provision machines
2. **Define VM Specifications**: Enter details for each virtual machine:
   - **VM Name**: Must start with a letter, can contain letters, numbers, hyphens, and underscores
   - **Operating System**: Choose from ubuntu, centos, or windows
   - **CPU Cores**: Number of CPU cores (positive number)
   - **RAM**: Memory allocation in GB (positive number)
3. **Validation**: The system automatically validates all inputs using Pydantic
4. **Service Installation**: After VM definition, the tool automatically attempts to install Nginx on each machine
5. **Logging**: All activities are logged to `logs/provisioning.log`

### Example Session

```
Would you like to provision machines? (yes/no) yes

Enter a VM Name: web-server-01
Select the desired OS to be deployed to the VM: (Supported OS: ubuntu/centos/windows) ubuntu
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
# OR
venv\Scripts\activate     # Windows

# Install new packages (only when venv is activated)
pip install package-name

# Update requirements.txt after installing new packages
pip freeze > requirements.txt

# Deactivate virtual environment when done
deactivate

# Remove virtual environment (if needed)
rm -rf venv  # Linux/macOS
# OR
rmdir /s venv  # Windows
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
- **VMSpec**: Pydantic BaseModel with comprehensive field validation
- **Field Validators**: 
  - `validate_name()`: Ensures VM names follow proper naming conventions
  - `validate_os()`: Restricts OS to supported platforms (ubuntu, centos, windows)
  - `validate_positive()`: Ensures CPU and RAM values are positive numbers
- **Type Safety**: Automatic type conversion and validation through Pydantic

### Machine Management (`src/machines.py`)
- **create_machine()**: Factory function for VM dictionary creation
- Logging integration for machine creation tracking
- Clean separation of concerns between validation and object creation

### Main Application (`infra_simulator.py`)
- **Current Version**: Uses Pydantic for modern validation approach
- User input handling with robust error management
- JSON configuration management with safe file operations
- Bash script execution via subprocess with error capture
- Comprehensive logging setup with timestamps

### Legacy Implementation (`infra_simulator_self_data_validation.py`)
- **Backup Version**: Preserves original custom validation logic
- Educational reference for comparing validation approaches
- Demonstrates evolution from manual to framework-based validation

### Automation Scripts (`scripts/install_services.sh`)
- **Smart Installation Logic**: Checks for existing installations before proceeding
- **Service Tracking**: Maintains `nginx_servers.txt` to track installed services
- **Duplicate Prevention**: Avoids redundant installations across multiple runs
- **Integrated Logging**: Seamless log integration with Python application

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
- **Exception Handling**: Try-catch blocks with appropriate error messages

## Future Enhancements

This project is designed to evolve with additional DevOps learning:
- **AWS Integration**: Real cloud resource provisioning
- **Terraform Support**: Infrastructure as Code implementation
- **Docker Integration**: Containerized service deployment
- **Configuration Management**: Ansible or similar tool integration
- **Monitoring**: Real-time infrastructure monitoring

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

## License

This project is for educational purposes as part of a DevOps course.

---

**Note**: This project simulates infrastructure provisioning for learning purposes. No actual cloud resources are created or modified.