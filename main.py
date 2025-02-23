import itertools
import numpy as np
from collections import Counter
import re

def vigenere_encrypt(text, key):
    encrypted_text = ""
    key = key.upper()
    text = text.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    decrypted_text = ""
    key = key.upper()
    text = text.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

def kasiski_examination(ciphertext):
    # Find repeating sequences of three letters
    sequences = {}  
    for i in range(len(ciphertext) - 2):
        triplet = ciphertext[i:i + 3]
        if triplet in sequences:
            sequences[triplet].append(i)
        else:
            sequences[triplet] = [i]
    
    # Calculate distances between repetitions
    distances = []
    for seq, indexes in sequences.items():
        if len(indexes) > 1:
            for j in range(len(indexes) - 1):
                distances.append(indexes[j + 1] - indexes[j])
    
    # Find the greatest common divisor of distances
    gcd_counts = Counter()
    for d in distances:
        for i in range(2, d + 1):
            if d % i == 0:
                gcd_counts[i] += 1
    
    return gcd_counts.most_common()

def transposition_encrypt(text, key):
    num_cols = len(key)
    num_rows = int(np.ceil(len(text) / num_cols))
    padded_text = text.ljust(num_cols * num_rows, '_')
    
    matrix = np.array(list(padded_text)).reshape((num_rows, num_cols))
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    encrypted_text = "".join("".join(matrix[:, i]) for i in sorted_key_indices)
    return encrypted_text

def transposition_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = int(np.ceil(len(ciphertext) / num_cols))
    matrix = np.empty((num_rows, num_cols), dtype=str)
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    index = 0
    for i in sorted_key_indices:
        for j in range(num_rows):
            if index < len(ciphertext):
                matrix[j, i] = ciphertext[index]
                index += 1
    
    decrypted_text = "".join("".join(row) for row in matrix)
    return decrypted_text.replace('_', '')

def create_table_cipher(text, key):
    matrix_size = int(np.ceil(len(text) ** 0.5))
    matrix = np.full((matrix_size, matrix_size), '_', dtype=str)
    
    index = 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            if index < len(text):
                matrix[i, j] = text[index]
                index += 1
    
    return "".join(matrix[i, j] for j in range(matrix_size) for i in range(matrix_size))

# Example usage
test_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key_vigenere = "CRYPTOGRAPHY"
encrypted_vigenere = vigenere_encrypt(test_text, key_vigenere)
decrypted_vigenere = vigenere_decrypt(encrypted_vigenere, key_vigenere)

key_transposition = "SECRET"
encrypted_transposition = transposition_encrypt(test_text, key_transposition)
decrypted_transposition = transposition_decrypt(encrypted_transposition, key_transposition)

key_table = "MATRIX"
table_cipher_text = create_table_cipher(test_text, key_table)

print("Vigenere Encrypted:", encrypted_vigenere)
print("Vigenere Decrypted:", decrypted_vigenere)
print("Transposition Encrypted:", encrypted_transposition)
print("Transposition Decrypted:", decrypted_transposition)
print("Table Cipher:", table_cipher_text)
