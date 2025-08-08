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
