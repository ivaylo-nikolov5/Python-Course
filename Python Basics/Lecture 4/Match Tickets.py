budget = float(input())
category = input()
people = int(input())

result = ""

if people >= 1 and people <=4:
    transport =budget * 0.75
    if category == "VIP":
        ticket = 499.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
    else:
        ticket = 249.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."

if people >= 5 and people <= 9:
    transport =budget * 0.60
    if category == "VIP":
        ticket = 499.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
    else:
        ticket = 249.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
if people >= 10 and people <=24:
    transport =budget * 0.50
    if category == "VIP":
        ticket = 499.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
    else:
        ticket = 249.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
if people >= 25 and people <=49:
    transport =budget * 0.40
    if category == "VIP":
        ticket = 499.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
    else:
        ticket = 249.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
if people >= 50:
    transport =budget * 0.25
    if category == "VIP":
        ticket = 499.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."
    else:
        ticket = 249.99
        m_spent = transport + ticket*people
        if m_spent < budget:
            m_left = budget - m_spent
            result = f"Yes! You have {m_left:.2f} leva left."
        else:
            m_needed = m_spent - budget
            result = f"Not enough money! You need {m_needed:.2f} leva."

print(result)












