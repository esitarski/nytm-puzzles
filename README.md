# nytm-puzzles
html/javascript programs that solve puzzles in the New York Times Magazine Puzzle Page

A collection of solvers for New York Times Magazine Puzzles, written in html/javascript.

To use, download the html file, then open it in a browser.

For Gas Lines and Yin Yang, the solvers use a constraint-based with back-tracking algorithm (trying every possibility would be infeasible).
Although the approach is effective (typically solving the problems in under a millisecond), it can make mistakes
in early stages which can take a relatively __long__ time to fix.

As the puzzle gets filled in, solution possibilitiees are reduced.  Additionally, the algorithm's feasibiliy tests can trim the decision tree.

For this reason, and to guard against pathologically designed puzzles, the algorithm makes a random choice between what it considers equivalent options.
So, sometimes the problem is solved much faster between involations if the algorithm "gets lucky" in the initial stages.

Ideally there would be a better way to prioritize decisions in early stages (perhaps some grid weighting approach).  Perhaps there is a way for the algorithm to repair bad
sections of the grid rather than doing a lengthy backtrack back to the bad decision.  Or, maybe the answer is just to start a bunch of web workers in parallel with different random number seeds and
stop when the first solution is found.

Please take these programs the right way - a way of experiencing and enjoying the puzzles, with credit to the puzzle creators.

I acknowledge that humans puzzle solvers likely don't approach the problems in any way similar to the algorithms.
Perhaps one day I will understand how anyone does it manually as I have not succeded, and I was able to write the programs in less time.

The best reference is too look at the source code in the html files.  If you have any suggestions or comments, let me know.
