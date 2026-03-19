def https_status(status):
    match status:
        case 101:
            return "ok"
        case 420 :
            return "case 2 is on way ..."
        case 404 :
            return "case 3 is running...."
        case _:
            return "default status"
        
print(https_status(100))