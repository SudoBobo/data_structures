def calc_pros_begin_times(size, n, arrivals, durations):
    ad = [[-2, -2, -2] for elem in range(n)]

    for elem in range(n):
        ad[elem][0] = arrivals[elem]
        ad[elem][1] = durations[elem]
        # starting time
        ad[elem][2] = -2

    buf = []
    time = 0

    incoming_elem_idx = 0
    number_of_pros_elems = 0
    last_buf_elem_idx = -1

    while not number_of_pros_elems == n:

        # инвариант : в начале буфера нет нулей

        # убираем из времени обрабатываемого единичку времени или сколько там прошло
        # между соседними эрайвалами
        # если он не пуст
        # справедливо полагаем, что элемент не нулевой

        if last_buf_elem_idx != -1:
                assert (buf[0][1] > 0)
                buf[0][1] -= 1
                # удаляем элемент, если он "закончился"
                if buf[0][1] == 0:
                    buf.pop(0)
                    number_of_pros_elems += 1
                    last_buf_elem_idx -= 1

                    # удаляем все нули за ним, присваивая им "время начала обработки" = time
                    while last_buf_elem_idx != -1 and buf[0][1] == 0:
                        e = buf.pop(0)
                        number_of_pros_elems += 1

                        e[2] = time
                        last_buf_elem_idx -= 1

                    # присваеваем элементу на выходе "время начала обработки" = time, если буффер не опустошился
                    if last_buf_elem_idx != -1:
                        assert (buf[0][1] > 0)
                        buf[0][2] = time


        while incoming_elem_idx < n and ad[incoming_elem_idx][0] <= time:

            # ... <= time for case with dt != 1
            # если буффер пуст
            if last_buf_elem_idx == -1:

                # если оказывается, что в начале (на выходе) буфера нули, то мы их сразу убираем
                # вернее, не добавляем в буфер
                if ad[incoming_elem_idx][1] == 0:
                    ad[incoming_elem_idx][2] = time
                    number_of_pros_elems += 1

                else:
                    buf.append(ad[incoming_elem_idx])
                    ad[incoming_elem_idx][2] = time
                    last_buf_elem_idx += 1
            else:
                # если новый элемент помещается в буффер
                if last_buf_elem_idx + 1 < size:
                    buf.append(ad[incoming_elem_idx])

                    last_buf_elem_idx += 1
                else:
                # если не помешается, то пропускаем
                    ad[incoming_elem_idx][2] = -1
                    number_of_pros_elems += 1

            incoming_elem_idx += 1

        time += 1

    times = []
    for i in range(n):
        times.append(ad[i][2])

    return times


size, n = map(int, input().split(' '))
arrivals = []
durations = []

if n > 0:
    for i in range(n):
        line = input().split(' ')
        arrivals.append(int(line[0]))
        durations.append(int(line[1]))

    pros_beggin_times = calc_pros_begin_times(size, n, arrivals, durations)

    for time in pros_beggin_times:
        print(time)
else:
    print('')
