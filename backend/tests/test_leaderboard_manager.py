import time
import unittest
import uuid

from backend.database import Enums
from backend.database import LeaderboardManager


class TestLeaderboard(unittest.TestCase):
    def test_get_leaderboard(self):
        leaderboard = LeaderboardManager.get_leaderboard('Mathematics', 'Algebra')
        self.assertLessEqual(len(leaderboard), Enums.leaderboardSize)
        self.assertGreaterEqual(len(leaderboard), 0)

        if len(leaderboard) > 0:
            curr = leaderboard[0]
            for i in range(1, len(leaderboard)):
                self.assertLessEqual(curr["score"], leaderboard[i]["score"])
                curr = leaderboard[i]

    def test_update_full_leaderboard_lower_score(self):
        # Inserting a score lower than the current lowest should not be successful
        subject = "Mathematics"
        topic = "Algebra"
        leaderboard = LeaderboardManager.get_leaderboard(subject, topic)
        currLowest = leaderboard[0]

        otherUser = {"score": currLowest["score"] - 1, "uid": str(uuid.uuid4()),
                     "epochTimeAdded": currLowest["epochTimeAdded"]}
        LeaderboardManager.update_leaderboard(otherUser, subject, topic)
        updatedLeaderboard = LeaderboardManager.get_leaderboard(subject, topic)
        self.assertEqual(currLowest, updatedLeaderboard[0])
        self.assertNotEqual(otherUser, updatedLeaderboard[0])

    def test_update_full_leaderboard_same_score(self):
        # Inserting a score equal to the current lowest should not be successful
        subject = "Mathematics"
        topic = "Algebra"
        leaderboard = LeaderboardManager.get_leaderboard(subject, topic)
        currLowest = leaderboard[0]

        otherUser = {"score": currLowest["score"], "uid": str(uuid.uuid4()), "epochTimeAdded": time.time()}
        LeaderboardManager.update_leaderboard(otherUser, subject, topic)
        updatedLeaderboard = LeaderboardManager.get_leaderboard(subject, topic)
        self.assertEqual(currLowest, updatedLeaderboard[0])
        self.assertNotEqual(otherUser, updatedLeaderboard[0])

    def test_update_full_leaderboard_higher_score(self):
        # Inserting a score higher than the current lowest should be successful
        subject = "Mathematics"
        topic = "Algebra"
        leaderboard = LeaderboardManager.get_leaderboard(subject, topic)
        currLowest = leaderboard[0]

        otherUser = {"score": currLowest["score"] + 1, "uid": str(uuid.uuid4()),
                     "epochTimeAdded": currLowest["epochTimeAdded"]}
        LeaderboardManager.update_leaderboard(otherUser, subject, topic)
        updatedLeaderboard = LeaderboardManager.get_leaderboard(subject, topic)
        self.assertNotEqual(currLowest, updatedLeaderboard[0])
