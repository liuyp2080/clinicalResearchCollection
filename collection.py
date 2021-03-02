# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image
import numpy as np
st.set_page_config('临床研究Station',page_icon='random')
st.balloons()

# st.sidebar.checkbox('标准化')
# st.sidebar.checkbox('预测模型')
# st.sidebar.checkbox('观点')
title='''<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">临床研究Station</h2>
</div>'''
st.write(title, unsafe_allow_html=True)
# image=Image.open('test.jpg')
# st.image(image,caption='test', use_column_width=True)
st.write('### ')
st.info('Welcome:heart:!      这里是一个关于临床科研相关知识和思考的网站，涵盖临床研究的多个方面，希望能让您有所收获! ————临床研究Station')


st.write('请选择感兴趣的板块:')
col1,col2,col3,col4=st.beta_columns(4)
select1=col1.checkbox('临床研究标准化')
select2=col2.checkbox('临床预测模型')
select3=col3.checkbox('临床研究设计')
select4=col4.checkbox('动态列线图',value=True)
if select1:
    st.write('随着临床研究这个领域的不断发展和成熟，在前人的不断探索下，形成了许多经验，这些经验经过专家群体或者专业机构的总结、扩展成为\n'
        '业内人士普遍接受的行为准则，这里称为“标准化”。虽说在临床研究领域并没有强制要求一定要按照标准化的流程来进行, 然而尽可能地学习并\n'
        '遵守这些行为准则，有助于快速地且质量较高的开展自己的临床研究，避免可能产生的种种错误, 从而在短期内上手且产出较高质量的研究\n'
        '成果。如果说临床科研纷繁复杂，犹如险峻陡峭的华山，而”标准化”则是从事临床科研的一条捷径。')

    st.write('临床研究包含多个环节, 标准化是针对临床试验的每个环节来制定的。目前主要的标准化环节有：1、研究报告格式和内容的标准化，之所以要进行这方面的标准化是因为\n'
         '许多报告格式和内容不规范, 试验中许多重要的, 体现试验质量的参数没有被报告出来，导致读者无从判断试验结论的可靠性，所以对研\n'
         '究报告的格式和内容进行了规范; 2.临床研究数据库建设的标准化。数据库要求一方面安全的存储数据，另一方面便于数据的后续分析和交流，\n'
         '在临床数据和分析数据之间起到“承前启后”的作用，有助于更充分地管理和利用收集的数据，数据的交流和合并; 3.核心结局变量集。结局变量是\n'
         '临床试验中所要收集的三大类变量（预测变量、混杂变量和结局变量）之一，其标准化有助于各个临床试验之间进行相互地比较，也为后续的Meta\n'
         '分析奠定基础,规范结局变量的收集，避免变量收集过多或者收集不全的情况。')
    st.subheader("一、核心结局指标集")
    st.write("**简介**：在从事临床研究过程中的可以体会到，自己领域的系列研究以及同行的研究在收集结局变量方面往往有相似性，这是结局变量标准化的基础：\n"
         "同领域内的研究往往有相同的结局变量。某些结局变量收集不齐全会直接导致试验结论不全面，\n"
         "与同行的研究不可比(结局指标不同)。在这样的背景下，临床试验核心指标集（COS）应运而生，COS是某特定病证相关的所有临床研究都应测量\n"
         "和报告的、最少但最重要的指标集合，是由国际学术组织有效性试验核心结局指标测量（[COMET](www.comet-initiative.org/)）成立并提出倡议。\n"
         "该网站上建立了COS数据库，可以查询下载目前已经建立的各个研究领域的COS。需要指出的是，许多小的研究领域并没有现成的COS，需要自己进行创建，\n"
         "为此，该组织发布了COS的制定标准,指导COS的创建。2019年7月19日，中国循证医学\n"
        "中心和天津中医药大学循证医学中心共建的中国临床试验核心指标集研究中心在天津中医药大学新校区揭牌，标志着该项标准化工作受到国内专家的重视。")
    st.write('### --Collection--')
    st.info('[核心结局指标集COS文档](https://pan.baidu.com/s/1IYWHdoAZKkNOiW-v06AM5Q)（提取码-lcyj）')
    st.subheader('二、零成本建立中小型临床数据库')
    st.write("**简介：**建立临床数据库过程中涉及的两个标准化是“数据组织形式的标准化”和“变量名的标准化”。建立数据库肯定是为了长期的研究，较少是\n"
         "仅仅为了一个小课题，所以需要收集的数据可能比较多，包括某个疾病的方方面面，需要分门别类，每一类数据组成一张表格，多个表格之间以唯\n"
         "一的识别码进行关联，构建成所谓的关系型数据库；同一类的数据内部按照纵向数据结构或横向数据结构组织在同一张表格中。这里我们借鉴[CDISC](https://www.cdisc.org/)成型的\n"
         "方法构建我们自己的临床性数据库，避免了从头学习复杂的数据库构建的相关知识。“变量名的标准化”，也称为“公共数据元”，是在相似的研究中统一变量名称\n"
         "方便了后续的数据分析(编程)和数据之间的合并和交换。我们从实际经验中总结了零成本建立中小型数据库的方法，并将其发表在\n"
         "网络上，可以用关键词“零成本”“临床数据库”进行搜索阅读。")
    st.write('### --Collection--')
    st.success('[零成本建立中小型临床数据库资料](https://pan.baidu.com/s/1Qon9dAy_OTE7B54h8nlPPw)（提取码-lcyj）')
    st.info('资料内容包括CDISC相关中英文指南、零成本建立数据的流程介绍')
    st.subheader('三、试验结果报告的标准化')
    st.write("**简介：**这是由国际上科学家和编辑共同制定的一系列科研报告的规范，以提高临床研究报告的质量。这些规范包括《随机对照试验规范》\n"
         "（[CONSORT](http://www.consort-statement.org/)）、《观察性研究报告标准》（[STROBE](https://www.strobe-statement.org/index.php?id=strobe-home)）\n"
         "、《非随机对照试验报告规范》（[TREND](https://www.cdc.gov/trendstatement/)）和《诊断性研究标准》（STARD）。")
    st.write('### --Collection--')
    st.warning('[试验结果报告标准下载](https://pan.baidu.com/s/1sVbkHpq_oVsUtqCWP6slDA)（提取码-lcyj）')
    st.write("**------------------------------------------------------------------------------------------------------------**")
    st.write('--The End-- ')
