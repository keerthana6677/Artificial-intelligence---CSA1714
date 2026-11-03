% Backward Chaining Program

% Facts
parent(john, mary).
parent(mary, sam).
parent(john, david).

% Rules
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

ancestor(X, Y) :-
    parent(X, Y).

ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% Backward chaining query rule
related(X, Y) :-
    ancestor(X, Y).
