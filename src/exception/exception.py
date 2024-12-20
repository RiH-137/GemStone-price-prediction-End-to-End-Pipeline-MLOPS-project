## this file is used to create custom exception and print the error 
# message with line number and file name

import sys


class customexception(Exception):

    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        print(exc_tb)

        # getting error line no and file name
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))


if __name__=="__main__":
    try:
       #1/0
       pass

    except Exception as e:
        #print(e)
        raise customexception(e,sys)