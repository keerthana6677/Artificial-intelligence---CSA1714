planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

terrestrial(mercury).
terrestrial(venus).
terrestrial(earth).
terrestrial(mars).

gas_giant(jupiter).
gas_giant(saturn).

ice_giant(uranus).
ice_giant(neptune).

planet_position(Name, Position) :-
    planet(Name, Position).