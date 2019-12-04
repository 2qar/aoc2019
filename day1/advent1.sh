#!/bin/bash

# part 1 
let t=0; for i in $(cat advent1.txt); do let "t += i/3-2"; done; echo $t

# part 2
fuel() { echo $(($1/3-2)); }
let t=0; for i in $(cat advent1.txt); do while [ "$(fuel $i)" -gt 0 ]; do let "t +=$(fuel $i)"; i=$(fuel $i); done; done; echo $t
