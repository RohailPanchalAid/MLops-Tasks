print("Lab Assignment-1 MLops \n")
#Script to get the pyhton version 
#github mlops assignment repo link : https://github.com/RohailPanchalAid/MLops-Tasks


import sys
import platform
import pkg_resources  # deprecated but works; see note below for modern alternative

# Python version info
print("Python Version:", sys.version)
print("-" * 50 ) ,print("\n")

#Python installed libraries list script
stdlib_modules = sorted(sys.stdlib_module_names)
print(f"Total standard library modules: {len(stdlib_modules)}\n")
for libs in stdlib_modules:
    print(libs) 

