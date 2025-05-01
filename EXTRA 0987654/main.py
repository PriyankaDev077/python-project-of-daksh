def mirrorChars(input,k):
 
    # create dictionary
    original = abcdefghijklmnopqrstuvwxyz
    reverse = zyxwvutsrqponmlkjihgfedcba
    dictChars = dict(zip(original,reverse))
    
    prefix = input[0:k-1]
    surfix = input[k-1:]
    mirror = ''

    for i in range(0,len)(suffix):
         mirror = mirror + dictChars[suffix[i]]
 
    # concat prefix and mirrored part
    print (prefix+mirror)
          
# Driver program
if __name__ == "__main__":
     input = 'letter'
     k = 3
     mirrorChars(input,k)