if select2:

    # st.write('### 临床预测模型')
    st.write('临床预测模型的开发属于“医学检验研究设计”大类，其目标在于应用数学方法开发新的（复合的）检验从而改善临床决策，并非评价已有的检验。\n'
             '预测模型研究利用临床资料或实验室检查或两者结合来进行研究,制作出来的模型可用于辅助临床决策是贴近临床的一种\n'
             '科研形式，并且对实验技能要求不高，医生不需要用额外的时间做实验，不需要关注临床研究以外的科研资料，所以也是适合医生开展的科研形式。\n'
             '一个合格的临床研究预测模型，应该具备以下特点：1、研究对象应该与应用该规则的人群类似；2、应用了合适的数学方法构建模型，可选的方法包括\n'
             '逻辑回归、Cox风险比例模型、机器学习和深度学习；3、进行了充份的验证。')
    st.write('结合医学数据的一些特点，我们在具体操作上也总结了一些经验:')
    st.write('* 模型可操作性要强，体现在预测变量的数量不宜过多，有的研究宁可牺牲一些的预测准确度也要减少预测变量的数量。')
    st.write('* 尝试用多种数学方法进行模型的构建或者采用集成或综合的方法来构建模型，特别是根据构建原理迥异的模型，比如决策树、神经网络、逻辑回归，然后从中选择较优的模型。')
    st.write('* 样本量不宜过少，临床上的样本量通常不大，需要采用交叉验证或采用集成算法等数学方法进行一定程度的克服。')
    st.write('* 模型构建过程中重视对原始数据的处理和模型超参数的调节等。')

    st.write('### --Collection--')
    st.write('[临床预测模型资料](https://pan.baidu.com/s/1jYvvYIPBvKs8JwGVXszKeA)（提取码-lcyj）')
    st.info('资料内容包括临床预测模型相关文献、中文指南')
    # st.write('### 生物信息学分析')
    st.write(
        '*----------------------------------------------------------------------------------------------------------------*')
    st.write('--The End-- ')
