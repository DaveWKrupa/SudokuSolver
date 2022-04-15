import sys


class ExceptionString:
    @staticmethod
    def get_exception_string(err):
        # get details about the exception
        err_type, err_obj, traceback = sys.exc_info()

        # get the line number when exception occurred
        line_num = traceback.tb_lineno
        return f"ERROR: {err}"






