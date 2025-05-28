<h1 align="center">$${\color{red}Read-Me!}$$ </h1>

<br>

<h2 align="center"> $${\color{red}About} {} {\color{red}The} {} {\color{red}Program:}$$ </h2>

This program is a TCP client in the same class as CURL and WGET written in Python3. 
It retrieves raw HTML via an HTTP GET call. Then the user has the option to print it to screen,
or print it out to a text file (by appending to it) in the program directory.
This client is **ONLY** designed for HTTP & **DOES NOT** include HTTPS functionality.
The client is summoned via the command line interface using the described syntax below. 
Included is a tester script that will attempt 3 different runs of each kind.
</br>


<br>


<h2 align="center">$${\color{red}Execution:}$$ </h2>


<h3 align="center"> 
  
1) Parse URL and correct it if needed
2) Use Socket to create a TCP connection
3) Craft & Send an HTTP request
4) Query a response & receive a webpage if applicable
5) Print to screen or write to a file called "output.txt" </h3>

</br>


<br>

<h2 align="center"> $${\color{red}Syntax:}$$ </h2>

  <h3 align="center"> python3 lab4.py *(output_flag)*  *(port)*  *(URL)* </h3>

</br>


<br>

<h2 align="center">$${\color{red}Examples:}$$ </h2>

  <h3 align="center"> python3 lab4.py -p 80 http://httpforever.com/  *(prints to screen)*  </h3>

  <h3 align="center"> python3 lab4.py -f 80 http://httpforever.com/  *(outputs to file)* </h3>

</br>