if select3:
    st.write('### 一、不是所有的统计方法都需要了解')
    st.write('临床研究技能已经被列为一个临床医师的核心职业技能之一，从纷繁复杂的影响疾病因素中找出规律是医学进步的途径也是临床医生无可替代的责任。\n'
             '对于想从事临床研究的医生来说，当然是了解临床研究的知识愈多愈好，但是繁多而复杂的临床研究的知识常常使临床医生无从下手，甚至望而却步。')
    st.write('要解决这个问题，除了加强学习之外，临床医生要明确的一点就是，不是所有的临床研究的知识都需要了解。首先，根据研究目的，临床研究的知识可以\n'
             '分为因果关系的研究设计和医学检验的研究设计两大部分。一般临床科室（内科、外科等）的临床医生往往期望发现疾病相关因子（预测因素）与疾病结局\n'
             '（结局因素）之间的因果关系，就只需要了解因果关系的研究设计。这也是和这类医生的诊断疾病，去除病因等日常临床工作紧密相关的。另一方面，\n'
             '医学检验的研究设计是考察某一个因子是否适合用于预测疾病结局，它不强调两者之间是否具有因果关系，而是更加关注的是两者关系的精确性、准确性\n'
             '和特异性等等指标。这方面大家可以和检验科的工作进行类比，检验科的医生往往不关心检验指标和疾病之间是否存在因果关系，而只关心检验指标是不是\n'
             '能够反映疾病状况。其次，即使在因果关系的研究设计中，又可以细分为观察性研究设计和随机对照盲法的研究设计。后者多是用在临床药物试验的过程中，\n'
             '实施难度大，要求更多的人力和物力，需要有前期大量的动物实验和临床试验的结果作为前期工作，且与医生的日常工作距离较远，所以除非科室有较好的临床\n'
             '研究的条件或研究任务，也可暂时不做了解。')
    st.write('综上所述，在所有的临床研究的知识当中，一般临床医生需要（或是优先）了解的就是因果关系研究设计中的观察性\n'
             '研究设计的相关知识，罗列起来这些知识包括，横断面研究、病例对照研究、队列研究以及相关的统计方法——逻辑回归、线性回归和Cox回归。其它的临床研究的\n'
             '知识都可以作为进阶阶段的内容。')
    st.write('### 二、师兄和师弟的科研经历')
    st.write('教授在学习会上发表演说，强调作为临床医生要担当起一个医生不可推卸的临床科研的责任：发现临床问题，解决临床问题，致力于临床科研。\n'
             '然后，教授出了一个题目：X基因表观修饰水平(连续变量)和糖尿病（和并发症），并交代各位同学根据自己的实际情况设计课题。讲完就飘然离去。')
    st.write('王师兄是临床医学背景，是内分泌科的主治医师。平时在临床工作，接触糖尿病的患者，就设计了适合自己的试验方案：收集科室内糖尿病患者的血液\n'
             '并存储在医院样本库备用检测（准备检测X基因的表观修饰水平），进行随访观察患者糖尿病肾病等的并发症发生情况和可能的影响结局因素（混杂变量）\n'
             '，期望分析获得X基因的表观修饰水平与糖尿病肾病等并发症之间的因果联系。把采集样本的时间作为患者进入队列的时间，因为X基因的表观修饰水平可\n'
             '能受到糖尿病患病年限的影响，所以在结果分析中通过匹配“糖尿病患病年限”或多因素分析中纳入“糖尿病患病时间”进行处理。又因为队列中的患者会\n'
             '在不同的随访时间出现结局，所以通过采用多因素Cox分析得出最后的结果。试验设计的最后一步是估计样本量，通过咨询医院的循证医学中心的老师，\n'
             '王师兄确定了相关的参数：α=0.05，1-β=0.8，效应值（出现结局和未出现结局两组间X基因表观修饰水平的差值），X基因表观修饰水平测量的精确度\n'
             '（标准差），分析方法为t检验，并用PASS软件大概估计样本量。试验设计完成了，开始执行。结果因为没有考虑到结局出现需要较长的时间，导致用了\n'
             '很长的时间收集样本，完成试验的时间不得不延后，也延迟了毕业。王师兄不禁感叹如果科室里事先建立多任务糖尿病病例数据库，并且在样本库里储存\n'
             '了样本，就可以利用病例库来进行这个科研工作，就不会有完成延迟的情况。因为临床试验确认了X基因表观修饰水平是糖尿病某结局之间较强的因果联系，\n'
             '王师兄觉得可以在动物实验上进行验证并探讨其背后的机制，并以此撰写了国家自然科学基金标书来申请课题。')
    st.write('李师弟是检验科背景，不关注X基因表观修饰水平与糖尿病某并发症发生之间的因果关系，而是关注X基因表观修饰水平是否可以作为一个糖尿病某并发症的指标，\n'
             '选择了“诊断试验”的设计：收集门诊所有送到检验科的血样，检测X基因表观修饰水平，并收集患者的基本信息和是否被诊断为糖尿病某并发症的信息，\n'
             '数据分析计算灵敏度、特异度和似然比以及各自的置信区间。同样，李师弟也用PASS软件进行了样本量的计算。李师弟后来得到了阳性的结果，撰写了论文，\n'
             '后续进一步申请了专利，为临床提供新的诊断手段。')
    st.write('教授后来点评，虽然是出于同一个题目，两种设计的关注点不同，人群不同，分析方法不同，但是都符合两个人的背景知识，同样具有可行性。临床试验目前\n'
             '已经形成一定的规范和套路，一个临床医生不论什么学历，都可以学会临床试验的做法，获得这项必备的职业技能。另外，每个人背景不同，关注点不同，\n'
             '不是所有临床试验的方法都要去了解。希望各位在职的学生克服畏难的想法，积极掌握临床试验的规范。')
    st.write('### 三、多元分析方法的运用需正确纳入混杂变量')
    st.write('目前，多元分析方法，如线性回归、Logistic回归和Cox回归等，在观察性临床研究中正得到广泛的使用，其要求将混杂变量带入方程以排除其对结局变量\n'
             '的影响，从而显现出自变量（预测变量）对因变量（结局变量）的相对独立作用。然而多元分析方法使用过程中凸显了一个问题就是混杂因素的收集不全或者\n'
             '不正确进而导致带入方程的变量不全或不正确，这样的研究得出的结论就缺乏说服力，不能作为循证医学的证据。除了少数特殊情况下，比如匹配，不需要测量\n'
             '收集混杂变量，多数情况下都是需要测量混杂变量才可以排除它的影响。另外，有些因素如果被误认为是混杂因素而代入到多元分析方程中，则会得出错误的结论。\n'
             '所以，提高临床研究质量的关键因素之一就是明确混杂变量的收集测量。')
    st.write('混杂因素的定义其首先是可以影响结局变量，同时要求其与预测变量相关（是预测变量的原因、与预测变量伴随或与预测变量有共同的原因，但不是预测变量的结果）。另一种更好理解说法是，混杂变量是其它研究中的预测变量。混杂因素是可以影响结局变量的因素，这一点是明确的，其它研究已经明确的或疑似的结局变量的因素都可以被确定为可能的混杂因素，至于第二点-“与预测变量有关联”-就相对模糊，并且通过某种变通找出两个因素有联系的合理性的情况是常见的，所以在实际操作中，以第一个条件为准，通过全面浏览文献，查询循证医学数据库或是咨询有经验的研究者等方式确定研究中需要测量混杂因素是合理的。特别推荐查询uptodate临床顾问等循证医学数据库，对疾病的影响因素有总结和筛选，是确定研究混杂因素的方便有效的途径。需要确定混杂因素的另一个原因是，某些因素被误认为是混杂因素而纳入到多元方程中会造成计算得出预测变量与结局变量之间虚假的关联。这样的因素包括1.中介因素：混杂因素的定义中会特别提到预测变量不能是待确定因素的原因，因为这样的因素属于中介因素，其原理可以参照李楠等的论述[1]；2.共享效应，指的是多个原因（不局限于预测变量和结局变量）均可导致的某种情况。如果研究者将这样的变量作为研究的入选标准、匹配变量或可能的混杂变量时，会发生限定共享效应（conditioning on a shared effect）所致的偏倚。')
    fig_hunza=Image.open('fig_hunza.png')
    st.image(fig_hunza,
             caption='图1：混杂变量、中介变量和共享效应区别简单示意图。中介变量，受预测变量影响，然后影响结局变量；混杂变量，影响结局变量和预测变量；共享效应，同时受结局变量和预测变量的影响。箭头指向受影响的变量。',
             width=450)
    st.write('最后，常见的另外一种情况是多元方程中纳入无关的变量，或许这样的操作对结果并没有太多的影响，但是收集变量的过程会造成人力和物力的浪费。总之，临床试验中运用多元分析方法过程中，正确纳入混杂因素并避免纳入中介变量和共享效应是保证研究结论确实可信的重要措施')
    st.write('参考文献：')
    st.write('[1]李楠, 石岩岩, 赵一鸣. 中间变量的识别和控制在证实研究假说中的作用[J]. 中华儿科杂志, 2017, 55(10):770-770.')
    st.write('### --Collection--')
    st.write('[临床研究设计学习资料](https://pan.baidu.com/s/1F59Xg2X-0srdPSeKfNYtKQ)（提取码：lcyj）')
    st.write('*----------------------------------------------------------------------------------------------------------------*')
    st.write('--The End-- ')
