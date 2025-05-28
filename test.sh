#!/bin/bash 

#Author: Yoko Parks
#Class:  CSCD 330 EWU Tony Espinoza 
#Date:   1st May 2025

test_num=3

test1=http://httpforever.com/
test2=http://theoldnet.com/
test3=http://web.simmons.edu/


for((i = 1; i < test_num + 1; i++));

do 
   
   url_var="test$i"
   url="${!url_var}"


# File output test
   echo "******************************"
   echo "Starting file out test $i: $url "
   echo "******************************"
   sleep 1
   python3 lab4.py -f 80 "$url"
  
  

# Print to console test
   echo "**************************************"
   echo "Starting print to screen test $i: $url "
   echo "**************************************"
   sleep 2
   python3 lab4.py -p 80 "$url"

  


done 


