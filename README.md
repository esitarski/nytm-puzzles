# nytm-puzzles
html/javascript programs that solve puzzles in the New York Times Magazine

A collection of solvers for New York Times Magazine Puzzles, written in html/javascript.

To use, download the html file, then open it in a browser.

For Gas Lines and Yin Yang, the solvers use a constraint-based with back-tracking (trying every possibility would be infeasible).
Although the approach is effective (typically solving the problems in under a millisecond), it can make mistakes
in early stages which can take a relatively __long__ time to fix.

As the puzzle gets filled in, solution possibilitiees are reduced.  Additionally, the algorithm's feasibiliy tests begin to trim the decision tree.

For this reason, and to guard against pathologically designed puzzles, the choice between indistiguishable decisions are randomized.
This means that sometimes the problem is solved much faster as the algorithm "got lucky" in the initial stages.

Finally, please take these programs the right way - a way of experiencing and enjoying them.
I expect that humans puzzle solvers don't approach the problem in any way similar to the algorithm

And, if you have any suggestions or improvements, let me know.
