import uuid

# Leaderboards
leaderboardSize = 30
leaderboard_user_fields = {
    "uid": {
        "Type": str
    },
    "score": {
        "Type": int
    }
}

# Questions
question_fields = {
    "Description": {
        "Type": str
    },
    "Difficulty_level": {
        "Type": int
    },
    "Correct": {
        "Type": str
    },
    "Wrong_1": {
        "Type": str
    },
    "Wrong_2": {
        "Type": str
    },
    "Wrong_3": {
        "Type": str
    },
}