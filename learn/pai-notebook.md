### 调用 pyodps 执行odps sql

```python
#调用 pyodps 执行odps sql 参考 pyodps 文档 https://pyodps.readthedocs.io/zh_CN/latest/

def exec_sql(sql):
    print('====> execute_sql: ' + sql)
    instance = o.run_sql(sql)
    print('====> logview: ' + instance.get_logview_address())
    instance.wait_for_success()
sql = "drop table if EXISTS notebook_test"
exec_sql(sql)
```

### 读取输入桩数据以及表的名字

```python
# notebook 相关功能默认注入 df1 等参数
# 读取全部数据
# df1.to_pandas()
# 读取 odps dataframe
# df1.to_odps_dataframe()

# 参考文档 https://aistudio.alipay.com/doc/odps_io.html

# pip install aistudio-common -i 'https://pypi.antfin-inc.com/simple' -U

from aistudio_common.utils.notebook_utils import NotebookUtils
input_table_name = NotebookUtils.get_input_table(port=1) # 1, 2 ... 分别代表 notebook 的四个输入桩
```

### 读取ODPS数据

```python
from pypai.io import TableReader
from aistudio_common.utils import env_utils

project_table_name = 'dtmodel_dev.zhonggong_test_for_multi_partitions'
o = env_utils.get_odps_instance()

# 多分区表使用如下配置 partition='p1=1,p2=1'
# 更多信息见文档：https://aistudio.alipay.com/doc/odps_io.html
reader = TableReader.from_tensorcache(o, project_table_name, partition='p1=1')

# 返回全量数据
reader.to_pandas()

# 数据裁剪
reader.to_pandas(limit=10000)


# 使用 notebook 的时候的特殊用法
df1.to_pandas() # df1, df1 ... 分别代表 notebook 的四个输入桩

# 如果使用 notebook 读 ``阿里集团`` 的 odps project，遇到超时问题，尝试如下代码
# 执行如下命令更新代码包
# pip install aistudio-common -i 'https://pypi.antfin-inc.com/simple' -U
from aistudio_common.utils.notebook_utils import NotebookUtils
input_table_name = NotebookUtils.get_input_table(port=1) # 1, 2 ... 分别代表 notebook 的四个输入桩
o._tunnel_endpoint = "http://dt.odps.aliyun-inc.com/"
reader = TableReader.from_tensorcache(o, input_table_name)
reader.to_pandas()
```

### 查看模型

```python
# 参考pypai.model 文档 https://aistudio.alipay.com/doc/model.html
from pypai.model import list_model
models = list_model()
models.head()
```

### ODPS表数据可视化

```python
# 以 ODPS 表数据进行可视化绘图
# 对于数据集庞大的 ODPS 表请慎用

# 更多详情请查看文档：https://yuque.antfin-inc.com/aii/aistudio/cywnqe#4UUOK

# 柱状图
from aistudio_common.utils.plot_utils import plot
plot(
    plot_type='bar',
    tableName="table_name",
    xAxis="field1",
    yAxis="field2",

    # 分区表，若果有则填写
    partitions="partition1=p1,partition2=p2",
    # 按条件筛选。选填。具体用法请查看文档
    groupBy="field3=xxx",
    # 按字段分类。选填。具体用法请查看文档
    filterBy="field4",
)

# 折线图
from aistudio_common.utils.plot_utils import plot
plot(
    plot_type='line',
    tableName="table_name",
    xAxis="field1",
    yAxis="field2",

    # 分区表，若果有则填写
    partitions="partition1=p1,partition2=p2",
    # 按条件筛选。选填。具体用法请查看文档
    groupBy="field3=xxx",
    # 按字段分类。选填。具体用法请查看文档
    filterBy="field4",
)

# 热力图
from aistudio_common.utils.plot_utils import plot
plot(
    plot_type='heat',
    tableName="table_name",
    xAxis="field1",
    yAxis="field2",

    # 分区表，若果有则填写
    partitions="partition1=p1,partition2=p2",
    # 按条件筛选。选填。具体用法请查看文档
    groupBy="field3=xxx",
    # 按字段分类。选填。具体用法请查看文档
    filterBy="field4",
)
```

