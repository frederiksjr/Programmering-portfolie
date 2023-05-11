
def get_friendships(users):
    friendships = []
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            # Check if the current pair of users are friends
            if (users[i]["id"] + users[j]["id"]) % 2 == 0:
                friendships.append((users[i]["id"], users[j]["id"]))
    return len(friendships), friendships


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

total_friendships, friendships = get_friendships(users)
print("Total friendship:", total_friendships)
print(friendships)
num_users = len(users)
average_friends = total_friendships / num_users
print("Average number of friends:", average_friends)
