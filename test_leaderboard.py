import unittest

from datetime import datetime, timedelta

from leaderboard import User, Event, Action, get_30_day_leaderboard


class TestLeaderBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.user1 = User(name='Nikko')
        self.user2 = User(name='Robert')

    def test_valid_leader_board(self):
        day_after_today = datetime.utcnow() + timedelta(days=1)

        events = [
            Event(user=self.user1, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user1, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user1, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user2, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user2, event_date=day_after_today, action_name=Action.learned),
        ]

        user_ids = get_30_day_leaderboard(events)
        assert user_ids == [self.user1.user_id, self.user2.user_id]

    def test_at_least_one_not_within_30_day_range(self):
        yesterday = datetime.utcnow() - timedelta(days=1)
        day_after_today = datetime.utcnow() + timedelta(days=1)

        events = [
            Event(user=self.user1, event_date=yesterday, action_name=Action.learned),
            Event(user=self.user1, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user2, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user2, event_date=day_after_today, action_name=Action.learned),
            Event(user=self.user2, event_date=yesterday, action_name=Action.learned),
        ]

        user_ids = get_30_day_leaderboard(events)
        assert user_ids == [self.user2.user_id, self.user1.user_id]

    def test_no_event_date_within_30_day_range(self):
        yesterday = datetime.utcnow() - timedelta(days=1)

        events = [
            Event(user=self.user1, event_date=yesterday, action_name=Action.learned),
            Event(user=self.user1, event_date=yesterday, action_name=Action.learned),
            Event(user=self.user2, event_date=yesterday, action_name=Action.learned),
            Event(user=self.user2, event_date=yesterday, action_name=Action.learned),
            Event(user=self.user2, event_date=yesterday, action_name=Action.learned),
        ]

        user_ids = get_30_day_leaderboard(events)
        assert user_ids == []


if __name__ == '__main__':
    unittest.main()
