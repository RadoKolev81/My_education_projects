capacity_volume = int(input())
debit_p1 = int(input())
debit_p2 = int(input())
hours = float(input())
first_pipe = debit_p1 * hours
second_pipe = debit_p2 * hours
current_volume = first_pipe + second_pipe
volume_in_percent = current_volume / capacity_volume * 100
first_pipe_in_percent = first_pipe / current_volume * 100
second_pipe_in_percent = second_pipe / current_volume * 100
if current_volume <= capacity_volume:
    print(f"The pool is {volume_in_percent}% full. Pipe 1: "
          f"{first_pipe_in_percent}%. Pipe 2: {second_pipe_in_percent}%.")
else:
    difference = current_volume - capacity_volume
    print(f"For {hours} hours the pool overflows with {difference} liters.")
