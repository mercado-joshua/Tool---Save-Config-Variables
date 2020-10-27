import shelve

class ConfigData:
    def open_save_data(self, specified_path):
        self.__file = shelve.open(specified_path)
        return self

    def create_data(self, var_name, var_value):
        self.__file[var_name] = var_value
        self.__close_data()
        return self

    def read_data(self, var_name):
        data = self.__file[var_name]
        self.__close_data()
        return data

    def __close_data(self):
        self.__file.close()

def main():
    s = ConfigData()
    s.open_save_data('configuration_file')
    s.create_data('cats', ['joshua', 'richard', 'aljon', 'roy', 'aeroll'])

    s.open_save_data('configuration_file')
    data = s.read_data('cats')
    print(data)

    s.open_save_data('settings_file')
    s.create_data('person', {'first_name': 'joshua', 'last_name' : 'mercado', 'age' : 22})

    s.open_save_data('settings_file')
    data = s.read_data('person')
    print(data)

    print(data.keys())
    print(data.values())

if __name__ == '__main__':
    main()