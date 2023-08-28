takes(raghu, csa24).
takes(ramu, cs265).
takes(rohan, cse302).
takes(raja, uba254).
classmates(X, Y) :- takes(X, Z), takes(Y, Z).
