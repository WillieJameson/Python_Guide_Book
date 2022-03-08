import sys

try:
  1/0
except:
  err = sys.exc_info()
  for e in err:
    print(e)

# exc_info returns a three-valued tuple where the first value indicates the exception’s type, the second details the exception’s value, and the third contains a traceback object that provides access to the traceback message (should you need it)