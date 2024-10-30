import subprocess

def install_system_packages(packages_file='system_packages.txt'):
    # Update package list
    subprocess.run(['apt-get', 'update'], check=True)
    
    # Read packages file
    with open(packages_file, 'r') as f:
        packages = []
        for line in f:
            # Skip comments and empty lines
            if line.strip() and not line.strip().startswith('#'):
                packages.append(line.strip())
    
    if packages:
        # Convert list to space-separated string
        packages_str = ' '.join(packages)
        # Install packages
        print(f"Installing: {packages_str}")
        subprocess.run(['apt-get', 'install', '-y'] + packages, check=True)
    
    print("System packages installation completed!")
