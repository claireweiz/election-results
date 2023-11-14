# Description

I have divided the README into two sections: 
* The [first section](https://github.com/claireweiz/election-results#election-results) includes instructions from the [Guardian coding exercises](https://github.com/guardian/coding-exercises). 
* The [second section](https://github.com/claireweiz/election-results#my-solutions) details my thought process for completing this task.

# Election results

It's election night! Exciting! We have a feed of election results from a data supplier. They will supply us a file which will be updated throughout the night as results come in.

## Results format

The fields in the file will be separated by commas but each row will vary in length as described below.

A result will consist of:

1. A constituency
2. A repeating set of pairs with the party code and the votes cast

So for example:

    Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD
    Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind

We want to transform this into a standard result that shows:

* the constituency name
* translates the party code into a full name
* shows the share of the vote as a percentage of all the votes cast

### Codes

* C - Conservative Party
* L - Labour Party
* UKIP - UKIP
* LD - Liberal Democrats
* G - Green Party
* Ind - Independent
* SNP - SNP


# My solutions

Updated Aug 28, 2023

How I did the task:

Imported the raw data of the election results (source.txt)

* Step 1: Transformed the constituency data to the key in the dictionary (data type: string)
* Step 2: Transformed the party code into a full party name (data type: string)
* Step 3: Displayed the vote of each party as a percentage of all the votes (data type: decimal)

The result was a nested dictionary created in this format: {'constituency' : {'party name' : 'percentage of the votes'}}