
    @classmethod
    def all(cls):
        """
        Returns the dictionary __objects.
        """
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """
        Serializes __objects to the JSON file.
        """
        data_to_save = {key: value.to_dict() if not isinstance(value, dict) else value
                        for key, value in cls.__objects.items()}
        with open(cls.__file_path, 'w') as file:
            json.dump(data_to_save, file, cls=DateTimeEncoder)

    @classmethod
    def reload(cls):
        """
        Deserializes the JSON file to __objects, if it exists.
        """
        if cls.__file_path:
            try:
                with open(cls.__file_path, 'r') as file:
                    cls.__objects = json.load(file)
            except FileNotFoundError:
                return

            for key, value in cls.__objects.items():
                if isinstance(value, dict):
                    class_name = value.get("__class__")
                    if class_name and class_name in cls.classes:
                        classF = cls.classes[class_name]
                        cls.new(classF(**value))
                else:
                    cls.new(value)
