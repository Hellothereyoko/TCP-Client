
#!/usr/bin/env python3

'''
Author: Yoko Parks 
Class:  CSCD 330 EWU Tony Espinoza
Date: 30th April 2025 
'''


from sys import argv
from socket import *
from urllib.parse import urlparse



# STEP 0: SETUP
def setup():

# !!! LENGTH ERROR CHECK !!!
   if len(argv) != 4:
      print("SYNTAX_ERR: Expected 3 arguments: -p/-f <port> <url>")
      exit(1)


   # Assign Args To Variables
   output_flag = argv[1] 
   port = int(argv[2])
   url = argv[3]


   # !!! ERROR HANDLING FOR FLAG !!!
   if output_flag not in ["-p", "-f"]:
      print(f"SYNTAX_ERR: Invalid Flag, use -p or -f")
      exit(1)

   else:
      return output_flag, port, url



# STEP 1: ESTABLISH TCP CONNECTION
def tcp_init(url, port):
   
   # Parse The URL
   parsed = urlparse(url)
   hostname = parsed.hostname
   
   # !!! ERROR CHECK FOR INVALID URL !!!
   if not hostname:
      print(f"SYNTAX_ERR: Invalid URL")
      exit(1)

   try:
      # Resolve IP From Domain 
      ip = gethostbyname(hostname)
   
   
   # !!! ERROR HANDLING FOR DOMAIN RESOLUTION !!!
   except:
      print(f"RUNTIME_ERR: Domain Can't Be Resolved")
      exit(1)
   
   # Establish TCP Connection
   try:
      # Create Socket Object
      srvr_socket= socket(AF_INET, SOCK_STREAM)

      # Connect to Server
      srvr_socket.connect((ip, port))
   
      # Return socket and parsed obj
      return srvr_socket, parsed
   
   
   # !!! ERROR HANDLING FOR CONNECTION !!! 
   except:
      print(f"COMMUNICATION_ERR: Connection Failed")
      exit(1)



# Step 2: Create & Send an HTTP GET REQUEST
def query_site(srvr_socket, parsed):

   # Decipher Site Path(s) If Applicable   
   path = parsed.path if parsed.path else "/"
   host = parsed.hostname

   # GET Request Built Here
   request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

   try:
      # Request Encoded Data From Site 
      srvr_socket.send(request.encode())
      
      # Return Status
      return True
   
   
   # !!! ERROR HANDLING FOR UNREACHABLE DATA !!!
   except:
      print(f"COMMUNICATION_ERR: Can't Fetch Data")
      exit(1)
   


# Step 3: Receive Full WebPage
def get_webpage(srvr_socket):
   
   try:
      # Final Output Init
      final_output = ""
   
      # Loop and Receive Until Data is Completed using bool passed by prior function
      while True:
   
          # Start To Get Response 
          response = srvr_socket.recv(4096)
   
          # Break Condition
          if not response:
             break;
         
          # Keep Adding Data to Final Response
          final_output += response.decode()
          #DEBUG: response = srvr_socket.recv(4096)
      
      # Return Final Response
      return final_output
          
   
   # !!! ERROR HANDLING FOR WEIRD/INCOMPLETE RESPONSES !!!
   except:
      print(f"DECODE_ERR: Data Parsing Failed")
      exit(1)



# Step 4: Output to STDOUT or output.txt
def get_output(output_flag, final_output):

      # Look For output_flag To Determine What To Do
      if output_flag == "-p":
         print(final_output)

      if output_flag == "-f":
         try:
            # Appends to avoid overwriting during testing 
            with open("output.txt", "a") as file:

               # Appends to Document & Adds Terminator for ease of reading
               file.write(final_output + "\n")
               file.write("")
               file.write("****** END OF DOCUMENT ******\n")
               file.write("")
               print(f"File Saved!")


         # !!! ERROR HANDLING FOR FILE WRITING !!!        
         except:
            print(f"FILESYS_ERR: Error Writing To File")
            exit(1)
   








def main():
   # Do Setup
   output_flag, port, url = setup()   

   # Begin TCP
   srvr_socket, parsed  = tcp_init(url, port)
   
   # Query Site for Info via HTTP
   query_site(srvr_socket, parsed)   

   # Get Response
   response = get_webpage(srvr_socket)

   # Trim Excess Data
   headers, html = response.split("\r\n\r\n", 1)

   # Close Connection
   srvr_socket.close()

   # Data Output  
   get_output(output_flag, html)

   


if __name__ == "__main__":
   
   main()

