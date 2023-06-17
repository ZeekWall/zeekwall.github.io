from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/score', methods=['GET'])
def get_score():

    import statsapi


    most_recent_game_id = statsapi.last_game(117)

    # print(statsapi.linescore(most_recent_game_id))

    game = statsapi.get('game', params = {
            "gamePk": most_recent_game_id,
            "fields": "gameData,teams,teamName,shortName,status,abstractGameState,liveData,linescore,innings,num,home,away,runs,hits,errors",
        })

    game_state = game["gameData"]["status"]["abstractGameState"]

    away_name = game["gameData"]["teams"]["away"]["teamName"]
    home_name = game["gameData"]["teams"]["home"]["teamName"]

    home_score = game["liveData"]["linescore"]["teams"]['home']['runs']
    away_score = game["liveData"]["linescore"]["teams"]['away']['runs']

    playing = None
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

    data = {
        'winning': winning,
        'opp_name': opp_name,
        'astros_score': astros_score,
        'opp_score': opp_score,
        }


    return data
    # # Return the score as JSON
    # return jsonify(score)
get_score()


# import statsapi


# most_recent_game_id = statsapi.last_game(117)

# # print(statsapi.linescore(most_recent_game_id))

# game = statsapi.get('game', params = {
#         "gamePk": most_recent_game_id,
#         "fields": "gameData,teams,teamName,shortName,status,abstractGameState,liveData,linescore,innings,num,home,away,runs,hits,errors",
#     })

# game_state = game["gameData"]["status"]["abstractGameState"]

# away_name = game["gameData"]["teams"]["away"]["teamName"]
# home_name = game["gameData"]["teams"]["home"]["teamName"]

# home_score = game["liveData"]["linescore"]["teams"]['away']['runs']
# away_score = game["liveData"]["linescore"]["teams"]['home']['runs']

# data = {
#     'game_state': game_state,
#     'home_name': home_name,
#     'away_name': away_name,
#     'home_score': home_score,
#     'away_score': away_score,
#     }
# return data