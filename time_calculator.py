def add_time(start, duration, day = False):

    sthours, stmins = start.split(':')
    stmins, stperiod =stmins.split(' ')
    # converting data to processing format
    durhours, durmins = duration.split(':')
    days_week = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    sthours = int(sthours)
    stmins = int(stmins)
    durhours = int(durhours)
    durmins = int(durmins)
    period = stperiod.strip().lower()
    days_later = 0
    hours_day = 24
    half_day = 12
    next_day = False

    # time calculation + shifts minutes to hours

    total_mins = stmins + durmins 
    if total_mins > 60: 
        durhours += total_mins / 60
        total_mins = total_mins % 60
    
    if durhours == 24:
        next_day = True
        total_hours = sthours

    if durhours != 24:
        total_hours = int(sthours + durhours)
        if total_hours == half_day:
                if period == 'pm':
                    period = 'am'
                    next_day = True
                else:
                    period = 'pm'
        if total_hours > half_day and total_hours < hours_day:
            if period == 'pm':
                period = 'am'
                total_hours = int(total_hours % 12)
                next_day = True
            else:
                period = 'pm'
                total_hours = int(total_hours % 12)

        if total_hours > hours_day:
            days_later += int(total_hours / hours_day) 
            total_hours = int(total_hours % hours_day)
            if total_hours > half_day:
                if period == 'pm':
                    period = 'am'
                    total_hours = int(total_hours % 12)
                    next_day = True
                else:
                    period = 'pm'
                    total_hours = int(total_hours % 12)
            elif total_hours == half_day:
                if period == 'pm':
                    period = 'am'
                    next_day = True
                else:
                    period = 'pm'


    if next_day and days_later > 0:
        next_day = False
        days_later += 1

    new_time = f'{total_hours}:{total_mins:02} {period.upper()}'

    if day:
        day = day.strip().lower()
        if next_day:
            curday_index = int((days_week.index(day) + 1) % 7)
        else:
            curday_index = int((days_week.index(day) + days_later) % 7)
        current_day = days_week[curday_index]
        new_time += f', {current_day.title()}'

    if next_day and days_later == 0:
        new_time += f' (next day)'
    if days_later >= 1:
        new_time += f' ({days_later} days later)'
    
    return new_time