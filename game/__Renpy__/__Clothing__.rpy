
init -2 python:
    
    clothing_type_paths = {
        'top':       "clothes/tops/",
        'bottom':    "clothes/bottoms/",
        'bra':       "clothes/underwear/bra/",
        'panties':   "clothes/underwear/panties/",
        'stockings': "clothes/stockings/",
        'hair':      "body/head/"
    }

    # outfit purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'clothing_purchases'):
        clothing_purchases = {}      

    class character_hair_option(object):

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_colors(self, root):
            li = []
            for color in self.colors:
                li.append( ( root +"/"+ str(self.option) +"_"+ str(color) +".png", color ) )
            return li


    class outfit_container(dict):
            
        def __init__(self, *args):
            for arg in args:
                if hasattr(arg, 'id'):
                    self[arg.id] = arg

        def all(self):
            return self.values()
        
        def purchased(self, to_check):
            global clothing_purchases
            if isinstance(to_check,str):
                return clothing_purchases.get( to_check, False )
            if isinstance(to_check,list):
                return all( [ clothing_purchases.get(item, False) for item in to_check ] )
        
        def any_purchased(self, *to_check):
            global clothing_purchases
            if isinstance(to_check,list):
                return any( [ clothing_purchases.get(item, False) for item in to_check ] )
        
    class character_outfit(object):
        id = ''

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def purchase(self):
            global clothing_purchases
            clothing_purchases[self.id] = True
        def purchased(self):
            global clothing_purchases
            return clothing_purchases.get(self.id, False)
            



    class clothing_item_container(dict):

        def __init__(self, *args):
            for arg in args:
                if hasattr(arg, 'name') and hasattr(arg, 'type'):
                    self[arg.type+"_"+arg.name] = arg

        def get(self, item_type, item_name):
            return deepcopy(self[item_type+"_"+item_name])

        def all_type(self, *types):
            li = []
            for type in types:
                for item in self.values():
                    if str(type) in str(item.type):
                        li.append( item )
            return li

        def all(self):
            return self.values()
        

    class clothing_item(object):
        type          = None
        name          = None
        version       = None
        color         = None
        wear          = False
        always_wear   = False
        actions       = []
        versions      = []
        colors        = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def __bool__(self):
            return notNull(self.name)
        __nonzero__ = __bool__


        def build_file_path(self, root, name, color, version):

            global clothing_type_paths
            if self.type in clothing_type_paths and clothing_type_paths[self.type] not in root:
                root += clothing_type_paths[self.type]

            if notNull( name, color, version ):
                return ( root + str(name) + "/" + str(color) + "_" + str(version) + ".png" )
            elif notNull( name, version ):
                return ( root + str(name) + "/" + str(version) +".png" )
            elif notNull( name, color ):
                return ( root + str(name) + "/" + str(color) +".png" )
            elif notNull( name ):
                return ( root + str(name) + ".png" )

        def get_file(self, root):
            return self.build_file_path( root, self.name, self.color, self.version )

        def get_versions(self, root):
            li = []
            for version in self.versions:
                li.append( ( self.build_file_path( root, self.name, self.color, version ), version ) )
            return li

        def get_colors(self, root):
            li = []
            for color in self.colors:
                li.append( (self.build_file_path( root, self.name, color, self.version ), color ) )
            return li


        def notNull(self, *atts):
            li = []
            for att in atts:
                if not hasattr(self, att) or getattr(self, att) == None or getattr(self, att) == "" or getattr(self, att) == []:
                    li.append(False)
                else:
                    li.append(True)
            return all(li)

        def save(self):
            dic = {}
            for att, value in self.__dict__.items():
                if value != getattr(clothing_item, att, "ATT_DNE"):
                    dic[att] = value
            return dic
        def load(self, dic):
            self.__dict__.update( dic )




    class custom_clothing(object):

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        # saves and loads the state of this object to the dictionary 'hg_clothing_saves'
        def save(self, id=None):
            global hg_clothing_saves
            dic = {}
            for att in dir(self):
                if not att.startswith('_'):
                    name = att
                    value = getattr(self, att)
                    if issubclass(value.__class__, object) and value.save():
                        dic[name] = { value.__class__.__name__ :  value.save() }
            dic.update(self.__dict__)
            if self.static:
                hg_dev_clothing_saves[self.id] = dic
            elif id == None:
                hg_clothing_saves[self.id] = dic
            else:
                hg_clothing_saves[id] = dic
        def load(self, id):

            # sets all atts back to default, prevents items from persisting across loads()
            for att in dir(hg_custom_clothing):
                if att not in ['get_layers', 'save', 'load'] and not att.startswith('_'):
                    setattr(self, att, getattr(hg_custom_clothing, att)) 

            global hg_clothing_saves
            if id in hg_dev_clothing_saves:
                load_dic = hg_dev_clothing_saves[id]
            else:
                load_dic = hg_clothing_saves[id]

            dic = {}
            for name, value in load_dic.items():
                if isinstance(value, dict):
                    for class_name in value:
                        class_ = globals()[class_name]
                        class_instance = class_()
                        class_instance.__dict__.update(value[class_name])
                        setattr(self, name, class_instance )
                else:
                    dic[name] = value
            self.__dict__.update( dic )
