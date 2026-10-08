# Complexity and Correctness
## Core idea
An algorithm is a finite procedure for solving a specified problem. Correctness asks whether it produces the required result. Complexity asks how resource use grows with input size.

## Asymptotic notation
Big O describes an asymptotic upper bound. Big Omega describes a lower bound; Big Theta describes a tight bound. Big O does not itself mean “worst case”: specify whether a claim concerns worst-case, average-case, or amortized cost.

Examples under standard constant-time primitive-operation assumptions:
- Accessing an array element by index: O(1).
- Scanning n elements: O(n).
- Repeatedly halving a search interval: O(log n).
- Comparing every pair: O(n²).

A nested loop is not automatically quadratic; count how many iterations actually occur.

## Correctness tools
A precondition describes valid inputs. A postcondition describes the required output. A loop invariant states a property preserved by each iteration. A termination argument explains why the procedure finishes.

For binary search, maintain the invariant that any possible match remains inside the current candidate interval. Each step preserves that property and shrinks the interval.

## Space
Distinguish input storage, output storage, and auxiliary space. Recursive calls also consume space. State which kind your analysis counts.

## Try it
A loop doubles a counter from 1 until it reaches n. How many iterations occur? What changes if each iteration scans n items?

## Expand next
Recurrences; amortized analysis; mathematical induction; recursion; computational models.

[Back to index](../../README.md)
