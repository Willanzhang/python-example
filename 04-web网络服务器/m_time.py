import time
def say_time():
    return time.ctime()

def application(evn, handleDeaders):
    env = {
      "PATH_INFO": fileName
      "QUERY_STRING": param
    }
    status_code = 200
    handleDeaders(status_code,[])
    return time.ctime()