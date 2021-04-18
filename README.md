## BIOLETE Alexandru-Eusebiu (334CC)
### Repo made public on April 18, 2021

# Computer Systems Architecture
## First Assignment - Marketplace

The purpose of this assignment was to efficiently use synchronization
elements to implement a concurrent application. I have used the Lock
element to block the access for non-thread safe operations to a single
thread at a time. Some of these non-thread safe operations are addition
and subtraction.
The assignment is a MPMC (Multiple Producer Multiple Consumer) problem
and we use the following classes:
  - Marketplace - synchronizes Producer and Consumer threads,
  registers producers, creates carts for customers;
  - Product;
  - Producer - publishes products and waits;
  - Consumer - adds/removes products to cart and waits
given amounts of time in the process, places orders.

On a lighter note, I do not find the assignment particularily useful
for the career path I would want to follow, but it was useful to learn
more about concurrence.

I consider the implementation quite efficient.

### Resources
-
https://ocw.cs.pub.ro/courses/asc/laboratoare/01
https://ocw.cs.pub.ro/courses/asc/laboratoare/02
https://ocw.cs.pub.ro/courses/asc/laboratoare/03

### Git
-
https://github.com/alexbiolete/Computer-Systems-Architecture-Marketplace.git

