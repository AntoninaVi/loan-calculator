try:
   def exception_test():
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")