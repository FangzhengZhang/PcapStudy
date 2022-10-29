import json

def get_json_map_from_DB(db_name):
    return json.load(open("./DB/" + db_name + ".json"))

def update_json_map_db(db_name, json_map):
    json.dump(json_map, open("./DB/" + db_name+".json",'w'))