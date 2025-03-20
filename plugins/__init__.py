from aiohttp import web

routes = web.RouteTableDef()

#Bot By: @TZ_IZANA 
#Bot By: @TZ_IZANA 
#Bot By: @TZ_IZANA 

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Silicon")

#Bot By: @TZ_IZANA 
#Bot By: @TZ_IZANA 
#Bot By: @TZ_IZANA 

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
 #Bot By: @TZ_IZANA 
#Bot By: @TZ_IZANA 
#Bot By: @TZ_IZANA    