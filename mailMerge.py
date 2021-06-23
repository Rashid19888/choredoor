with open("Names.txt", "r") as namefile:
    with open("Message.txt", "r") as messagefile:
        body = messagefile.read()
        for name in namefile:
            mail = "Hello " + name + body
            with open(name.strip() + ".txt", "w") as messagefile:
                messagefile.write(mail)

    print("All done, messages created and ready, tahe a look in your directory")
print("-----------------------------------------")
print("Here is an example of the messages created\n")

with open("Dave.txt", "r") as daves:
              print(daves.read())
