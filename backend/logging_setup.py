# import logging
#
# def set_up_logger(name,log_file='server.log',level=logging.DEBUG):
#     #create a custom logger
#     logger = logging.getLogger(name)
#
#     #configure the custom logger
#     logger.setLevel(level)
#     file_handler = logging.FileHandler(log_file)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#
#     return logger
import logging

def set_up_logger(name, log_file="server.log", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # ✅ Prevent adding handler multiple times (duplicate logs)
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


    logger.propagate = False

    return logger
