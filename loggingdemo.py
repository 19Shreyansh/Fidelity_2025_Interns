#Logging specail file , above 30 you can't neglect.
#critical=50
#error=40
#warning=30
#info=20
#debug=10
#notset=0

import logging 
logging.basicConfig(filename="log.txt",level=logging.WARNING,filemode="w")
print("Logging Demo")
logging.debug("Debug Information")
logging.info("info information")
logging.warning("warning information")