def get_status(is_busy):
    status = {}
    if is_busy:
        status["status"] = "busy"
    else:
        status["status"] = "available"
    return status
