# Introduction to programming, computers, basic concepts and numeric systems

In the lecture we took look at what computers are, how do they serve the world and what does it take to write computer code and develop an software application.

There are plenty of materials on the topic but you can start by reading most of it in [Wikipedia](https://en.wikipedia.org/wiki/Software_development).

## Numeric systems
The most common numeric system that everybody around the world understands is decimal. There we have 10 digits that let us count (0..9).  Computers, however, don't understand decimal nativaly. Underneath, computers understand another numberic system to do all its operations called *Binary* and then it is all converted to either *Decimal* or another visual literal or GUI representation so that the person could easily understand, read and interact.

[Here](https://en.wikipedia.org/wiki/Numeral_system) you may read more about Numberic systems.\
[Here](https://en.wikipedia.org/wiki/Binary_number) you may read more about Binary systems.

One of the most import piece is the conversion from one number system to another. Consider the follong formula:

$ X*Y^N + ... + X*Y^2 + X*Y^1 + X*Y^0$\
Where:
* X is the current digit
* Y is the numberic system's max value (will be 10 for decimal)
* N is the current digit's position

or read more [here](https://en.wikipedia.org/wiki/Binary_number#Conversion_to_and_from_other_numeral_systems).