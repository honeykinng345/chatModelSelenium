import requests

from datetime import datetime

from model.User import User
from network_requests.network_calling import HttpRequestHandler
from utils.global_objects import Global
from utils.json_parser import JsonParser
from utils.json_responses import JsonResponse
from utils.web_driver import WebDriverHandler

userObject: User  # Initialize the global variable at the module level


class UserHandler:
    userObject: User

    @classmethod
    def checkUserAlreadyExistOrNot(cls, appId):
        try:
            with open("ScreenFlow.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: initialize_chrome_drive")

            isMatch: bool = False
            global userObject

            if appId not in Global.user_map:
                webDriver = WebDriverHandler(ip=12345, port=434)
                Global.user_map[appId] = User(appId, "12345",
                                              webDriver.initialize_chrome_driver(appId, webDriver.proxyIp,
                                                                                 webDriver.proxyPort
                                                                                 , "ddd"))
                userObject = Global.user_map[appId]
                return userObject
            else:
                with open("ScreenFlow.txt", "a") as f:
                    current_datetime = datetime.now()
                    f.write(f"{current_datetime}:getExsitUSer() \n f{Global.user_map[appId]}")
                return Global.user_map[appId]

        except Exception as e:
            raise e

            # geonodeList = cls.getProxyListFromGeonode()
            # sorted_data = sorted(geonodeList.data, key=lambda datum: datum.speed)
            # if len(Global.user_map.values()) >= 1:
            #     userObject = None
            #     for geonodeObject in geonodeList.data:
            #
            #         for getUser in Global.user_map.values():
            #             if getUser.proxyIP != geonodeObject.ip and geonodeObject.speed <= 7:
            #                 webDriver = WebDriverHandler(ip=geonodeObject.ip, port=geonodeObject.port)
            #                 Global.user_map[appId] = User(appId, geonodeObject.ip,
            #                                               webDriver.initialize_chrome_driver(appId, webDriver.proxyIp,
            #                                                                                  webDriver.proxyPort
            #                                                                                  , geonodeObject.protocols[0].value))
            #                 isMatch = True
            #                 userObject = Global.user_map[appId]
            #                 break
            #         if isMatch:
            #             break
            #
            # else:
            #     if sorted_data[0].speed <= 7:
            #         webDriver = WebDriverHandler(ip=sorted_data[0].ip, port=sorted_data[0].port)
            #         Global.user_map[appId] = User(appId, sorted_data[0].ip,
            #                                       webDriver.initialize_chrome_driver(appId, webDriver.proxyIp,
            #                                                                          webDriver.proxyPort,
            #                                                                          sorted_data[0].protocols[0].value))
            #         isMatch = True
            #         userObject = Global.user_map[appId]

            # if not isMatch:
            #     raise Exception(JsonResponse.getErrorResponse("No Server Found", 500))

            # else:
            #     return userObject

    # Define the function to call the external API
    @classmethod
    def getProxyListFromGeonode(cls):
        url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
        try:
            httpRequestHandler = HttpRequestHandler(url)
            response = httpRequestHandler.getRequest()
            if response:
                # Create an instance of MyModel using the parsed data
                return JsonParser.parse_geonode_proxy_servers(response)

        except Exception as e:
            # Handle exceptions such as connection errors or timeouts
            with open("GeneralException.txt", "a") as f:
                current_datetime = datetime.now()
                f.write(f"{current_datetime}: Exception in getProxyListFromGeonode(): {e}\n")
            raise Exception(JsonResponse.getErrorResponse("Something went wrong", 500))
