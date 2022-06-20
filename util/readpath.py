#coding:utf-8
import  os

#获取文件路径
class Path():

    def current(self):
        return os.getcwd()


    def superior_path(self):
        return os.path.abspath(os.path.dirname(os.getcwd()))

    def get_project_path(self):
        return os.path.join(os.path.dirname(__file__))



if __name__ == "__main__":
    print(Path().current())
    print(Path().superior_path()+ '\config\config.yaml')
    print(Path().get_project_path("../"))