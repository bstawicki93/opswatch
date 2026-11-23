def validate_port(port):
    if  1 <= port <= 65535:
        return True
    else:
        raise ValueError("Niepoprawna wartość")
        
