# Leaderboards
leaderboardSize = 30
leaderboard_user_fields = {
    "username": {
        "Type": str
    },
    "score": {
        "Type": int
    },
    "epochTimeAdded": {
        "Type": float
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
    "question_id": {
        "Type": str
    }
}

question_result_fields = {
    "description": {
        "Type": str
    },
    "correct": {
        "Type": str
    },
    "wrong_1": {
        "Type": str
    },
    "wrong_2": {
        "Type": str
    },
    "wrong_3": {
        "Type": str
    },
    "count_attempts": {
        "Type": int
    },
    "count_correct": {
        "Type": int
    },
    "count_wrong_1": {
        "Type": int
    },
    "count_wrong_2": {
        "Type": int
    },
    "count_wrong_3": {
        "Type": int
    }
}