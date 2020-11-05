import json


def make_precomputed_recommendation():
    with open('run.txt', 'w') as data_out:
        with open('data/gesis-search/candidates/candidate_resdata_top10.txt') as data_in:
            recommendations_complete = json.loads(data_in.read())
            for recommendations in recommendations_complete:
                rank = 0
                for recommendation, score in recommendations.get('similar_items').items():
                    rank += 1
                    line_entry = recommendations.get('target_items') + ' Q0 ' + recommendation + ' ' + str(rank) + ' ' + str(score) + ' ' + 'run_id\n'
                    data_out.write(line_entry)


if __name__ == '__main__':
    make_precomputed_recommendation()





