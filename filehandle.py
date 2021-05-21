# """
# How to create and read file
# read "r"
# write "w"
# append "a"

# """

# # f=open("test.txt", "w")
# # f.write("Hello Python here.\n ")
# # f.close()

# # f=open("test.txt", "a")
# # f.write("Hello Pawan noob")
# # f.close()

# """reading in different ways"""

# f=open("test.txt", "r")
# print(f.read())
# f.close()


# f=open("test.txt", "r")
# print(f.readline())
# f.close()

# f=open("test.txt", "r")
# print(f.readlines())
# f.close()


a=[
        {"1":
            {
            "name": ["Ram", "kumar", "Shrestha"],
            "contact":
                {
                "home":["014432004"],
                "office":["9818949901"]
                 }
            }
        }
    ]

# fullname=(a[0].get("1").get("name"))
# print(f"Your name is {' '.join(fullname)}.")

home_contact=(a[0].get("1").get("contact").get("home")[0])
print(f"Your home contact is {home_contact}")

print("Your office contact is", (a[0].get("1").get("contact").get("office")[0]))
