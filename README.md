# dad_statistics

Tests whether the success rate of multiple rolls can actually be predicted.


For example, when rolling with 1/100 odds, theory suggests that the probability of success increases with every roll.
More specifically, it suggests that the probability of failure decreases as the number of rolls increase.

To calculate the change in probability, you need to begin with the probability that a roll will NOT be successful.
So, for 1/100 odds, the probability of failure is 99/100, or 0.99

From here, basic probability calculations apply. So, after two rolls, the probability of failure decreases from 0.99 to (0.99 X 0.99, or 0.99^2) ~= 0.98.
For three rolls, the probability of failure decreases to (0.99 X 0.99 X 0.99, or 0.99^3) ~= 0.97, etc.

Across multiple rolls, 1/100 odds (or 99/100 probability of failure) changes substantially according to this theory. 
For example, after 69 rolls, the probabiliy calculation becomes 0.99^69, which roughly equals 0.5 or 50/100.

Some people find this theory to be unconvincing, arguing that since every roll is a discrete event (e.g., previous rolls have no bearing on subsequent rolls),
the idea that multiple rolls actually change the odds of success doesn't make sense. 

This program tests that idea. A large number of rolls are made by default (1 million), and when a rolls is successful the roll number is appended to a list.
Then, the percentage of successful rolls that occur at or before the midpoint (in the case of 1/100 odds, at or before 69 rolls) over the total number of successful
rolls is calculated and printed out.

Several further statistics are printed (e.g., min and max number of rolls for a success to occur), and the option to create a scatter plot is also included.
All variables can be easily changes (e.g., total rolls, odds, and cutoff point for probability calculation), allowing the theory to be tested in multiple ways.
