# CS491-Final-Project
# Betting Connect 4

Betting Connect 4 is a game which creates two players "Player 1" and "Player 2" and each have $500 to bet on a game of Connect 4. Once an indivudial wins their bet is doubled and added to the wallet.

## Basic Running Instructions

Below is a list of running instructions for the copying of the Repository.

Manual Running Instructions:
```bash
python3 game.py
```
Manual Running Test Instructions:
```bash
python3 -m unittest test.py
```

## One Click Job Running Instructions

Testing, Coverage, and Deployment all happen upon every commit utilizing GitHub, GitHub Actions, and Docker.
If you would like to rerun all jobs
1. Look for recent commit and see either a "checkmark" or "x", Click.
2. In top right locate button "Re run All Jobs", Click.
3. Look at GitHub Actions to show results.

## Docker Instructions

Pull Docker Image:
```bash
docker pull conway5525/cs491final 
```
Run Docker Image:
```bash
docker run -it conway5525/cs491final:latest
```
