import json
import sys

import bencodepy 
# import requests - available if you need it!

# Examples:
#
# - decode_bencode(b"5:hello") -> b"hello"
# - decode_bencode(b"10:hello12345") -> b"hello12345"
def decode_bencode(bencoded_value):
    return bencodepy.decode(bencoded_value)
    def decode_string(bencoded_value):
        first_colon_index = bencoded_value.find(b":")
        if first_colon_index == -1:
            raise ValueError("Invalid encoded value")
        return bencoded_value[int(first_colon_index) + 1 :]

    def decode_integer(bencoded_value):
        return int(bencoded_value[1:-1])
    
    if chr(bencoded_value[0]).isdigit():
        return decode_string(bencoded_value)
        
    
    elif chr(bencoded_value[0]) == "i" and chr(bencoded_value[-1]) == "e":
        return decode_integer(bencoded_value)
    
    elif chr(bencoded_value[0]=="l"):
        res = []
        list_str = bencoded_value[1:-1]
        for i in range(len(list_str)):
            if chr(list_str[i]).isdigit():
                string = decode_string(list_str[i:int(list_str[i])+2])
                res.append(string)
                i+=(len(string)+1)
            
         


    else:
        raise TypeError("Only strings are supported at the moment")



def main():
    command = sys.argv[1]

  

    if command == "decode":
        bencoded_value = sys.argv[2].encode()

        
          
        # json.dumps() can't handle bytes, but bencoded "strings" need to be
        # bytestrings since they might contain non utf-8 characters.
        #
        # Let's convert them to strings for printing to the console.
        def bytes_to_str(data):
            
            if isinstance(data, bytes):
                return data.decode()

            raise TypeError(f"Type not serializable: {type(data)}")

    
        print(json.dumps(decode_bencode(bencoded_value), default=bytes_to_str))
    else:
        raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
    main()
