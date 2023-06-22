def get_score():

    import statsapi
    from datetime import date
    import json

    most_recent_game_id = statsapi.next_game(117)
    schedule = statsapi.schedule(team=117, start_date=date.today(), end_date=date.today())
    try:
        current_game = schedule[0]['game_id']
    except IndexError:
        current_game = statsapi.last_game(117)

    game = statsapi.get('game', params = {
            "gamePk": current_game,
            "fields": "gameData,teams,teamName,shortName,status,abstractGameState,liveData,linescore,innings,num,home,away,runs,hits,errors",
        })

    events = statsapi.game_scoring_plays(current_game)
    events = events.split('\n')

    real_e = []

    for event in events:
        if "Top" in event or "Bottom" in event:
            real_e.append(event)

    
    highlights = (statsapi.game_highlight_data(current_game))
    highlights_data = {}

    for item in highlights:
        if item['type'] == 'video':
            highlights_data[item['date']] = [item['title'],item['playbacks'][0]['url']]

    keys = list(highlights_data.keys())
    keys.sort()
    sorted_hd = {i: highlights_data[i] for i in keys}

    game_state = game["gameData"]["status"]["abstractGameState"]

    away_name = game["gameData"]["teams"]["away"]["teamName"]
    home_name = game["gameData"]["teams"]["home"]["teamName"]

    try:
        home_score = game["liveData"]["linescore"]["teams"]['home']['runs']
        away_score = game["liveData"]["linescore"]["teams"]['away']['runs']
    except KeyError:
        home_score, away_score = 0, 0

    winning = None

    astros_score = home_score if home_name == "Astros" else away_score
    opp_score = away_score if home_name == "Astros" else home_score

    opp_name = away_name if away_name != "Astros" else home_name

    
    
    if game_state == 'Final':
        winning = "Not playing now."
    else:
        if astros_score > opp_score:
            winning = 'YES!'
        elif astros_score < opp_score:
            winning = "No..."
        elif astros_score == opp_score:
            winning = "Tied"

    r_highlights_data = {}

    for key in reversed(sorted_hd):
        value = sorted_hd[key]
        r_highlights_data[key] =  value


    data = {
        'winning': winning,
        'opp_name': opp_name,
        'astros_score': astros_score,
        'opp_score': opp_score,
        'highlights_data': r_highlights_data,
        'scoring_plays': events[::-1]
        }

    return data

get_score()