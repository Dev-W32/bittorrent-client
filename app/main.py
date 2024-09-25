import json
import sys

import bencodepy 
# import requests - available if you need it!

bc = bencodepy.Bencode(encoding="utf-8")

# Examples:
#
# - decode_bencode(b"5:hello") -> b"hello"
# - decode_bencode(b"10:hello12345") -> b"hello12345"
def decode_bencode(bencoded_value):
    return bc.decode(bencoded_value)
   

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
                try:
                    return data.decode()
                except UnicodeDecodeError:
                    return str(data)

            elif isinstance(data, dict):
                return {bytes_to_str(key): bytes_to_str(value) for key, value in data.items()}
            elif isinstance(data, list):
                return [bytes_to_str(item) for item in data]
            return data

            

        decoded_value = decode_bencode(bencoded_value)
        print(json.dumps(decoded_value, default=bytes_to_str))
    else:
        raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
    main()
