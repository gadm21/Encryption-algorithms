
import numpy as np 


def rc4(key):
    '''
    param key (str) : encryption key
    '''

    #swaps two numpy-array locations
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    #  INITIALIZATION (2 steps)

    # step 1
    # initialize s-box with 256 bytes and extend the key if it's less than 256 char (byte) long
    s = np.zeros(256, np.uint8)
    k = np.copy(s) 
    key_len = len(key) 
    for i in range(256): 
        s[i] = i
        k[i] = ord(key[ i % key_len] )

    # step 2
    # use k to produce the initial permutation of s-box 
    j = 0
    for i in range(256):
        j = (j + s[i] + k[i]) % 256
        swap(s, i, j) 
    
    print(s) 

rc4("hel")