if select4:

    import streamlit as st
    from PIL import Image
    import numpy as np


    def toweight(ls_hr):
        list_weight = list(map(np.log, ls_hr))
        return list_weight


    st.header('1、甲状腺微小瘤转移概率预测计算器')
    thyroid_nomo = Image.open('thyriod_nom.png')
    st.image(thyroid_nomo, width=400)
    st.info('参考文献:杨瑞,张守鹏,黄韬,明洁,杨鹏,朱俊玲,瞿芳.cN0期甲状腺微小乳头状癌淋巴结转移模型的构建和验证\n'
            '以及手术方式探讨[J].临床耳鼻咽喉头颈外科杂志,2021,35(02):137-140.说明:根据文献介绍，该研究纳入病例670例，预测概率值的阈值为0.55时,中央组淋巴结转移\n'
            '预测的准确率为68.5%。')
    st.sidebar.subheader('1、甲状腺微小瘤转移概率预测')
    para_size = st.sidebar.slider('肿瘤直径', min_value=1.0, max_value=10.0, step=0.1)
    col1, col2, col3 = st.beta_columns(3)
    col1.write('您选择的肿瘤直径是：{}mm'.format(para_size))
    age_select = st.sidebar.radio('性别', ['女', '男'], )
    col2.write('您选择的性别是：{}性'.format(age_select))
    if age_select == '女':
        para_sex = 0
    else:
        para_sex = 1
    para_age = st.sidebar.slider('患者年龄', 10, 75)
    col3.write('您选择的患者年龄是：{}岁'.format(para_age))

    list_para = [para_size, para_sex, para_age]
    list_or = [1.26579, 2.50828, 0.94866]
    betaZero = 0.0665
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者甲状腺微小肿瘤的发生淋巴结转移概率为{:.2f}%:'.format(prob * 100))
#___________________________________________________________________________________
    st.header('2、甲状腺术后低钙风险预测计算器')
    thyroid_hypocalcemia = Image.open('hypocalcemia.png')
    st.image(thyroid_hypocalcemia, width=400)
    st.info('参考文献:李岚,刘畅,肖明.预测甲状腺术后发生低钙血症的风险列线图模型建立[J].重庆医学,2021,50(03):461-465.说明:'
            )
    st.sidebar.subheader('2、甲状腺术后低钙风险预测')
    malignant_select = st.sidebar.radio('恶性肿瘤', ['否', '是'], )
    col1, col2, col3,col4,col5,col6 = st.beta_columns(6)
    col1.write('恶性肿瘤为：{}'.format(malignant_select))
    bilateral_select = st.sidebar.radio('双侧病变', ['否', '是'], )
    col2.write('双侧病变为：{}'.format(bilateral_select))
    central_node_select = st.sidebar.radio('清扫中央组淋巴结', ['否', '是'], )
    col3.write('清扫中央组淋巴结为：{}'.format(central_node_select))
    posterior_capsule_select = st.sidebar.radio('甲状腺后被膜破坏', ['否', '是'], )
    col4.write('甲状腺后被膜破坏为：{}'.format(posterior_capsule_select))
    operation_time_select = st.sidebar.radio('手术时间超过100分钟', ['否', '是'], )
    col5.write('手术时间超过100分钟为：{}'.format(operation_time_select))
    parathyroidectomy_select = st.sidebar.radio('甲状旁腺切除', ['否', '是'], )
    col6.write('甲状旁腺切除为：{}'.format(parathyroidectomy_select))

    paras=[]
    for i in [malignant_select,bilateral_select,central_node_select,posterior_capsule_select,operation_time_select,parathyroidectomy_select]:
        if i == '否':
            para = 0
        else:
            para = 1
        paras.append(para)
    list_para=paras
    list_or = [2.546,3.204,2.582,3.508,3.658,2.553]
    betaZero = -4.668
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者甲状腺术后发生低钙血症概率为{:.2f}%:'.format(prob * 100))

