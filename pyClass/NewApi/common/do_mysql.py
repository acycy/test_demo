from mysql import connector
from NewApi.common.read_config import ReadConfig
from NewApi.common import project_path

class DoMysql:
    '''操作数据库的类，专门进行数据的读取'''

    def do_mysql(self,query,flag=1):
        '''
        query sql查询语句
        flag 标志 1 获取一条数据 2获取多条数据'''
        db_config = ReadConfig(project_path.conf_path).get_data('DB', 'db_config')

        cnn = connector.connect(**db_config)
        cursor = cnn.cursor()
        cursor.execute(query)

        if flag == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()

        return res


if __name__ == '__main__':
    query = 'SELECT * FROM load WHERE Id<23528' # '
    res = DoMysql().do_mysql(query, 2)
    print('数据库的查询结果1：{}'.format(res))