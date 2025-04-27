#!/usr/bin/env python
"""
Tournament Winner

There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.
Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam] , where each team is a string of at most 30 characters representing the name of the team. The results array contains information about the winner of each corresponding competition in the competitions array. Specifically, results [il denotes the winner of competitions [1]. where a 1 inthe results array means that the home team in the corresponding competition won and a o means that the away team won.
It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.

Sample Input

competitions = [
["HTML", "C#"],
["C#", "Python"], ["Python", "HTML"],
]
results = [0, 0, 1]

Sample Output
"Python"
// c# beats HTML, Python Beats C#, and Python Beats HTML.
// HTML - 0 points
// c# - 3 points
// Python - 6 points
"""
from typing import List

# Time Complexity O(n) and Space Complexity is O(n)
def tournamentWinner(competitions: List[List[str]], results: List[int]):
    scores = {"": 0}
    leader = ""
    AWAY_WINNER = 0

    for pos,match in enumerate(competitions):
        home_team, away_team = match
        winner = away_team if results[pos] == AWAY_WINNER else home_team
        if winner in scores:
            scores[winner] += 3
        else:
            scores[winner] = 3
        
        if scores.get(leader) < scores.get(winner):
            leader = winner

    return leader


if __name__ == "__main__":
    result = tournamentWinner([
        ["HTML", "C#"],
        ["C#", "Python"], 
        ["Python", "HTML"]
    ], [0, 0, 1])
    print(result)