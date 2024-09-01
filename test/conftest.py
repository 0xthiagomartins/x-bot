import os, sys

# Get the current directory (test folder)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the root path to the parent directory
root_path = os.path.dirname(current_dir)

# Add the root path to sys.path
sys.path.insert(0, root_path)
