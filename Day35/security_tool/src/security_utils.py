def is_valid_port(port):
    return isinstance(port,int) and 1 <= port <= 65535
def classify_status_code(status_code):
    if 200 <= status_code < 300:
        return "Success"
    if 400 <= status_code < 500:
        return "Client_error"
    if 500 <= status_code < 600:
        return "server_error"
    return "Other"