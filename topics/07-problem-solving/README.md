# Problem-Solving Patterns
## Start with the problem
State the input, output, constraints, and valid edge cases. Write a simple correct solution before improving it. A familiar pattern is a hypothesis, not a correctness proof.

## Patterns to recognize
- **Two pointers:** move positions through a sequence using an ordering or partition invariant.
- **Sliding window:** maintain information about a contiguous range as its endpoints move.
- **Prefix sums:** preprocess cumulative sums to answer range-sum queries efficiently.
- **Divide and conquer:** solve smaller subproblems and combine results.
- **Greedy:** make local choices that require an argument showing they preserve a global optimum.
- **Backtracking:** explore choices and undo them when returning.
- **Dynamic programming:** reuse solutions to overlapping subproblems with an appropriate state and recurrence.

## A small dynamic-programming example
Suppose you can climb one or two steps at a time. Let ways(n) be the number of ways to climb n steps. Set ways(0) = 1 and ways(1) = 1. For n >= 2:
```text
ways(n) = ways(n - 1) + ways(n - 2)
```
The final move must be a one-step or a two-step move. Those possibilities are disjoint, which explains the addition. An iterative solution needs O(n) arithmetic operations and two stored counts; growing integer sizes matter in a bit-level analysis.

## Common mistake
A greedy coin-change strategy can fail: with denominations 1, 3, 4, choosing the largest coin first makes 6 as 4+1+1 instead of 3+3.

## Try it
Define states, base cases, and a recurrence for minimum coin count. State how you represent an unreachable amount.

## Expand next
Dedicated implementations and exercises for each pattern are planned.

[Back to index](../../README.md)
