# string concatenation (aka how to put strings together)
# a few ways to do this
# activity = "tennis"

# print("My favorite activity is" + activity)
# print("My favorite actvity is {}".format(activity))
# print(f"My favorite activity is {activity}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_landmark = input("Famous landmark: ")

madlib = f"Traveling is so {adj}! When I go abroad I love to {verb1}. \
It's hard to imagine but I also enjoy {verb2}. \
My favorite sight in the entire world is {famous_landmark}!"

print(madlib)
