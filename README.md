# Home Service Pricing Module

This Python project simulates pricing calculations for a small home service company.  
It includes a main module (`pricing.py`) with well-structured functions and a separate testing file (`test_pricing.py`) using Python’s built-in `unittest` framework.


## Project Overview

The **Pricing Module** demonstrates:
- Clean function design and input validation  
- Conditional logic and arithmetic operations  
- Structured automated testing with `unittest`  

This small system calculates costs for floor cleaning, roof inspection, appliance installation, and yard cleanup.

## Features

### clean_floor(area)
- Calculates cost based on square footage.  
- $200 for the first 500 sq ft  
- +$100 for every additional 250 sq ft  

###  inspect_roof(material)
- Returns the inspection price by roof type.  
- “tile” → $500  
- “shingle” → $600  
- Any other input → -1  

### install_appliances(number_appliance, haul_old_appliance=False)
- $100 per appliance  
- +$500 if hauling away old appliances  

### yard_cleanup(front_area, back_area)
- Calculates cost based on total yard area.  
- Returns $300 if ≤ 800 sq ft  
- Adds $50 per 200 sq ft beyond 800  

## Example Usage

from pricing import clean_floor, inspect_roof, install_appliances, yard_cleanup

print(clean_floor(750))              # Output: 300
print(inspect_roof("tile"))          # Output: 500
print(install_appliances(3, True))   # Output: 800
print(yard_cleanup(300, 400))        # Output: 300