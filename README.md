# nytm-puzzles
html/javascript programs that solve puzzles in the New York Times Magazine

A collection of solvers for New York Times Magazine Puzzles, written in html/javascript.

To use, download the html file, then open it in a browser.

For Gas Lines and Yin Yang, the solvers use a constraint-based with back-tracking (trying every possibility would be infeasible).
Although the approach is effective (typically solving the problems in under a millisecond), it can make mistakes
in early stages which can take a relatively __long__ time to fix.

As the puzzle gets filled in, solution possibilitiees are reduced.  Additionally, the algorithm's feasibiliy tests begin to trim the decision tree.

For this reason, and to guard against pathologically designed puzzles, the makea a random choice between what it considers equivalent options.
This means that sometimes the problem is solved much faster if the algorithm "got lucky" in the initial stages.

Ideally there would be a better way to prioritize decisions in early stages (perhaps some grid weighting approach).  Alternatively, perhaps there is a way for the algorithm to repair bad
sections of the grid rather than doing a lengthy backtrack back to the bad decision.

Finally, please take these programs the right way - a way of experiencing and enjoying the puzzles, with credit to the puzzle creators.

I acknowledge that humans puzzle solvers likely don't approach the problems in any way similar to the algorithms.
Perhaps one day I will understand how anyone does it manually as I have not succeded, and I was able to write the programs in less time.

If you have any suggestions or improvements, let me know.
