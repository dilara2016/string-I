def update(position, new_value, string):
    if not (0 <= position < len(string)):
        return "Wrong Input Given"
    return string[:position] + new_value + string[position+1:]

def delete(position, string):
    if not (0 <= position < len(string)):
        return "Wrong Input Given"
    return string[:position] + string[position+1:]

string = "CODINGAL"

print(update(3,'B',string))
print("\n")
print(delete(3,string))