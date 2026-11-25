def validate_port(port: int) -> bool:
    if type(port) is not int:
        raise TypeError("Podany argument jest nie poprawny")
    
    if port <=0 or port >= 65536:
        raise ValueError("Niepoprawna wartość")

    return True
            
