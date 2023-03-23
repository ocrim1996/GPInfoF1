from datetime import datetime, timedelta
import flag


def convert_num_to_month(num):
    return {
        '1': 'Gennaio',
        '2': 'Febbraio',
        '3': 'Marzo',
        '4': 'Aprile',
        '5': 'Maggio',
        '6': 'Giugno',
        '7': 'Luglio',
        '8': 'Agosto',
        '9': 'Settembre',
        '10': 'Ottobre',
        '11': 'Novembre',
        '12': 'Dicembre',

    }[num]


def convert_num_to_day(num):
    return {
        '0': 'Lun',
        '1': 'Mar',
        '2': 'Mer',
        '3': 'Gio',
        '4': 'Ven',
        '5': 'Sab',
        '6': 'Dom',
    }[num]


def get_flag_country(country):
    return {
        'Australia': flag.flag("AU"),
        'Azerbaijan': flag.flag("AZ"),
        'USA': flag.flag("US"),
        'Italia': flag.flag("IT"),
        'Monaco': flag.flag("MC"),
        'Spagna': flag.flag("ES"),
        'Canada': flag.flag("CA"),
        'Austria': flag.flag("AT"),
        'Gran Bretagna': flag.flag("GB"),
        'Ungheria': flag.flag("HU"),
        'Belgio': flag.flag("BE"),
        'Olanda': flag.flag("NL"),
        'Singapore': flag.flag("SG"),
        'Giappone': flag.flag("JP"),
        'Qatar': flag.flag("QA"),
        'Messico': flag.flag("MX"),
        'Brasile': flag.flag("BR"),
        'Abu Dhabi': flag.flag("AE"),
        'Bahrain': flag.flag("BH"),
        'Arabia Saudita': flag.flag("SA"),
    }[country]


def get_country(circuit):
    return circuit.split("-")[0][:-1]


def race_time_with_delay(race_time):
    race_year = race_time.year
    race_month = race_time.month
    race_day = race_time.day
    race_hour = race_time.hour
    race_minute = race_time.minute

    return datetime(race_year, race_month, race_day, race_hour, race_minute) + timedelta(hours=4)


def create_date_message(date):
    weekday = convert_num_to_day(str(date.weekday()))
    day = str(date.day)
    month = convert_num_to_month(str(date.month))
    hour = date.strftime("%H")
    minute = date.strftime("%M")

    return weekday + " " + day + " " + month + " " + hour + ":" + minute


def create_date_message_schedule(date):
    day = str(date.day)
    month = convert_num_to_month(str(date.month))

    return day + " " + month


def format_next_f1_gp(gp):
    header = "\U0001f51c \u23F0 \U0001f3ce\uFE0F \u23ED\uFE0F \U0001f3ce\uFE0F \u23F0 \U0001f51c\n"

    # GP with Sprint Race.
    if gp[5] != "X":
        fp1_time = create_date_message(datetime.fromisoformat(gp[1]))
        qualifying_time = create_date_message(datetime.fromisoformat(gp[4]))
        fp2_time = create_date_message(datetime.fromisoformat(gp[2]))
        sprint_race_time = create_date_message(datetime.fromisoformat(gp[5]))
        race_time = create_date_message(datetime.fromisoformat(gp[6]))
        country_flag = get_flag_country(get_country(gp[0]))
        return header + "*" + gp[0].replace("-", "\-") + "*" + country_flag + "\n" \
               + "*FP1*:\n" + "• " + fp1_time + "\n" + \
               "*Qualifiche per Sprint Race*:\n" + "• " + qualifying_time + "\n" + \
               "*FP2*:\n" + "• " + fp2_time + "\n" + \
               "*Sprint Race*:\n" + "• " + sprint_race_time + "\n" + \
               "*Gara*:\n" + "\U0001f3c1 " + "*" + race_time + "*"

    # GP without Spint Race.
    else:
        fp1_time = create_date_message(datetime.fromisoformat(gp[1]))
        fp2_time = create_date_message(datetime.fromisoformat(gp[2]))
        fp3_time = create_date_message(datetime.fromisoformat(gp[3]))
        qualifying_time = create_date_message(datetime.fromisoformat(gp[4]))
        race_time = create_date_message(datetime.fromisoformat(gp[6]))
        country_flag = get_flag_country(get_country(gp[0]))
        return header + "*" +gp[0].replace("-", "\-") + "*" + country_flag + "\n" \
               + "*FP1*:\n" + "• " + fp1_time + "\n" + \
               "*FP2*:\n" + "• " + fp2_time + "\n" + \
               "*FP3*:\n" + "• " + fp3_time + "\n" + \
               "*Qualifiche*:\n" + "• " + qualifying_time + "\n" + \
               "*Gara*:\n" + "\U0001f3c1 " + "*" + race_time + "*"


