def prepareNotification(message, k):
    k -= 3
    temp = ""
    total = 0
    messages = message.split(" ")
    if len(messages[0]) > k:
        return " "
    if len(message) <= k:
        return message
    for i in message:
        if i.isalpha():
            temp += i
        if i == " ":
            if total + 1 + len(temp) > k:
                continue  
            total = total + 1 + len(temp)
            temp = ""
    return message[:total-1] + "..."

print(prepareNotification( "And now here is my secret",15))

print(prepareNotification( "There is an animal with four legs",15))

print(prepareNotification( "super dog",4))

print(prepareNotification( "how are you",20))


# Echo con IA
def prepareNotification(message, k):
    # Espacio disponible antes de los puntos suspensivos
    available = k - 3
    if len(message) <= k:
        return message

    words = message.split()
    result = ""
    
    for word in words:
        # Si la palabra no cabe ni sola, devolvemos "..."
        if len(word) > available:
            return " "
        # Si agregar esta palabra excede el límite, paramos
        if len(result) + (len(result) > 0) + len(word) > available:
            break
        # Agregar palabra (con espacio si no es la primera)
        result += (" " if result else "") + word

    return result + "..."

# Pruebas
print(prepareNotification("And now here is my secret", 15))   # "And now..."
print(prepareNotification("There is an animal with four legs", 15)) # "There is an..."
print(prepareNotification("super dog", 4))                    # ""
print(prepareNotification("how are you", 20))                 # "how are you"
