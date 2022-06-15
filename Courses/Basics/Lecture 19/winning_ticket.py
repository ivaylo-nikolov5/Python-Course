def additional_func(half):
    streak = 0
    special_char = ""

    for x in half:
        if x != special_char:
            if streak >= 6:
                break
            streak = 1
            special_char = x
        else:
            streak += 1

    return [streak, special_char]


def validate_func(ticket):
    ticket_condition = ""
    if len(ticket) != 20:
        ticket_condition = "invalid ticket"
    elif ticket[0] * 20 == ticket and ticket[0] in "@#$^":
        ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
    else:
        data_source = ""
        if additional_func(ticket[:10]) > (additional_func(ticket[10:])):
            data_source = additional_func(ticket[10:])
        else:
            data_source = additional_func(ticket[:10])

        streak = data_source[0]
        special_char = data_source[1]

        if streak < 6 or special_char not in "@#$^":
            ticket_condition = f'ticket "{ticket}" - no match'
        else:
            ticket_condition = f'ticket "{ticket}" - {streak}{special_char}'

    return ticket_condition


def winning_ticket(tickets):

    for ticket in tickets:
        ticket = ticket.strip()
        print(validate_func(ticket))


text = input().split(",")
winning_ticket(text)
