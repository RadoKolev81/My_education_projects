name_of_agency = input()
num_tickets_for_adult = int(input())
num_tickets_for_children = int(input())
net_price_for_adult_tickets = float(input())
tax_for_service = float(input())

net_price_for_children_tickets = net_price_for_adult_tickets * 0.30
final_price_for_adult_ticket = net_price_for_adult_tickets + tax_for_service
final_price_for_children_ticket = net_price_for_children_tickets + tax_for_service
price_for_all_tickets = (num_tickets_for_adult * final_price_for_adult_ticket) + \
                        (num_tickets_for_children * final_price_for_children_ticket)
profit = price_for_all_tickets * 0.20

print(f"The profit of your agency from {name_of_agency} tickets is {profit:.2f} lv.")