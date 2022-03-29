from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

from Bot import Bot
from UhillUnit import UhillUnit
app = FastAPI()

bot = Bot()
uhill = UhillUnit()

@app.get('/api/target_unit')
@app.post('/api/target_unit')
async def get_target_unit(request: Request):
    units = uhill.get_all_available_units()
    target_units = ['Fairley', 'Tristan', 'Tasso', 'Deco']
    res = list(filter(lambda item: item['floorplan_name'] in target_units, units))
    filename, txt = uhill.write_csv(res)
    if request.method == "POST":
        await bot.send(txt)
        return "OK"
    elif request.method == "GET":
        return FileResponse(filename)
    