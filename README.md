# CRAFT_inference_xmlchange

对文本检测模型CRAFT训练与推断过程中，需要的数据格式转换代码汇总。

#### 1. test_to_txt.py

将CRAFT-Pytorch项目中的test.py换为test_to_txt.py可以把推断中检测的文本框坐标保存成txt文件，格式如下：

820,827,1559,827,1559,930,820,930,textline

2846,850,3188,850,3188,947,2846,947,textline

3281,879,3572,879,3572,934,3281,934,textline

#### 2. creat_json.py

将txt格式坐标转换为json格式，使其可以在labelme中查看并修正。

ps：网上几乎没有txt转json的标准代码，保存一下以便后续使用。

#### 3. change_int.py

将float型坐标转换为int型，避免训练时报错。
