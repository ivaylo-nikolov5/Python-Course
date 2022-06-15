class Email:
    def __init__(self, sender, receiver, content,):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while command != "Stop":
    explode = command.split(" ")
    sender = explode[0]
    receiver = explode[1]
    content = explode[2]

    email = Email(sender, receiver, content)

    emails.append(email)

    command = input()

send_email = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())



