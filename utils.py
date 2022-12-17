import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill_name):
    result = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result







