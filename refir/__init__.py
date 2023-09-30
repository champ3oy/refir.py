# my_python_package/__init__.py

# You can explicitly specify what modules and classes should be imported
from .refir import Refir
from .constants import ENDPOINTS

# You can also define any initialization code for the package
# This code will be executed when the package is imported

# For example, you can print a welcome message
print("Refir v1.1")

# You can also define variables or constants that should be accessible at the package level
PACKAGE_VERSION = "1.1"
