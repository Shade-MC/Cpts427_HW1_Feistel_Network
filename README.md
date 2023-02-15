# Cpts427_HW1_Feistel_Network

Assignment Description
In this assignment, you will be designing your own simple cipher to show you understand how the Feistel structure works.

You will create the following:

A key schedule based on the bits of your name
A round function (F) which will be very simple
Note: the requirements for the key schedule are chosen to make cheating less appealing. The cipher you create here will be completely insecure. Do not use it to encrypt anything you care about. It is vulnerable to linear cryptanalysis.

You will wrap your key schedule and round function in a working Feistel cipher that I can run on text to encrypt and decrypt it.

The Cipher
The cipher will be a 16-bit block cipher. All the cipher operations will have a structure based on your name. You must calculate the following:

Get the 8-bit ascii values from the first 4 bytes of your full name name in uppercase
Then, use the following table of primes: https://primes.utm.edu/lists/small/1000.txt (Links to an external site.)

For each byte of your first name, calculate prime[ byte - 64 ]
So if the first letter of your first name is "B", that is ascii 66, 66 - 64 = 2, So you will use prime[ 2 ] = 5 for that letter. (note: we are getting the 2nd index in the prime list, assuming that the first prime is 0th, don't use 2 as the prime number itself)

In a comment line at the top of the program, write the following:

Your full name
The programming language and version you are using (very important!)
Your section (CS 427 or CS 527, choose the one that applies to you)
The first 4 letters of your first name as upper case, the 4 indexes into the prime table, the 4 primes you got
If either name isn't long enough, pick random numbers between 1 and 26 inclusive to fill it out (but start with your actual name).

Example: Bob Bobbersson would write the following
# Bob Bobbersson
# Python 3 <-- must include the version! python 2 is different!
# CS 427
# BOBB; 2 15 2 2; 5 53 5 5

The cipher

The key must be 16-bits. We will break the key into 4 subkeys with this schedule:
SubkeyN = lowerbyte( ActualKey rol (N  * 4) ) xor lowerbyte( NamePrimesN )

The first round is round 0. The last is round 3. So your subkeys should be calculated with N = 0, 1, 2, and 3.

Use bitwise masks to compute lowerbyte(). We want the least significant 8 bits from the 16 bit key after rolling it.

The round function F will be:
F( ki, m ) = ( ki xor m )

There will be no initial or final permutation.

Your system will use 4 rounds.

Mode of operation

The cipher will use "counter mode". Implement counter mode so that each cipher block is different even if the plain blocks are the same. The grader will be checking to make sure you did not use ECB mode. In counter mode, encryption is the same as decryption, so you will not need to run your cipher's key schedule in reverse. (note: this makes the Feistel structure kind of pointless, but it's still a good exercise to make sure you understand Feistel networks and CTR).

Input
I will call your program with the following usage:
standard input will consist of: nonce key message
example: 0123 fe23 a0f3d2219c
and the output may be something like
ffaed0113b

Note: these outputs are random numbers. Don't think you will get the same thing.

Because all block ciphers in counter mode are invertible, I should be able to send
0123 fe23 ffaed0113b to standard input
and get
a0f3d2219c [the original message]

Usage
Read from standard input, not from the command line. If you want to test your project like this without using ideone.com, use the "echo" command to send data to standard input:

echo nonce key message | your_prog

For example:

echo 0123 fe23 ffaed0113b | my_prog
might return a0f3d2219c 

IDEone lets you write in standard input directly.

You are responsible for testing your program on IDEone before sending it in.

Before you implement counter mode you may want to have encrypt/decrypt modes to make sure your Feistel network works correctly. However, in counter mode, there is no difference between encryption and decryption.

note: the input and output will be hex, not ASCII, to prevent non-printable garbage from being in the string. Do not print the 0x. Assume the user will type in hex without the 0x. Your code must work regardless of case.

You may assume that hex characters always come in pairs. If you receive an input like af4 you may print an error.

"af44" and "af" are both valid messages. Each block is 4 hex characters. Use zero padding to make the input be a list of blocks (i.e., if I say "af" as the message, pad that to "af00").