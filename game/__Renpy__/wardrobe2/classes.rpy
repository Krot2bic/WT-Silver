init python:    
    def get_character_object(key):
        for key in character_list:
            try:
                object = character_list[key]
            except KeyError:
                raise Exception('Character "'+key+'" is not defined as a character class')
            return object
            
    class outfit_class(object):
        name = None
        price = 0
        desc = ""
        unlocked = False
        group = []
        cached = False
        
        sprite = "empty"
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
            if self.name == None:
                raise Exception('Outfit: "name" was not defined in outfit_class.')
            
            if self.group < 1:
                raise Exception('Outfit: "group" list was not defined in outfit_class.')
            
            # Mark each clothing piece from the group as unlocked/locked by default
            if self.unlocked:
                self.unlock(True)
                    
        def unlock(self, bool):
            self.unlocked = bool
            get_character_object(self.group[0].char).outfits.append(self)
            for i in xrange(0, len(self.group)):
                self.group[i].unlock(bool)
                
        def clone(self):
            clothes = []
            clothing = get_character_object(active_girl).clothing
            for key in clothing:
                if not clothing[key][0] == None:
                    clothes.append(clothing[key][0].clone())
            return outfit_class(name=self.name, desc=self.desc, unlocked=self.unlocked, group=clothes)
                
        def get_image(self):
            if not self.cached:
                self.cached = True
                # Create sprite list
                sprite_list = []
                
                char = get_character_object(self.group[0].char)
                
                # Add body to sprite list
                body = char.get_bodyparts()
                for i in xrange(0, len(body)):
                    item = [body[i][0], body[i][1]]
                    sprite_list.append(item)
                
                # Add clothing to sprite list
                for i in xrange(0, len(self.group)):
                    item = [self.group[i], char.clothing[self.group[i].type][1]]
                    sprite_list.append(item)
                        
                # Sort sprite list by zorder based on character clothing zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)            
                
                # Build image
                self.sprite = Image("characters/dummy.png")
                for sprite in sprite_list:                        
                    if isinstance(sprite[0], basestring):
                        self.sprite = Composite(
                                    (1010, 1200),
                                    (0,0), self.sprite, 
                                    (0,0), im.MatrixColor(Image(sprite[0]), im.matrix.desaturate()))
                    else:
                        self.sprite = Composite(
                                    (1010, 1200),
                                    (0,0), self.sprite,
                                    (0,0), sprite[0].get_image(True))
            return self.sprite
            
            
    class cloth_class(object):
        char = None # astoria, cho, hermione, luna, susan, tonks
        category = None
        subcat = None
        type = None
        id = None
        layers = None
        color = []
        color_default = []
        skinlayer = "characters/dummy.png"
        unlocked = True
        cloned = False
        cached = False
        
        sprite_ico = None

        name = ""
        desc = ""
        
        pose = ""

        imagepath = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Clothing: "char" was not defined in cloth_class.')
                
            if self.category == None:
                raise Exception('Clothing: "category" was not defined in cloth_class.')
                
            if self.subcat == None:
                raise Exception('Clothing: "subcat" was not defined in cloth_class.')
                
            if self.type == None:
                raise Exception('Clothing: "type" was not defined in cloth_class.')
                
            if self.id == None:
                raise Exception('Clothing: "id" was not defined in cloth_class.')
                
            if self.layers == None:
                raise Exception('Clothing: "layers" number was not defined in cloth_class.')
                
            if len(self.color) < self.layers:
                for i in xrange(len(self.color), self.layers):
                    self.color.append([255, 255, 255, 255])
                    
            self.color_default = [] # DO NOT DELETE !!!
            for i in xrange(0, len(self.color)):
                self.color_default.append(self.color[i])
                
            if self.layers > len(self.color):
                raise Exception('Clothing: "color" list does not match the number of layers in cloth_class.')
            
            # Check if clothing folder is a category, subcategory or a type
            if renpy.exists("characters/"+self.char+"/clothes/"+self.category+"/"+self.id+"/0.png"):
                self.imagepath = "characters/"+self.char+"/clothes/"+self.category+"/"
            elif renpy.exists("characters/"+self.char+"/clothes/"+self.subcat+"/"+self.id+"/0.png"):
                self.imagepath = "characters/"+self.char+"/clothes/"+self.subcat+"/"
            else:
                self.imagepath = "characters/"+self.char+"/clothes/"+self.type+"/"
  
            if renpy.exists(self.imagepath+self.id+"/skin.png"):
                self.skinlayer = self.imagepath+self.id+"/skin.png"
                
            # Add cloth object to respective character, category and sub-category in dictionary keylist
            if not self.cloned and self.unlocked:
                get_character_object(self.char).clothing_dictlist.setdefault(self.category, {}).setdefault(self.subcat, []).append(self)
                character_clothes_list.append(self)
                
            # Initialize icon crop calculations A.K.A threading A.k.A lazyload
            layers = []
            for i in xrange(0, self.layers):
                layers.append(self.get_imagelayer(i))
                
            self.sprite_ico = lazyload(layers, self.color, 0)
                
        def unlock(self, bool):
            if not self.unlocked:
                self.unlocked = bool
                get_character_object(self.char).clothing_dictlist.setdefault(self.category, {}).setdefault(self.subcat, []).append(self)
            
        def clone(self):
            dyes = []
            for dye in self.color:
                dyes.append([dye[0],dye[1],dye[2],dye[3]])
            return cloth_class(char=self.char, category=self.category, subcat=self.subcat, type=self.type, id=self.id, layers=self.layers, color=dyes, unlocked=self.unlocked, cloned=True, name=self.name, desc=self.desc)
                
        def set_pose(self, pose):
            if renpy.exists(self.imagepath+self.id+"/"+pose+"_0.png"):
                self.pose = pose
                self.sprite_ico.cached = False
                self.cached = False
                return True
            return False

        def get_matrixcolor(self, layer):
            return im.matrix.tint(float(self.color[layer][0])/255.0, float(self.color[layer][1])/255.0, float(self.color[layer][2])/255.0)

        def get_color(self, layer):
            return (float(self.color[layer][0])/255.0, float(self.color[layer][1])/255.0, float(self.color[layer][2])/255.0, float(self.color[layer][3])/255.0)
            
        def get_color_hex(self, layer):
            return '#%02x%02x%02x' % (self.color[layer][0], self.color[layer][1], self.color[layer][2])

        def get_alpha(self, layer):
            return self.color[layer][3]

        def set_color(self, layer):
            self.color[layer] = color_picker(self.color[layer], False, "Cloth layer "+str(layer+1), pos_xy=[20, 130])
            self.sprite_ico.cached = False
            self.cached = False
            
        def reset_color(self):
            for i in xrange(0, len(self.color)):
                self.color[i] = self.color_default[i]
            self.sprite_ico.cached = False
            self.cached = False

        def get_imagelayer(self, layer):
            return self.imagepath+self.id+"/"+str(layer)+".png" if self.pose == "" else self.imagepath+self.id+"/"+self.pose+"_"+str(layer)+".png"
                    
        def get_image(self, skingray=False):
            self.sprite = Image(self.skinlayer)
            
            # Used in mannequin generation
            if skingray:
                self.sprite = im.MatrixColor(self.sprite, im.matrix.desaturate())
            
            # Keep used clothes images in cache
            renpy.start_predict("characters/"+self.char+"/clothes/"+self.category+"/"+self.id+"/*.*")

            for i in xrange(0, self.layers):
                self.sprite = Composite(
                       (1010, 1200),
                       (0,0), self.sprite,
                       (0,0), im.MatrixColor(str(self.get_imagelayer(i)), self.get_matrixcolor(i)))
            return self.sprite
            
        def get_icon(self):
            return self.sprite_ico.get_image()
            
    class char_class(object):
        char = None
        
        cached = False
        cache_override = False
        
        body = {}
        face = {}
        clothing = {}
        clothing_dictlist = {}
        outfits = []
        other = {}
        
        sprite = "empty"
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Character: "char" was not defined in char_class.')
                
            character_list.update({self.char: self})
                
        def get_object(self, dict, *keys):
            for key in keys:
                try:
                    dict = dict[key][0]
                except KeyError:
                    return None
            return dict
            
        def update_zorder(self, layer, value):
            try:
                self.clothing[layer][1] = value
                self.cached = False
                return layer+" zorder changed to "+str(value)
            except KeyError:
                return 'Warning: layer "'+str(layer)+'" not found.'
            
        def update_paths(self, *args):
            symbol = "/"
            
            if 'body' in args:
                imagepath = "characters/"+self.char+"/body/"
                
                hair = self.get_object(self.body, 'hair')
                hairshadow = self.get_object(self.body, 'hairshadow')
                armleft = self.get_object(self.body, 'armleft')
                armright = self.get_object(self.body, 'armright')
                breasts = self.get_object(self.body, 'breasts')
                base = self.get_object(self.body, 'base')
                legs = self.get_object(self.body, 'legs')
                
                if hair and symbol not in hair :
                    self.body['hair'][0] = imagepath+"hair/"+hair+".png"
                if hairshadow and symbol not in hairshadow :
                    self.body['hairshadow'][0] = imagepath+"hair/"+hairshadow+".png"
                if armleft and symbol not in armleft:
                    self.body['armleft'][0] = imagepath+"arms/"+armleft+".png"
                if armright and symbol not in armright:
                    self.body['armright'][0] = imagepath+"arms/"+armright+".png"
                if breasts and symbol not in breasts:
                    self.body['breasts'][0] = imagepath+"breasts/"+breasts+".png"
                if base and symbol not in base:
                    self.body['base'][0] = imagepath+"base/"+base+".png"
                if legs and symbol not in legs:
                    self.body['legs'][0] = imagepath+"legs/"+legs+".png"
            if 'face' in args:
                imagepath = "characters/"+self.char+"/face/"
                
                tears = self.get_object(self.face, 'tears')
                cheeks = self.get_object(self.face, 'cheeks')
                eyebrows = self.get_object(self.face, 'eyebrows')
                eyes = self.get_object(self.face, 'eyes')
                pupils = self.get_object(self.face, 'pupils')
                whites = self.get_object(self.face, 'whites')
                mouth = self.get_object(self.face, 'mouth')
                
                if tears and symbol not in tears:
                    self.face['tears'][0] = imagepath+"extras/"+tears+".png"
                if cheeks and symbol not in cheeks:
                    self.face['cheeks'][0] = imagepath+"extras/"+cheeks+".png"
                if eyebrows and symbol not in eyebrows:
                    self.face['eyebrows'][0] = imagepath+"brow/"+eyebrows+".png"
                if eyes and symbol not in eyes:
                    self.face['eyes'][0] = imagepath+"eyes/"+eyes+".png"
                if pupils and symbol not in pupils:
                    self.face['pupils'][0] = imagepath+"pupil/"+pupils+".png"
                if whites and symbol not in whites:
                    self.face['whites'][0] = imagepath+"eyes/"+whites+".png"
                if mouth and symbol not in mouth:
                    self.face['mouth'][0] = imagepath+"mouth/"+mouth+".png"
            if 'other' in args:
                imagepath = "characters/emotes/"
                
                emote = self.get_object(self.other, 'emote')
                cum = self.get_object(self.other, 'cum')
                
                if emote and symbol not in emote:
                    self.other['emote'][0] = imagepath+emote+".png"
                    
                imagepath = "characters/"+self.char+"/cum/"
                
                if cum and symbol not in cum:
                    self.other['cum'][0] = imagepath+cum+".png"
            self.cached = False
            
        def expression(self, **kwargs):
            for arg, value in kwargs.iteritems():
                if value:
                    try:
                        self.face[str(arg)][0] = value
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" expression type was not defined for "'+self.char+'" character class.')

            self.update_paths("face")
            self.cached = False
            
        def special(self, **kwargs):
            for arg, value in kwargs.iteritems():
                try:
                    self.other[str(arg)][0] = value
                except KeyError:
                    raise Exception('Character: "'+str(arg)+'" other type was not defined for "'+self.char+'" character class.')

            self.update_paths("other")
            self.cached = False
            
        def get_cloth(self, type):
            return self.get_object(self.clothing, type)
            
        def get_category_list(self, category):
            return self.clothing_dictlist[category]
            
        def get_clothing_list(self, category, subcategory):
            return self.clothing_dictlist[category][subcategory]
            
        def get_equipped(self, category, subcategory, item):
            if not self.get_cloth(self.get_clothing_list(category, subcategory)[item].type) == None:
                return self.get_cloth(self.get_clothing_list(category, subcategory)[item].type).id
            return None
            
        def equip(self, object):
            if isinstance(object, outfit_class):
                self.unequip("all")
                for i in xrange(0, len(object.group)):
                    self.clothing[object.group[i].type][0] = object.group[i]
                    self.clothing[object.group[i].type][4] = False
            else:
                if self.clothing[object.type][0] == object:
                    self.clothing[object.type][0] = None
                else:
                    self.clothing[object.type][0] = object
                    self.clothing[object.type][4] = False
            self.cached = False
            
        def unequip(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    self.clothing[key][0] = None
            else:
                for arg in args.iteritems():
                    try:
                        self.clothing[str(arg)][0] = None
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def strip(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    self.clothing[key][4] = True
            else:
                for arg in args:
                    try:
                        self.clothing[str(arg)][4] = True
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def get_worn(self, type):
            if not self.clothing[type][0]:
                return None
            if not self.clothing[type][4]:
                return True
            return False
            
        def wear(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    self.clothing[key][4] = False
            else:
                for arg in args:
                    try:
                        self.clothing[str(arg)][4] = False
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def toggle_wear(self, type):
            try:
                self.clothing[str(type)][4] = not self.clothing[str(type)][4]
            except KeyError:
                raise Exception('Character: "'+str(type)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
                
        def say(self, string, **kwargs):
            if kwargs:
                self.expression(**kwargs)
            if string:
                renpy.say(self.char, string)
                
        def get_bodyparts(self):
            bodyparts = []
            for key, value in self.body.iteritems():
                if self.body[key][0]:
                    bodyparts.append(value) 
            return bodyparts
            
        def get_image(self):
            if not self.cached or self.cache_override:                
                self.cached = True
                
                # Keep character images in cache
                renpy.start_predict("characters/"+self.char+"/body/*.*")
                renpy.start_predict("characters/"+self.char+"/face/*.*")
                
                # Create sprite list
                sprite_list = []
                
                # Add body to sprite list
                for key, value in self.body.iteritems():
                    if self.body[key][0] and not self.body[key][4]:
                        sprite_list.append(value)
                        
                # Add face to sprite list
                for key, value in self.face.iteritems():
                    if self.face[key][0] and not self.face[key][4]:
                        sprite_list.append(value)
                
                # Add other to sprite list        
                for key, value in self.other.iteritems():
                    if self.other[key][0] and not self.other[key][4]:
                        sprite_list.append(value)
                        
                # Add clothing to sprite list        
                for key, value in self.clothing.iteritems():
                    if self.clothing[key][0] and not self.clothing[key][4]:
                        sprite_list.append(value)
                        
                # Sort sprite list by zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)
                
                # Build image
                self.sprite = Image("characters/dummy.png")
                if sprite_list:
                    for sprite in sprite_list:
                        # Check if sprite is an imagepath or an object
                        if isinstance(sprite[0], basestring):
                            self.sprite = Composite(
                                    (1010, 1200),
                                    (0,0), self.sprite,
                                    (sprite[2],sprite[3]), Image(sprite[0]))
                        else:
                            self.sprite = Composite(
                                    (1010, 1200),
                                    (0,0), self.sprite,
                                    (sprite[2],sprite[3]), sprite[0].get_image())
                                    
                    # Fixes alpha change issues during transitions
                    self.sprite = Flatten(self.sprite)
            return self.sprite