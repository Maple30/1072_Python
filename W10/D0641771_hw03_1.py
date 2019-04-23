def price(Ticket):
    AllPrice = {'星光票':150,'優待票':175,'團體票':230,'學生票':250,'全票':350,'二日票':450,'三日票':650,'全期票':2500}
    Ticket_Name = list(Ticket.keys())
    Total = 0
    for i in Ticket_Name:
        Total += AllPrice[i]*Ticket[i]
    return Total
ticket = {'星光票':2,'二日票':3}
p = price(ticket)
print(p)