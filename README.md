# RGBLights
Child repository of SpotifyRGB

This python program attempted to ask wolframalpha for a constant that would make this function true:
`integral(max(0,sin(x) + CONSTANT),0,2*pi) / integral(abs(sin(x) + CONSTANT),0,2*pi)`
This was in an attempt to map this function to several pins on an arduino that were controlling the R, G, and B pins for an LED light strip. I eventually realised that even if I solved
the function, there was no way I could perform this type of arbitrarily advanced calculus on an arduino. I fixed the problem by buying N-Channel Mosfets, they were like $2.00 per.

Moral of the story, sometimes you just gotta spend a 'lil money.
