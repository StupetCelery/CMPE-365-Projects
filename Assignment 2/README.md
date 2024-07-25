Triangle Strips Project

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This code builds triangle strips from a triangle mesh.

A triangle strip is a sequence of triangles, such that each triangle in the sequence shares an edge with the next triangle in the sequence.

It is much more efficient to render a triangle mesh as a set of triangle strips rather than as individual triangles.

These triangle strips are created using a greedy algorithm, an algorithm which builds a solution piece by piece, always choosing the piece that offers the most immediate benefit.
