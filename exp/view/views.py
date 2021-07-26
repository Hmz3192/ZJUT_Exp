from django.shortcuts import render


# Create your views here.

def to_index(request):
    return render(request, 'index.html')


def sign_up(request):
    return render(request, 'signup.html')


def sign_in(request):
    return render(request, 'signin.html')


def self(request):
    return render(request, 'self_mes.html')


def to_exp_twenteen(request):
    id = "实验-12"
    title = "蚁群算法求解最短路径实验"
    aim = "熟悉和掌握蚁群算法的原理、流程和算法模型，并利用蚁群算法求解最短路径问题，理解求解流程并测试主要参数对结果的影响。"
    content = "编写基于蚁群算法求解TSP问题的程序，算出20个城市和50个城市之间的最短距离。"
    exp_request = "1.编写基于蚁群算法求解TSP问题的程序，给出20个城市的坐标信息，求解最短路径；将输入数据换为50个城市的坐标，求解最短路径。" \
                  "\n2.对于同一个TSP问题，设置不同的参数（信息素启发式因子α，期望启发式因子β，信息素残留常数ρ，蚁群规模等），分析不同的参数对蚁群算法的影响。" \
                  "\n3.讨论三种不同的模型，分析哪种模型的效果最佳。"
    exp_report = "1.画出蚁群算法求解TSP问题的流程图。" \
                 "\n2.针对同一个TSP问题，分析不同的参数对于蚁群算法效果的影响。" \
                 "\n3.分析蚁群算法和遗传算法的区别与联系，优缺点。" \
                 "\n4.总结实验心得。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_fifteen(request):
    id = "实验-15"
    title = "粒子群算法求函数最小值实验"
    aim = "熟悉和掌握粒子群算法的原理、流程，并利用粒子群算法求解函数优化问题，理解求解流程并测试主要参数对实验结果的影响。"
    content = "用粒子群算法求解函数优化问题。"
    exp_request = "1、用粒子群求解下列函数的最小值。" \
                  "\n（1）使用python编写粒子群算法代码，并给出该适应度函数的定义方法。" \
                  "\n（2）记录每一代种群的全局最优个体g_best的适应度值，使用matplotlib可视化g_best适应度值随种群迭代的变化曲线。理解并分析种群收敛过程。" \
                  "\n（3）设置不同的加速度常量，求得相应的最佳适应度、平均适应度，填入表1，比较并分析PSO社会模型、PSO认知模型等对算法性能的影响。" \
                  "\n2、用粒子群局部版本（利用环形法，粒子的编号取粒子的邻域）求解同一函数的最小值问题。" \
                  "\n（1）记录每一代种群的全局最优个体g_best的适应度值，使用matplotlib可视化g_best适应度值随种群迭代的变化曲线。" \
                  "\n（2）比较分析粒子群全局版本和局部版本的差别。"
    exp_report = "1、画出粒子群算法的算法流程图。" \
                 "\n2、根据实验内容，给出相应结果以及结果分析。" \
                 "\n3、比较分析粒子群局部版本和全局版本的区别。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_fourteen(request):
    id = "实验-14"
    title = "量子粒子群算法求函数最优解"
    aim = "熟悉和掌握量子粒子群的概念及流程，并利用量子粒子群算法求最优解。理解量子粒子群更新粒子位置的基本理论，包括收缩-扩张因子的定义、粒子位置的计算方法、平均最优位置的计算方法、粒子最优位置的计算方法、量子空间中粒子精确位置的测量方法、全局最优粒子的搜索及更新方法，掌握量子粒子群算法的更新迭代流程。"
    content = "利用量子粒子群算法实现对不同维度的变量空间求测试函数最优解。"
    exp_request = "1.使用python编写量子粒子群算法代码，设定算法所需参数：变量空间维度D、种群规模n、迭代次数T。" \
                  "\n2.记录每一代种群的全局最优个体g_best的适应度值，使用matplotlib可视化g_best适应度值随种群迭代的变化曲线。理解并分析种群收敛过程。"
    exp_report = "1.按照实验要求，给出相应结果。" \
                 "\n2.分析量子粒子群的更新方式和收敛过程" \
                 "\n3.对比量子粒子群和粒子群的优劣。" \
                 "\n4.总结实验心得体会"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_thirteen(request):
    id = "实验-13"
    title = "量子进化算法求函数最优解"
    aim = "熟悉和掌握量子粒子群的概念及流程，并利用量子粒子群算法求最优解。理解量子粒子群更新粒子位置的基本理论，包括收缩-扩张因子的定义、粒子位置的计算方法、平均最优位置的计算方法、粒子最优位置的计算方法、量子空间中粒子精确位置的测量方法、全局最优粒子的搜索及更新方法，掌握量子粒子群算法的更新迭代流程。"
    content = "利用量子粒子群算法实现对不同维度的变量空间求测试函数最优解。"
    exp_request = "1.使用python编写量子粒子群算法代码，设定算法所需参数：变量空间维度D、种群规模n、迭代次数T。" \
                  "\n2.记录每一代种群的全局最优个体g_best的适应度值，使用matplotlib可视化g_best适应度值随种群迭代的变化曲线。理解并分析种群收敛过程。"
    exp_report = "1.按照实验要求，给出相应结果。" \
                 "\n2.分析量子粒子群的更新方式和收敛过程" \
                 "\n3.对比量子粒子群和粒子群的优劣。" \
                 "\n4.总结实验心得体会"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_nine(request):
    id = "实验-9"
    title = "卷积神经网络分类MINST数据集"
    aim = "熟悉掌握卷积神经网络的定义，了解网络中卷积层、池化层等各层特点，并利用卷积神经网络对MINST数据集进行分类。"
    content = "以MINST数据集为数据，实现对MINST数据集分类的操作，其中MINST数据集有10类分别为手写数字0-9。"
    exp_request = "1. 从网上下载MINST数据集，训练你所编写的网络，要求记录每次迭代的损失值。" \
                  "\n2. 改变卷积神经网络卷积层和池化层数，观察分类准确率。思考网络层数的多少对分类准确率的影响。" \
                  "\n3. 改变卷积神经网络卷积核大小，观察分类准确率。思考网络卷积核大小对分类准确率的影响。" \
                  "\n4. 增加dropout，观察增加前后准确率以及训练误差的变化。"
    exp_report = "1. 按照实验要求，给出相应结果。" \
                 "\n2. 分析卷积层和池化层数对网络的影响。" \
                 "\n3. 分析卷积核大小、是否增加dropout对网络的影响。" \
                 "\n4. 总结实验心得体会。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_eight(request):
    id = "实验-8"
    title = "基于神经网络的优化计算问题"
    aim = "掌握连续Hopfield神经网络的结构和运行机制，理解连续Hopfield神经网络用于优化计算的基本原理，掌握连续Hopfield神经网络用于优化计算的一般步骤。"
    content = "采用Python3.6编写基于连续Hopfield神经网络求解TSP问题的程序"
    exp_request = "1.编写基于连续Hopfield神经网络求解TSP问题的程序，给出15个城市和20个城市的求解结果（包括最短路径和最佳路线），分析Hopfield神经网络求解不同规模TSP问题的算法性能。" \
                  "\n2.对于同一个TSP问题（列入15个城市的TSP问题），设置不同的网络参数，分析不同参数对算法结果的影响。"
    exp_report = "1.画出连续Hopfield神经网络求解TSP问题的流程图。" \
                 "\n2.根据实验内容，给出相应结果和分析。" \
                 "\n3.总结连续Hopfield神经网络和遗传算法用于TSP问题求解时的优缺点。" \
                 "\n4.提交源代码。" \
                 "\n5.总结实验心得和体会"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_seven(request):
    id = "实验-7"
    title = "采用BP神经网络分类MINST数据集实验"
    aim = "熟悉掌握BP神经网络的定义，并利用BP神经网络对MINST数据集进行分类。"
    content = "以MINST数据集为数据，实现对MINST数据集分类的操作，其中MINST数据集有10类分别为手写数字0-9。"
    exp_request = "1. 从网上下载MINST数据集，训练你所编写的网络，要求记录每次迭代的损失值。" \
                  "\n2. 改变BP神经网络隐藏层的层数，观察分类准确率。思考网络层数的多少对分类准确率的影响。"
    exp_report = "1. 按照实验要求，给出相应结果。" \
                 "\n2. 分析隐藏层的层数对网络的影响。" \
                 "\n3. 总结实验心得体会。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_six(request):
    id = "实验-6"
    title = "遗传算法求TSP问题实验"
    aim = "熟悉和掌握遗传算法的原理、流程和编码策略，理解求解TSP问题的流程并测试主要参数对结果的影响，掌握遗传算法的基本实现方法"
    content = "用遗传算法求解不用规模（如10个城市，20个城市，100个城市）的TSP问题。"
    exp_request = "1用遗传算法求解不用规模（如10个城市，20个城市，100个城市）的TSP问题" \
                  "\n2.对于用一个TSP问题，设置不同的种群规模、交叉概率和变异概率。" \
                  "\n3设置种群规模为100，交叉概率为0.85，变异概率为0.15，然后增加一种变异策略（如相邻两点互换变异、逆转变异或插入变异）和1种个体选择概率分配策略用于求解同一TSP问题。"
    exp_report = "1.画出遗传算法求解TSP问题的流程图。" \
                 "\n2.分析遗传算法求解不用规模的TSP问题的算法性能。" \
                 "\n3.对于用一个TSP问题，分析种群规模、交叉概率和变异概率对算法结果的影响。 " \
                 "\n4.增加1中变异策略和1中个体选择概率分配策略，比较求解同一TSP问题时不同变异策略及不同个体选择分配策略对算法结果的影响。" \
                 "\n5.提交源程序。" \
                 "\n6.总结实验心得体会。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_five(request):
    id = "实验-5"
    title = "遗传算法求函数最大值实验"
    aim = "熟悉和掌握遗传算法的原理、流程和编码策略，并利用遗传算法求解函数优化问题，理解求解流程并测试主要参数对结果的影响。"
    content = "用python求解函数的最值。"
    exp_request = "1. 用遗传算法求解下列函数的最大值，设定求解精度到15位小数。" \
                  "\n（1）设计及选择上述问题的编码、选择操作、交叉操作、变异操作以及控制参数等，给出最佳适应度和最佳个体图。" \
                  "\n（2）使用相同的初始种群，设置不同的种群规模，如5、20和100，初始种群的个体取值范围为[0,10]，然后求得相应的最佳适应度、平均适应度和最佳个体，分析种群规模对算法性能的影响。" \
                  "\n（3）设置种群规模为20，初始种群的个体取值范围为[0,10]，选择不同的选择操作、交叉操作和变异操作，然后独立运行算法10次，分析比较采用不同的选择策略、交叉策略和变异策略的算法运行结果。" \
                  "\n2.用遗传算法求解下面Rastrigin函数的最小值，设定求解精度到15位小数。" \
                  "\n（1）设计及选择上述问题的编码、选择操作、交叉操作、变异操作以及控制参数等，并画出最佳适应度和最佳个体图。" \
                  "\n（2）设计种群不同的初始范围，如[1,1.1]、[1,100]、和[1,2]，画出相应的最佳适应度值和平均距离图" \
                  "\n（3）设置不同的交叉概率，画出无变异的交叉，无交叉的变异以及交叉概率为0.8时最佳适应度值和平均距离图"
    exp_report = "1.画出遗传算法的算法流程图。" \
                 "\n2.根据实验内容，给出相应的结果以及结果分析。" \
                 "\n3.总结遗传算法的特点，并说明适应度函数在遗传算法中的作用。" \
                 "\n4.总结实验心得体会。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_one(request):
    id = "实验-1"
    title = "产生式系统实验"
    aim = "熟悉一阶谓词和产生式表示法，掌握产生式系统的运行机制，以及基于规则推理的基本方法。"
    content = "设计并编程实现一个小型产生式系统（如分类、诊断等类型）。"
    exp_request = "1.具体应用领域自选，具体系统名称自定。" \
                  "\n2.用一阶谓词逻辑和产生式规则作为知识表示，利用产生式系统实验程序，建立知识库，分别运行正、反向推理。"
    exp_report = "1.系统设置，包括系统名称和系统谓词，给出谓词名及其含义。" \
                 "\n2.编辑知识库，通过输入规则或修改规则等，建立规则库。" \
                 "\n3.建立事实库（综合数据库），输入多条事实或结论。" \
                 "\n4.运行推理，包括正向推理和返乡推理，给出相应的推理过程、事实区和规则区。" \
                 "\n5.总结实验心得和体会"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_two(request):
    id = "实验-2"
    title = "洗衣机模糊推理系统实验"
    aim = "理解模糊逻辑推理的原理及特点，熟练应用模糊推理。"
    content = "采用python设计洗衣机洗涤时间的模糊控制。"
    exp_request = "1、是一种以模糊判断为前提，运用模糊语言规则，推出一个新的近似的模糊判断结论的方法。" \
                  "\n2、模糊逻辑推理是一种不确定性的推理方法，其基础是模糊逻辑，它是在二值逻辑三段论的基础上发展起来的。" \
                  "\n3、前期缺乏现代形式逻辑中的性质，理论上不够完善。但是这种推理方法得到的结论与人的思维一致或相近，在应用实践中证明是有用的。许多学者在模糊逻辑和模糊推理的性质方面展开了卓有成效的研究。"
    exp_report = "1.确定输入/输出的模糊子集以及论域。" \
                 "\n2.选择控制规则。" \
                 "\n3.规则的运算关系。" \
                 "\n4.通过最大隶属度函数来计算模糊控制输出的量化值。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_three(request):
    id = "实验-3"
    title = "A*算法求解八数码问题实验"
    aim = "熟悉和掌握启发式搜索的定义、估价函数和算法过程，并利用A*算法求解N数码难题，理解求解流程和搜索顺序。"
    content = "以8数码问题和15数码问题为例实现A*算法的求解程序（编程语言不限），要求设计两种不同的估价函数。"
    exp_request = "1. 设置相同的初始状态和目标状态，针对不同的估价函数，求得问题的解，比较他们对搜索算法性能的影响，包括扩展节点数、生成节点数等." \
                  "\n2.设置与上述1相同的初始状态和目标状态，用宽度优先搜索算法（即令估计代价h（n）=0的A*算法）求得问题的解，以及搜索过程中的扩展节点数、生成节点数。" \
                  "\n3.实现A*算法求解15数码问题的程序，设计两种不同的估价函数，然后重复上述1和2的实验内容。"
    exp_report = "1. 分析不同的估价函数对A*算法性能的影响。" \
                 "\n2. 根据宽度优先搜索算法和A*算法求解8、15数码问题的结果，分析启发式搜索的特点。" \
                 "\n3. 画出A*算法求解N数码问题的流程图。" \
                 "\n4. 提交源程序。" \
                 "\n5. 总结实验心得体会。"
    key_code_url = "../static/exp_code/exp_4.md"
    vedio_path = "../static/vedio/exp_4.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)


