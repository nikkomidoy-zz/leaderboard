"""
The Speakly team wants to add a new feature to their app: a leaderboard to display the top language learners in their respective languages.
You are tasked with creating a method that, given the different users' histories, will generate a leaderboard that will be displayed in the app.
"""
import itertools

from datetime import datetime, timedelta
from enum import Enum
from typing import List


class BaseUser:
    """
    Abstract class for user id
    """
    id_iter = itertools.count(start=1)

    def __init__(self):
        self.user_id = next(self.id_iter)


class User(BaseUser):
    """
    User object to handle
    """
    def __init__(self, **kwargs):
        super().__init__()
        self.name = kwargs.get('name')


class Action(Enum):
    """
    List of available actions
    """
    learned = 'words_learnt'
    correct = 'correct_answer'
    incorrect = 'incorrect_answer'


class Event(object):
    """
    Event object
    """
    def __init__(self, **kwargs) -> None:
        self.user = kwargs.get('user')
        self.event_date = kwargs.get('event_date')
        self.action_name = kwargs.get('action_name')

    def is_within_30_days_range(self):
        today = datetime.utcnow()
        thirty_days = datetime.utcnow() + timedelta(days=30)
        return today <= self.event_date <= thirty_days


def get_30_day_leaderboard(events: List[Event]) -> List[int]:
    """
    Get 30 day leaderboard for fastest learning users
    :param events: List of users events
    :return: list of user ids for most word learnt
    """
    leaderboard = {}
    for event in events:
        if event.is_within_30_days_range():
            leaderboard.setdefault(event.user.user_id, 0)
            if event.action_name == Action.learned:
                leaderboard[event.user.user_id] += 1

    sorted_board = dict(sorted(leaderboard.items(), key=lambda x: x[1], reverse=True))
    sorted_user_ids = list(sorted_board.keys())

    return sorted_user_ids
