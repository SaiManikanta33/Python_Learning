1. What is logging?

Logging is the process of recording events that happen while a program is running.

instead of printing:

print("User logged in)

professional applications use logs

2026-08-01 10:20:15 INFO User admin logged in

Logs help developer and security analyst:
--> Debug applications
--> investigate incidents
--> Detect attacks
--> Monitor systems
--> Create audit trails

2. Log Levels
Python provides several log levels:

    Level           Purpose
 -  DEBUG           Deatiled debugging information
 -  INFO            Normal application events
 - WARNING         Something unexpected happened
 - ERROR           An operation failed
 - CRITICAL        Serious that may stop the program