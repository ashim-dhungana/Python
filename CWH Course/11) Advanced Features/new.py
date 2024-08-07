#walrus operator
if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements, expected <=3)")


#Match Case (Switch Case)

def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(404))