def format_f1_schedule(csv_reader):
    schedule = "\U0001f5d3\uFE0F \U0001f5d3\uFE0F \U0001f5d3\uFE0F \U0001f3ce\uFE0F \U0001f3ce\uFE0F \U0001f3ce\uFE0F " \
             "\U0001f5d3\uFE0F \U0001f5d3\uFE0F \U0001f5d3\uFE0F\n"
    for gp in csv_reader:
        country_flag = get_flag_country(get_country(gp[0]))
        race_time = create_date_message_schedule(datetime.fromisoformat(gp[6]))
        schedule = schedule + "• " + "*" + race_time + "*" + ", " + gp[0].replace("-", "\-") + country_flag + "\n"

    return schedule


def format_all_f1_gp(gps):
    message = ""
    for gp in gps:
        header = "\-"*30+"\n"

        # GP with Sprint Race.
        if gp[5] != "X":
            fp1_time = create_date_message(datetime.fromisoformat(gp[1]))
            qualifying_time = create_date_message(datetime.fromisoformat(gp[4]))
            fp2_time = create_date_message(datetime.fromisoformat(gp[2]))
            sprint_race_time = create_date_message(datetime.fromisoformat(gp[5]))
            race_time = create_date_message(datetime.fromisoformat(gp[6]))
            country_flag = get_flag_country(get_country(gp[0]))
            message += header + "*" + gp[0].replace("-", "\-") + "*" + "\U0001f3ce\uFE0F" + country_flag + "\n" \
                   + "*FP1*:\n" + "• " + fp1_time + "\n" + \
                   "*Qualifiche per Sprint Race*:\n" + "• " + qualifying_time + "\n" + \
                   "*FP2*:\n" + "• " + fp2_time + "\n" + \
                   "*Sprint Race*:\n" + "• " + sprint_race_time + "\n" + \
                   "*Gara*:\n" + "\U0001f3c1 " + "*" + race_time + "*" + "\n"

        # GP without Spint Race.
        else:
            fp1_time = create_date_message(datetime.fromisoformat(gp[1]))
            fp2_time = create_date_message(datetime.fromisoformat(gp[2]))
            fp3_time = create_date_message(datetime.fromisoformat(gp[3]))
            qualifying_time = create_date_message(datetime.fromisoformat(gp[4]))
            race_time = create_date_message(datetime.fromisoformat(gp[6]))
            country_flag = get_flag_country(get_country(gp[0]))
            message += header + "*" +gp[0].replace("-", "\-") + "*" + "\U0001f3ce\uFE0F" + country_flag + "\n" \
                   + "*FP1*:\n" + "• " + fp1_time + "\n" + \
                   "*FP2*:\n" + "• " + fp2_time + "\n" + \
                   "*FP3*:\n" + "• " + fp3_time + "\n" + \
                   "*Qualifiche*:\n" + "• " + qualifying_time + "\n" + \
                   "*Gara*:\n" + "\U0001f3c1 " + "*" + race_time + "*" + "\n"

    return message
