RSA Factoring Challenge
Overview
This repository contains solutions and programs related to the RSA Factoring Challenge. The goal of the challenge is to factorize given numbers into products of two smaller numbers, with the added complexity that the factors must be prime.

Table of Contents
Task 0: Factorize all the things!

Usage: python factors.py <file>
Description: Factorizes natural numbers into products of two smaller numbers.
Output format: n=p*q
Task 1: RSA Factoring Challenge

Usage: python rsa.py <file>
Description: Factorizes RSA numbers into products of two prime numbers.
Output format: n=p*q
Usage
To run the programs, use the provided Python scripts (factors.py and rsa.py) with a file containing natural numbers to factor. The numbers should be listed one per line in the file, with no empty lines and no spaces before and after the valid numbers.

Example:

bash
Copy code
$ python factors.py tests/test00
bash
Copy code
$ python rsa.py tests/rsa-1
