def validate_port(port: int) -> bool:
    if type(port) is int:
        if  1 <= port <= 65535:
            return True
        else:
            raise ValueError("Niepoprawna wartość")
    else:
        raise TypeError("Niepoprawny typ plików")
    
        
