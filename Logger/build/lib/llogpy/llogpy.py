try:
    from functools import wraps,partial
    import logging
    import os
    import datetime
    import sys

except Exception as e:
    print('Some Modules are Missings ')

def logMethod(func=None, prefix=''):

    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = datetime.datetime.now()     # start time
        Tem = func(*args, **kwargs)
        FunName = func.__name__        # get Function Name
        end = datetime.datetime.now()       # End time

        message = """                       # Form Message
            Function : {}
            Execution Time : {}
            Memory: {} Bytes
            Date: {}
            args :{}
            kwargs: {}
            """.format(FunName,
                       end-start,
                       sys.getsizeof(func),
                       start,
                       args,
                       kwargs)

        cwd = os.getcwd()                       # get CWD
        folder = 'Logs'                         # Create Folder Logs
        newPath = os.path.join(cwd, folder)     # change Path

        try:
            """ try to create directory """
            os.mkdir(newPath)                   # create Folder

        except Exception as e:

            """ Directory already exists """

            logging.basicConfig(filename='{}/log.log'.format(newPath), level=logging.DEBUG)
            logging.debug(message)

        return Tem

    return wrapper

def logClass(cls):

    for key,value in vars(cls).items():
        if callable(value):
            setattr(cls, key, logMethod(value))
    return cls
