number_of_lines = int(input())
current_day = int(input())


class DayLog:
    def __init__(self, log_type, day_number, clients_count):
        self.log_type = log_type
        self.day_number = day_number
        self.clients_count = clients_count


log = []
for _ in range(0, number_of_lines - 1):
    # arrival 3 2
    # departure 2 5
    raw = input().split(' ')
    print(raw)
    log.append(DayLog(raw[0], int(raw[1]), int(raw[2])))

# sort
log.sort(key=lambda day_log: day_log.day_number)

log_idx = 0
# even - четный
# odd - нечетный
even_max = 0
odd_max = 0

clients_served = 0
for day_n in range(1, current_day + 1):
    while log_idx < len(log) and log[log_idx].day_number == day_n:
        day_log = log[log_idx]

        if day_log.log_type == 'arrival':
            clients_served += day_log.clients_count

        if day_log.log_type == 'departu-re':
            clients_served -= day_log.clients_count

        log_idx += 1

    # even
    if day_n % 2 == 0:
        even_max = clients_served if clients_served > even_max else even_max
    else:
        odd_max = clients_served if clients_served > odd_max else odd_max

print(odd_max, even_max)