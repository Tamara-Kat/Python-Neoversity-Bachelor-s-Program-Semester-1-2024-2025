import sys

print(sys.argv)

# for arg in sys.argv:
#   print(arg)

if sys.argv[1] == "--help":
  print("Help")
elif sys.argv[1] == "--version":
  print("Version")