# for test


import os



def run(**args):

   print "[*] In dirlister module"
   files = os.listdir(".")

   return str(files)
"""
def run():
    print 123
"""
if __name__ == "__main__":
   run()

