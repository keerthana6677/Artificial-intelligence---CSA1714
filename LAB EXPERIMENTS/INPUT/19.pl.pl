
% Forward Chaining Program

% Initial facts
fact(a).
fact(b).

% Rules
rule1 :- fact(a), fact(b), write('Conclusion: c is true'), nl.

rule2 :- fact(c), write('Conclusion: d is true'), nl.

% Forward chaining process
forward :-
    rule1,
    assertz(fact(c)),
    rule2,
    assertz(fact(d)),
    write('Forward Chaining Completed'), nl.
