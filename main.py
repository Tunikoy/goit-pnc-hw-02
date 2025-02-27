import itertools
import string
from collections import deque

def vigenere_encrypt(text, key):
    alphabet = string.ascii_uppercase
    encrypted_text = ""
    key = itertools.cycle(key.upper())
    
    for char in text.upper():
        if char in alphabet:
            shift = alphabet.index(next(key))
            encrypted_text += alphabet[(alphabet.index(char) + shift) % 26]
        else:
            encrypted_text += char
    
    return encrypted_text

def vigenere_decrypt(text, key):
    alphabet = string.ascii_uppercase
    decrypted_text = ""
    key = itertools.cycle(key.upper())
    
    for char in text.upper():
        if char in alphabet:
            shift = alphabet.index(next(key))
            decrypted_text += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            decrypted_text += char
    
    return decrypted_text

def transposition_encrypt(text, key):
    rows = [''] * key
    index = 0
    for char in text:
        rows[index] += char
        index = (index + 1) % key
    return ''.join(rows)

def transposition_decrypt(text, key):
    num_rows = key
    num_cols = len(text) // key
    extra_chars = len(text) % key
    
    rows = [text[i * num_cols + min(i, extra_chars):(i + 1) * num_cols + min(i + 1, extra_chars)] for i in range(num_rows)]
    
    return ''.join(itertools.chain.from_iterable(itertools.zip_longest(*rows, fillvalue=''))).replace('_', '')

def table_cipher_encrypt(text, key):
    size = int(len(text) ** 0.5) + 1
    table = [[' '] * size for _ in range(size)]
    
    for i, char in enumerate(text):
        row = i // size
        col = i % size
        if row < size and col < size:
            table[row][col] = char
    
    return '\n'.join([''.join(row) for row in zip(*table)])

def table_cipher_decrypt(text, key):
    size = int(len(text) ** 0.5) + 1
    cols = [''] * size
    index = 0
    
    for i in range(len(text)):
        cols[index] += text[i]
        index = (index + 1) % size
    
    return ''.join(itertools.chain.from_iterable(cols)).replace('_', '')

original_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key = "CRYPTOGRAPHY"
table_key = "MATRIX"

print("\n======================= Vigenere Cipher =======================")
enc_vigenere = vigenere_encrypt(original_text, key)
dec_vigenere = vigenere_decrypt(enc_vigenere, key)
print("Encrypted:", enc_vigenere)
print("Decrypted:", dec_vigenere)

print("\n================== Transposition Cipher ==================")
enc_transposition = transposition_encrypt(original_text, 4)
dec_transposition = transposition_decrypt(enc_transposition, 4)
print("Encrypted:", enc_transposition)
print("Decrypted:", dec_transposition)

print("\n================== Table Cipher ==================")
enc_table = table_cipher_encrypt(original_text, table_key)
dec_table = table_cipher_decrypt(enc_table, table_key)
print("Encrypted:")
print(enc_table)
print("\nDecrypted:", dec_table)