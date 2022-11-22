# Election Analysis

## Overview of Election Audit: 

  The purpose of the election audit analysis was to determine if there was a way automate counting the ballots. Currently the results are counting by 

hand and verified in a excel spread sheet. This is very time consuming and there has to be a better method to counting votes. If the code provided proves 

to be correct then the Colorado election office with use the code in future elections. 


## Election-Audit Results: 

- How many votes were cast in this congressional election? 
   - Total Votes: 369,711
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Which county had the largest number of votes?
  - Largest County Turnout: Denver  
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)  
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  -  Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%  

## Election-Audit Summary: 

As you can see the code we used was very accurate. I purpose that the script can be used for any election moving forward. That said, the script is not 

perfect, but I believe the following modifications can be added to the script to sure up code. Currently the code only handles results from counties. We 

could modify the script so that there is a block of code for each type of election. For example, if just a city wide election we would structure te 

script around precincts. If we were going to use the script for the general election we would also need to introduce the electoral college to the script. 

The most votes a candidate received would result in the candidate winning the state but receiving the value of the electoral college. We would then need 

to sum up all the state won per candidate to see who one the general election. 
