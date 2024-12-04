"""
Guide
  Package Attributes:
    bulky      IF (vol >= 1e6 OR any dim >= 150)
    heavy      IF (mass >= 20)
  Dispatch Statuses:
    standard   IF (NOT bulky OR heavy)
    special    IF (heavy OR bulky)
    rejected   IF (heavy AND bulky)
"""

# Returns dispatch status based on package measurements.
def sort(width, height, length, mass) -> str:
  try:
    # Check invalid package measurements.
    zero = 0 in [width, height, length, mass]
    negative = any(value < 0 for value in [width, height, length, mass])
    if zero or negative:
      return "INVALID"

    volume = width * height * length

    # Check package attributes.
    bulky = volume >= int(10e6) or max(width, height, length) >= 150
    heavy = mass >= 20

    # Return corresponding dispatch status.
    if bulky and heavy:
      return "REJECTED"
    elif bulky or heavy:
      return "SPECIAL"
    else:
      return "STANDARD"

  # Log exception and continue.
  except Exception as e:
    print(f"ERROR: {e}")
    return "INVALID"

packages = [
  # Standard cases
  (100, 100, 100, 10),      # STANDARD
  (200, 50, 50, 10),        # SPECIAL  | bulky
  (50, 50, 50, 25),         # SPECIAL  | heavy
  (200, 200, 200, 30),      # REJECTED | bulky and heavy
  # Edge cases
  (100, 100, 100, 0),       # (+) mass (x) volume | has (x) values.
  (-100, -100, -100, -10),  # (-) mass (-) volume | has (-) values.
  (-100, -100, 201, 10),    # (+) mass (+) volume | has (-) values.
  (-100, 100, 100, 10),     # (-) mass (+) volume | has (-) values.
]

# Sort through packages.
for package in packages:
  print(f"Status: {sort(*package)}\nPackage: {package}\n\n")