#____________________________________________________________________________________
    st.header('2、甲状腺癌患者术后出血风险预测计算器')
    thyroid_bloody = Image.open('bloody.png')
    st.image(thyroid_bloody, width=400)
    st.info('参考文献:郑艳,张茜,孙菲.个人化预测甲状腺癌患者术后出血风险的列线图模型的建立[J].医学综述,2021,27(03):609-613.说明:'
            )
    st.sidebar.subheader('2、甲状腺癌患者术后出血风险预测')
    hypertension_select = st.sidebar.radio('合并高血压', ['否', '是'], )
    col1, col2, col3,col4,col5,col6 = st.beta_columns(6)
    col1.write('合并高血压为：{}'.format(malignant_select))
    fullcut_select = st.sidebar.radio('甲状腺全切', ['否', '是'], )
    col2.write('甲状腺全切为：{}'.format(bilateral_select))
    tumor_stage_select = st.sidebar.radio('肿瘤分期达III期', ['否', '是'], )
    col3.write('肿瘤分期达III期为：{}'.format(central_node_select))
    tumor_size_select = st.sidebar.radio('肿瘤尺寸达4cm', ['否', '是'], )
    col4.write('肿瘤尺寸达4cm为：{}'.format(posterior_capsule_select))
    nerve_invasion_select = st.sidebar.radio('喉返神经浸润', ['否', '是'], )
    col5.write('喉返神经浸润为：{}'.format(operation_time_select))
    node_metastasis_select = st.sidebar.radio('淋巴结转移', ['否', '是'], )
    col6.write('淋巴结转移为：{}'.format(node_metastasis_select))

    paras=[]
    for i in [hypertension_select,fullcut_select,tumor_stage_select,tumor_size_select,nerve_invasion_select,node_metastasis_select]:
        if i == '否':
            para = 0
        else:
            para = 1
        paras.append(para)
    list_para=paras
    list_or = [12.33,6.12,4.137,5.118,16.477,5.296]
    betaZero = -5.256
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者甲状腺术后出血的风险为{:.2f}%:'.format(prob * 100))
 #___________________________________________________________________________
    st.header('4、四肢骨肉瘤生存率预测计算器')
    bone_tumor = Image.open('bone_tumor.jpg')
    st.image(bone_tumor, width=400)
    st.info('参考文献：来源于柳昌全,赵广雷,陈康明,王思群,魏亦兵,黄钢勇,陈杰,石晶晟,夏军,陈飞雁.基于SEER数据库的四肢骨肉瘤预后相关列线图的\n'
            '构建[J].中国骨与关节杂志,2020,9(08):563-571.说明：所有四肢骨肉瘤患者的数据来源于SEER 数据库 (1995年至2014年)；\n'
            '组织学类型是骨肉瘤 ( 9180-普通型骨肉瘤，9181-软骨母细胞性骨肉瘤，9182-纤维母细胞性骨肉瘤，9183-血管扩张性骨肉瘤，9184-paget’s 骨肉瘤，9185-小细胞骨肉瘤，9186-中心性骨肉\n'
            '瘤，9187-骨内高分化骨肉瘤，9192-骨旁骨肉瘤，9193-骨膜骨肉瘤，9194-高等级骨表面骨肉瘤。')
    st.sidebar.subheader('4、四肢骨肉瘤生存率预测')
    age_select = st.sidebar.radio('患者年龄分层', ['<21', '21~46', '>=46'])
    if age_select == '<21':
        para_age_1 = 0
        para_age_2 = 0
    elif age_select == '21~46':
        para_age_1 = 1
        para_age_2 = 0
    else:
        para_age_1 = 0
        para_age_2 = 1
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    col1.write('您所选择的年龄是:{}'.format(age_select))
    period_select = st.sidebar.radio('肿瘤分期', ['局部性', '区域性', '远处转移'])
    if period_select == '局部性':
        para_period_1 = 0
        para_period_2 = 0
    elif period_select == '区域性':
        para_period_1 = 1
        para_period_2 = 0
    else:
        para_period_1 = 0
        para_period_2 = 1
    col2.write('您所选择的肿瘤分期是:{}'.format(period_select))
    operation = st.sidebar.radio('手术与否', ['是', '否'])
    if operation == '是':
        para_operation = 0
    else:
        para_operation = 1
    col3.write('您所选择的手术情况是:{}'.format(operation))
    size = st.sidebar.radio('肿瘤尺寸', ['<13.9', '>=13.9'])
    if size == "<13.9":
        para_size = 0
    else:
        para_size = 1
    col4.write('您所选择的肿瘤尺寸是:{}'.format(size))
    type = st.sidebar.selectbox('病理类型', ['9192', '9182', '9186', '9183', '9180', '9181'])
    if type == '9192':
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9181':
        para_type_1 = 1
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9180':
        para_type_1 = 0
        para_type_2 = 1
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9183':
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 1
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9186':
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 1
        para_type_5 = 0
    else:
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 1
    col5.write('您所选择的肿瘤病理类型是:{}'.format(type))

    def toweight(ls):
        list_weight = list(map(np.log, ls))
        return list_weight

    # output
    basic_rate_adopt_1 = 0.9883522937528895
    basic_rate_adopt_3 = 0.9409661226740611
    basic_rate_adopt_5 = 0.9175902823690558
    hr = [1.63, 3.88, 1.31, 3.50, 2.10, 1.40, 2.635, 2.464, 2.151, 1.719, 1.161]
    list_para = [para_age_1, para_age_2, para_period_1, para_period_2, para_operation, para_size, para_type_1,
                 para_type_2, para_type_3, para_type_4, para_type_5]
    list_weight = toweight(hr)
    var = [a * b for a, b in zip(list_weight, list_para)]
    survival_rate_1year = basic_rate_adopt_1 ** np.exp(sum(var))
    survival_rate_3year = basic_rate_adopt_3 ** np.exp(sum(var))
    survival_rate_5year = basic_rate_adopt_5 ** np.exp(sum(var))
    st.success('该患者的1年生存率为{:.2f}%，3年生存率为{:.2f}%，5年生存率为{:.2f}%。'.format(survival_rate_1year * 100, survival_rate_3year * 100,survival_rate_5year * 100))
    # st.subheader("团队介绍")
    # st.write('团队致力于提供医学数据库建设、流行病学试验设计、论文统计学\n'
    #          '方法分析、临床样本收集、生物信息学分析、数据分析、数据可视化等七类医学相关的方法学支持。“学组”成员来源于临床医学专业、\n'
    #          '统计学专业、生物信息学专业和生物学专业，并在各自领域有多年的研究经验，为开展相关研究和服务奠定了坚实的基础。')
    # st.write('欢迎徐州和淮海地区的从事临床相关研究的学生和老师咨询！')
    # st.info('学组主要成员介绍:')
    # team_df=pd.DataFrame({'姓名':['李 睿','刘岳鹏','王秀力','刘学奎','吕 茜','李 阳'],
    #                       '专业':['临床医学','神经生物学','人体解剖与组织胚胎学','统计学','分子生物学','生物信息学'],
    #                       '专修方向':['细胞行为研究','临床预测模型','临床组织样本利用和管理','临床研究设计和数据统计','基因和蛋白检测','基因数据分析']
    #                       },index=[1,2,3,4,5,6])
    # st.table(team_df)
    # st.subheader("合作服务内容:")
    # st.write('* **生物医学统计方法咨询：**回答统计过程中可以采用的技巧和方法。')
    # st.write('* **临床研究设计：**在开展临床试验之初，根据研究问题对试验的整个过程进行规划。')
    # st.write('* **生物信息学分析：**分析和展示基因相关的数据。')
    # st.write('* **临床数据分析：**对临床数据进行清理、分析因果关系。')
    # st.write('* **临床预测模型构建：**用机器学习和深度学习的方法构建临床预测模型（python）。')
    # st.write('* **数据可视化：**制作数据相关的图。')
    # st.write('* **临床数据库建设：**为临床科室或个人建立临床数据库进行软件和数据库设计方面的指导。')
    # st.write('* **组织样本收集指导：**为如何收集和利用临床样本提供经验指导。')
    # st.subheader('联系方式:')
    # st.write('咨询微信群:email:：临床研究Station')
    # st.write('咨询电话:telephone:：15351633096')

