# 30 day leaderboard

Aims to display top language learners in their respective languages.

### Running unit test
To run unittest to check if the code works as expected:
```shell script
python3 -m unittest test_leaderboard.py 
```

### Thought process
Currently, based on the snippet given, one possible limitation is that it will run at single run time.
But in real production sense, we could always have database to store user actions and query efficiently.

### Implementation
With regards to design patterns, not exactly sure the right term but it most likely a mix of Abstract factory and Singleton approach.
I have a User object to handle user details and id. Also, I have Event object in place with functional check for date range.

To cap it off, I have one callable function to set events list and sort out the user who learns fastest.

The test cases in unit test will provide test implementations of running the 30 day leaderboard.
