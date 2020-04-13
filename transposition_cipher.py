

import numpy as np 



def transposition_cipher_col(message, key):
    cols_num = len(key) 

    message += '*' * (cols_num - (len(message) % cols_num))
    message = np.array([c for c in message] )
    
    col_idx= np.arange(0, len(message)) % cols_num 

    out_message= message.copy()
    for i, k in enumerate(key):
        i_indecies= np.where(i == col_idx )[0]
        k_indecies= np.where((k) == col_idx )[0]
        out_message[i_indecies] = message[k_indecies]
    
    return ''.join(out_message) 

def transposition_cipher_row(message, key):
    rows_num = len(key) 
    cols_num = math.ceil(len(message) / len(key)) 
    if len(message)/len(key) != float(len(message)//len(key)):
        print("error")

    message += '*' * (rows_num - (len(message) % rows_num))
    message = np.array([c for c in message] )
    
    col_idx= np.array([(x//cols_num) for x in range(len(message))])

    out_message= message.copy()
    for i, k in enumerate(key):
        i_indecies= np.where(i == col_idx )[0]
        k_indecies= np.where(k == col_idx )[0]
        out_message[i_indecies] = message[k_indecies]
    
    return ''.join(out_message) 


'''
not working 
def transposition_cipher_double(message, enc_col_key, enc_row_key):
    encrypted_by_col_transposition = transposition_cipher_col(message, enc_col_key)
    
    encrypted_by_double_transposition = transposition_cipher_row(encrypted_by_col_transposition, enc_row_key)
    
    return encrypted_by_double_transposition

def decrypt_transposition_cipher_double(enc_message, dec_row_key, dec_col_key):
    decrypted_from_row_transposition = transposition_cipher_row(enc_message, dec_row_key) 
    
    decrypted_from_double_transposition = transposition_cipher_col(decrypted_from_row_transposition, dec_col_key) 
    
    result = ""
    for c in decrypted_from_double_transposition:
        if c != "*" : result += c
    return result 

'''

message = "ENEMY ATTACKS TO NIGHT"
enc_col_key = [0, 1, 3, 2]
enc_row_key = [3, 1, 4, 5, 2, 0] 


col_enc = transposition_cipher_col(message, enc_col_key)
row_enc = transposition_cipher_row(message, enc_row_key)

dec_row_key = [5, 1, 4, 0, 2, 3]
dec_col_key = [0, 1, 3, 2]

col_dec = transposition_cipher_col(col_enc, dec_col_key) 
row_dec = transposition_cipher_row(row_enc, dec_row_key) 
