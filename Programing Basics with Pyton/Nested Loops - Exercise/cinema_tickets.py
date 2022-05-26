student_tickets_counter = 0
standart_tickets_counter = 0
kid_tickets_counter = 0
total_tikets = 0

comand = input()
while comand != 'Finish':
    movie_name = comand
    free_places = int(input())
    total_places = free_places
    sold_tickets = 0
    while free_places > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student_tickets_counter += 1
        elif ticket_type == 'standard':
            standart_tickets_counter += 1
        elif ticket_type == 'kid':
            kid_tickets_counter += 1
        free_places -= 1
        sold_tickets += 1
        total_tikets += 1
    print(f"{movie_name} - {(sold_tickets / total_places * 100):.2f}% full.")
    comand = input()

print(f"Total tickets: {total_tikets}")
print(f"{(student_tickets_counter / total_tikets * 100):.2f}% student tickets.")
print(f"{(standart_tickets_counter / total_tikets * 100):.2f}% standard tickets.")
print(f"{(kid_tickets_counter / total_tikets * 100):.2f}% kids tickets.")
