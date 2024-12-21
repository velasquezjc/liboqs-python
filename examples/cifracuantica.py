import time
from oqs import OQS

# Inicializar el esquema de cifrado
kem = OQS.KEM("NTRU-HRSS-701")

# Generar clave pública y privada
inicio = time.time()
public_key, private_key = kem.keypair()
fin = time.time()

print("Tiempo generacion par keys: ", fin-inicio)

# Mensaje a cifrar
message = b"Hola, este es un mensaje secreto."

# Cifrar el mensaje
ciphertext = kem.encapsulate(public_key)

# Descifrar el mensaje
decapsulated_message = kem.decapsulate(ciphertext, private_key)

print("Cifrado Cuántico:")
print("Mensaje original:", message)
print("Mensaje cifrado:", ciphertext)
print("Mensaje descifrado:", decapsulated_message)