def resolve_status(status_code):
    if status_code is  None:
        return "UNKNOWN"
    elif status_code >= 200 and status_code <=299:
        return "UP"
    else:
        return "DOWN"  
    
