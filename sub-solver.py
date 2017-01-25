# Substitution Ciper Solver
# Matthew Budde
# Started 1.24.17
#
# Takes a message encoded with a 1-to-1 substitution cipher and analyzes the
# text to sucessfully decode the message.

from collections import Counter

GRAMCOUNT = 7

encoded = input( 'Enter the encoded message: ' )
print( encoded )

#encoded = encoded.decode( 'utf8' )

# Find all repeated bigrams
bigrams = []
for i in range( len( encoded ) - 1 ):
    bigrams.append( encoded[i:i+2] )
bigrams = Counter( bigrams ).most_common( GRAMCOUNT )
#print( bigrams )

# Find all repeated trigrams
trigrams = []
for i in range( len( encoded ) - 2 ):
    trigrams.append( encoded[i:i+3] )
trigrams = Counter( trigrams ).most_common( GRAMCOUNT )
#print( trigrams )

# Find all repeated quadgrams
quadgrams = []
for i in range( len( encoded ) - 3 ):
    quadgrams.append( encoded[i:i+4] )
quadgrams = Counter( quadgrams ).most_common( GRAMCOUNT )
#print( quadgrams )
