<h1 align="center">Read-Me!</h1>

## Author: Yoko Parks 
## Class: CSCD 330 EWU Tony Espinoza 
## Date: 1st May 2025 


<br>

<h2 align="left"> About The Program:</h2>

This program is a TCP client in the same class as CURL and WGET written in Python3. 
It retrieves raw HTML via an HTTP GET call. Then the user has the option to print it to screen,
or print it out to a text file (by appending to it) in the program directory.
This client is **ONLY** designed for HTTP & **DOES NOT** include HTTPS functionality.
The client is summoned via the command line interface using the described syntax below. 
Included is a tester script that will attempt 3 different runs of each kind.
</br>


<br>


<h2 align="left">Execution:</h2>

###0) Set up Args to Pass as Variables
###1) Parse URL and correct it if needed
###2) Use Socket to create a TCP connection
###3) Craft & Send an HTTP request
###4) Query a response & receive a webpage if applicable
###5) Print to screen or write to a file called "output.txt"

</br>


<br>

<h2 align="left"> Syntax:</h2>
###python3 lab4.py *(output_flag)*  *(port)*  *(URL)*

</br>


<br>

<h2 align="left">Examples:</h2>

###python3 lab4.py -p 80 http://httpforever.com/  *(prints to screen)* 

###python3 lab4.py -f 80 http://httpforever.com/  *(outputs to file)*

</br>


<br>

<h2 align="center">Laboratory Questions:</h2>

### 1) Why did you have to encode() your request & decode() your response(s)? What do these functions do?

I have to speak to the server in standardized protocols. Each function is pretty self-explanatory, encode translates my machine's string request to a manner that server can understand (bytes). Then, they use that encoding to coordinate the bandwith, packets received, and when to stop communicating. The same can be said for decoding just in reverse. 


  
### 2) What changes would you have to make to create a UDP socket?

I would have to change the request structures & the socket functions. I would also have to change the accepted ports of the program to UDP over TCP. In addition, I might have to slightly tweak the error coding to handle UDP calls instead of TCP. But, overall not too much has to change for the program to accept UDP. 



### 3) If you wanted to create a TCP server, what would you have to change?

The commands I make inside of socket would have to listen instead of calling out.
Basically, I would use establish & listen commands to receive data. Then, and only then can I transmit data to the client. Essentially, I would switch roles and be the server in the 3 way handshake.



### 4) Can your TCP client create or process HTTPS traffic? What happens if you send a request over port 443? 

Since I didn't add HTTPS support, my program will return a DECODE_ERR due to receiving encrypted data. The program will use its internal error checking system to gracefully quit.
In order to add HTTPS support, I would have to implement code to read the port number & generate 
multiple request formats based on it. Then, I would have to change the data decoding to handle encryption.

</br>
