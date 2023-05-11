def get_friendships(users):
    return [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


def people_you_might_know(user_id, friendships):
    # Get the friends of the user
    user_friends = [friend for friend in friendships if user_id in friend]
    # Get the friends of the user's friends
    friends_of_friends = []
    for friend in user_friends:
        for friendship in friendships:
            if friend[0] in friendship and friendship[0] != user_id and friendship[0] not in friends_of_friends:
                friends_of_friends.append(friendship[0])
            if friend[1] in friendship and friendship[1] != user_id and friendship[1] not in friends_of_friends:
                friends_of_friends.append(friendship[1])
    return friends_of_friends


users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = get_friendships(users)
print(friendships)
for user in users:
    user_id = user["id"]
    friends_of_friends = people_you_might_know(user_id, friendships)
    print("People you might know for user",
          user["name"], ":", friends_of_friends)
