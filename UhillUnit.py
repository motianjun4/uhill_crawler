import requests
import json

class UhillUnit():
    def __init__(self) -> None:
        self.url = "https://sightmap.com/app/api/v1/4d7p1q57wkx/sightmaps/4873"

    def get_all(self):
        response = requests.request("GET", self.url)
        data = json.loads(response.text)
        return data['data']

    def get_all_available_units(self):
        data = self.get_all()
        floorplan = {}

        for item in data['floor_plans']:
            floorplan[item['id']] = item


        def mapFloorplan(item):
            item['floor_plan'] = floorplan[item['floor_plan_id']]
            return item


        units = list(map(mapFloorplan, data['units']))


        def mapUnits(item):
            fp = item['floor_plan']
            return {
                "#": item['display_unit_number'],
                'price': item['price'],
                'available_on': item['available_on'],
                'bedroom': fp['bedroom_count'],
                'floorplan_name': fp['name'],
                'area': item['area'],
            }


        flattend = list(map(mapUnits, units))
        return flattend
    
    def write_csv(self, data):
        import csv
        csv_columns = ['#', 'price', 'available_on', 'bedroom', 'floorplan_name', 'area']
        with open('./export.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in data:
                writer.writerow(data)
        return "./export.csv"
        
if __name__ == "__main__":
    a = UhillUnit()
    d = a.get_all_available_units()
    target_units = ['Fairley', 'Tristan', 'Tasso', 'Deco']
    res = list(filter(lambda item: item['floorplan_name'] in target_units, d))
    print(d)
    a.write_csv(res)
