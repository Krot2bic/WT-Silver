

### Classes ###

init -2 python:

    #Favours
    class silver_request(object):
        title = ""
        tier = 0
        start_label = ""
        return_label = ""
        points = 0
        progress_hint = False

    class favor_class(silver_request):
        level = 0 # Hearts
        costume_event = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/heart_0"+str(self.level)+".png"
            ret_str = "\""+self.title+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            if self.costume_event:
               ret_str += "  {image=interface/clothes.png}"
            return ret_str

    class request_class(silver_request):
        complete = False
        inProgress = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            ret_str = "\""+self.title+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            return ret_str

    class shaming_class(silver_request):
        complete = False
        inProgress = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            ret_str = "\""+self.title+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            return ret_str
