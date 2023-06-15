

# key value pairs
# key is reference, value is the content

#making a dictionary

# student1 = {
#     "name": "Jane",
#     "number": "021564646",
#     "grade": 11,
#     "completedLessons": 4,
#     "completedLessonNames": ["variables", "git", "dataTypes", "collections"]
# }
#
# # print(student1["grade"])
# #
# # student1["completedLessons"] = 3
# #
# # student1["completedLessonNames"].remove("dataTypes")
# #pr
# # print(student1["completedLessonNames"])
# #
# # print(student1.keys())
# # print(student1.values())
#
# for key, val in student1.items():
#     print(key + ": " + str(val))


characters = {
    "spongebob": 0,
    "mrKrabs": 0,
    "squidward": 0,
    "patrickStar": 0,
    "plankton": 0
}


characters["spongebob"] = characters["spongebob"] + 2

print(characters["spongebob"])

print(characters)
for key, val in characters.items():
    if val == 2:
        print(f"you are {key}")