def to_exp_four(request):
    id = "实验-4"
    title = "A*算法求解八数码问题实验"
    aim = "熟悉和掌握启发式搜索的定义、估价函数和算法过程，并利用A*算法求解N数码难题，理解求解流程和搜索顺序。"
    content = "以8数码问题和15数码问题为例实现A*算法的求解程序（编程语言不限），要求设计两种不同的估价函数。"
    exp_request = "1. 设置相同的初始状态和目标状态，针对不同的估价函数，求得问题的解，比较他们对搜索算法性能的影响，包括扩展节点数、生成节点数等." \
                  "\n2.设置与上述1相同的初始状态和目标状态，用宽度优先搜索算法（即令估计代价h（n）=0的A*算法）求得问题的解，以及搜索过程中的扩展节点数、生成节点数。" \
                  "\n3.实现A*算法求解15数码问题的程序，设计两种不同的估价函数，然后重复上述1和2的实验内容。"
    exp_report = "1. 分析不同的估价函数对A*算法性能的影响。" \
                 "\n2. 根据宽度优先搜索算法和A*算法求解8、15数码问题的结果，分析启发式搜索的特点。" \
                 "\n3. 画出A*算法求解N数码问题的流程图。" \
                 "\n4. 提交源程序。" \
                 "\n5. 总结实验心得体会。"
    key_code_url = "../static/exp_code/exp_5.md"
    vedio_path = "../static/vedio/exp_5.mp4"
    exp_dict = {'id': id, 'title': title, 'aim': aim, 'content': content, 'exp_request': exp_request,
                'exp_report': exp_report, 'vedio_path': vedio_path, 'key_code_url': key_code_url}
    return render(request, 'exp.html', exp_dict)
