#coding:utf-8
import yaml
from util.readpath import Path


class YamlHandler:

    def __init__(self,file):
        self.file = file


    def read_yaml(self,encoding='utf-8'):
        """
        :param encoding:
        :return: 读取yaml数据
        """
        with open(self.file,encoding=encoding) as f:
            return yaml.load(f.read(),Loader=yaml.FullLoader)

    def write_yaml(self,data,encoding='utf-8'):
        """
        :param data:
        :param encoding:
        :return: 向yaml文件写入数据
        """
        with open(self.file,encoding=encoding,mode='w') as f:
            return yaml.dump(data,stream=f,allow_unicode=True)

superior = Path().superior_path()
# print(type(superior))
yaml_data = YamlHandler(superior + "\config\config.yaml").read_yaml()

if __name__ == "__main__":
    # data = {
    #     "user":{
    #         'username':'wuxiaojia',
    #         'password':'123456'
    #     }
    # }
    #
    #读取config.yaml配置文件数据
    #read_data = YamlHandler('../config/config.yaml').read_yaml()
    # #将data数据写入config1.yaml配置文件
    # # write_yaml= YamlHandler('../config/config.yaml').write_yaml(data)
    #print(read_data)
    a = yaml_data
    print(a['config']['path'])


