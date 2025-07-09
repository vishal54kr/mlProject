import logging
import sys

def error_message_detail(error,error_detail: sys):
    """
    Generates a detailed error message.
    
    Args:
        error (Exception): The exception that occurred.
        error_detail (sys): The sys module to access the traceback.
        
    Returns:
        str: A formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name: [{0}]  line number: [{1}] error message: [{2}]".format(
    file_name,exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    """
    Custom exception class that formats error messages.
    
    Args:
        Exception (Exception): The base exception class.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException with a formatted error message.
        
        Args:
            error (Exception): The exception that occurred.
            error_detail (sys): The sys module to access the traceback.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    
    def __str__(self):
        """
        Returns the string representation of the error message.
        
        Returns:
            str: The formatted error message.
        """
        return self.error_message
    
