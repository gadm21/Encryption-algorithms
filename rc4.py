
import numpy as np 


class RC4(object):

    def __init__(self, key, s_len = 256):

        # TODO : accept other types
        assert isinstance(key, str), "key must be string"
        
        self._key = key 

        self._s_length = s_len
        self._s = np.zeros(self._s_length, np.uint16) 
        self._s_initialized = False 
        self._i = 0
        self._j = 0


    def _swap(self, i, j):
        temp = self._s[i] 
        self._s[i] = self._s[j] 
        self._s[j] = temp 
    
    def _initialize(self):
        
        orig_key_len = len(self._key)
        k = np.copy(self._s) 

        #initialize s and extend key if len(key) < len(s) and copy key in k
        for i in range(self._s_length):
            self._s[i] = i 
            k[i] = ord(self._key[i % orig_key_len])
        

        #use k to produce the first permutation of s 
        j = 0
        for i in range(self._s_length):
            j = (j + self._s[i] + k[i]) % self._s_length 
            self._swap(i, j) 

        self._s_initialized = True 
        #initialization is done at this point. we don't need the key or k anymore.

    
    def get_next(self):

        if not self._s_initialized : self._initialize() 

        self._i = (self._i + 1) % self._s_length
        self._j = (self._j + self._s[self._i]) % self._s_length

        final_index = (self._s[self._i] + self._s[self._j]) % self._s_length 
        result = self._s[final_index ]

        # permute s, this makes s change continously so it's hard to track
        self._swap(self._i, self._j)  
        
        return result 




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
    s = np.zeros(256, np.uint16)
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
    
    
    # at this stage the key: (key) and its extension (k) aren't used anymore

    i = 0
    j = 0
    
    print(s[i])
    j = (j + s[i]) % 256
    print(i, " ", j) 
    print(s[i], " ", s[j])
    t = s[i]
    t = (t + s[j]) % 256
    print(t)
    swap(s, i, j)

    return s[t] 



rc = RC4("hello") 

l = []
for i in range(500): 
    n = rc.get_next() 
    if l.count(n) > 4:
        print(n)
    l.append(n) 

print("len:", len(l))
