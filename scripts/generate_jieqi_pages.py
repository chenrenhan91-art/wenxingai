#!/usr/bin/env python3
"""
生成24节气命理运势页面
输出目录：/24jieqi/
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE_DIR, "24jieqi")

JIEQI = [
    {
        "slug": "lichun",
        "name": "立春",
        "date": "2月3日或4日",
        "wuxing": "木",
        "season": "春",
        "meaning": "春季开始，万物萌生，木气生发之始。",
        "mingli": "立春是紫微斗数流年换算的关键节点，也是八字四柱中「年柱」更替的分界线。命盘中木星系主星（天机、太阴）在此节气前后运势变动最为明显。",
        "faqs": [
            ("立春对八字命理有什么影响？", "立春是传统命理中年柱更换的重要时间节点——命理算命以立春为新年的起算点，而非农历初一。换句话说，生于立春前的人仍属前一年年柱，生于立春后才算新年。这一点与日历新年不同，在排四柱八字时尤为关键。"),
            ("立春时节哪些生肖运势最旺？", "立春五行属木，生肖虎和兔（寅卯木）在此节气最得天时；木生火，因此属马、属蛇的人也有助力。属金的生肖（猴、鸡）则需注意木克土、土生金链条中可能出现的变动。"),
            ("紫微斗数如何看立春流年运势？", "在紫微斗数中，流年宫位以农历为基础，但大运和流年交接参考节气。命盘天机星、太阴星入旺宫位者，立春前后往往出现事业或人际关系的新转机。可通过问星AI输入生辰查看个人流年命盘。"),
            ("立春有哪些命理择日习俗？", "民间有「立春接春」习俗，认为此日动土、开业、搬迁大吉。从八字择日角度看，立春日干支与个人命盘形成三合或六合者，行事最为顺遂。"),
        ],
        "tips": "立春日五行木气旺盛，适合启动新项目、签约、搬入新居。属金人需避免重大财务决策。",
    },
    {
        "slug": "yushui",
        "name": "雨水",
        "date": "2月18日或19日",
        "wuxing": "木",
        "season": "春",
        "meaning": "雨水滋润大地，木气舒展，草木萌发。",
        "mingli": "雨水节气五行仍属木，但木中带水，天干壬癸水能量渗入。命盘中水系主星（天同、天梁）在此节气前后能量较为活跃，感情与人际关系易有新变化。",
        "faqs": [
            ("雨水节气在命理上代表什么？", "雨水节气木气中带水，象征资源流动与滋养。命理上此时适合梳理人际关系、整合资源。水克火，命盘中太阳、廉贞星旺盛者需注意情绪管理。"),
            ("雨水时节做什么最有利于财运？", "雨水属水木交接，木主生长、水主财禄流动。此时期适合拓展人脉、商谈合作。八字日主为木者财运较旺；日主为火者需防破财，建议守成。"),
            ("雨水节气与婚恋感情有什么关联？", "雨水水木并重，天同星（感情宫位的重要星曜）能量升涨，感情运相对活跃。单身者在此节气前后更易邂逅；有伴侣者需注意雨水带来的情绪波动影响沟通。"),
            ("如何用紫微斗数判断雨水时节的运势？", "通过问星AI输入出生年月日时，可生成个人命盘并查看流月运势。雨水节气对应流月宫位入「天同」或「太阴」者，感情与人际发展顺遂；入「破军」者则易有变动。"),
        ],
        "tips": "雨水时节感情运较旺，适合坦诚沟通、维护感情。事业方面宜广结善缘，不宜冒进投资。",
    },
    {
        "slug": "jingzhe",
        "name": "惊蛰",
        "date": "3月5日或6日",
        "wuxing": "木",
        "season": "春",
        "meaning": "春雷惊醒蛰虫，阳气升腾，万物复苏。",
        "mingli": "惊蛰木气最旺，阳气急速上升。紫微斗数中天机星（代表思维与行动）在此节气能量最强，适合启动新计划、学习进修。命盘官禄宫在此节气前后变动影响最大。",
        "faqs": [
            ("惊蛰节气对事业运势有什么影响？", "惊蛰是木气最旺之时，象征行动力和破旧立新。命理上此节气利于跳槽转职、开创事业。八字日主为木的人在此节气前后往往遇到重要的事业转机；日主为金者则要防止被迫调整。"),
            ("惊蛰是什么意思？与算命有什么关系？", "惊蛰字面意思是春雷惊醒冬眠的虫兽。在八字命理中，惊蛰是春季木气最旺的节气，对应「卯月」开始。卯月（虎年）的人在此节气前后往往有转机；生于卯月的人命盘木气极旺，性格主动果断。"),
            ("紫微斗数惊蛰流月哪些星曜最活跃？", "惊蛰对应流月宫位进入木旺之宫时，天机星（思维策划）、破军星（变革开拓）能量最为活跃。命盘天机化科者在惊蛰前后学习和考试运极佳；天机化忌者则需防决策失误。"),
            ("惊蛰适合开业或签合同吗？", "惊蛰日阳气盛旺，是传统择日中开业、签约的吉日。但需对照个人命盘，若个人流年遇「化忌」冲命宫，则需谨慎行事，宜先通过问星AI查询个人流年是否有煞气冲克。"),
        ],
        "tips": "惊蛰是一年中行动力最强的节气，适合开展新计划、参加考试、争取晋升机会。避免冲动决策伤感情。",
    },
    {
        "slug": "chunfen",
        "name": "春分",
        "date": "3月20日或21日",
        "wuxing": "木",
        "season": "春",
        "meaning": "昼夜等长，阴阳平衡，木气达到极盛。",
        "mingli": "春分阴阳各半，五行木气至极而转。紫微斗数看此节气重点在「平衡」——命盘中夫妻宫、合盘关系在春分前后最能见到真实状态，适合评估感情和伙伴关系。",
        "faqs": [
            ("春分在命理上有什么特殊意义？", "春分是阴阳等分的时刻，象征平衡与抉择。命理上此节气适合回顾过去三个月的得失，调整方向。命盘中太阳（阳）与太阴（阴）同时活跃，男女感情运均有波动。"),
            ("春分时节感情运如何？", "春分阴阳平衡，夫妻宫与感情宫位能量均等，感情中的矛盾和优势都会浮现。此时是评估感情关系的好时机。命盘夫妻宫入「天梁」者春分前后感情稳健；入「廉贞」或「七杀」者需注意争执。"),
            ("春分节气利于做哪些事情？", "春分适合平衡规划：既适合签订合作协议（阳刚事务），也适合处理家庭、感情（阴柔事务）。八字中木火通明格局的人在春分前后综合运势最旺。"),
            ("怎么用问星AI查春分流月运势？", "在问星AI中输入出生年月日时，可生成个人紫微命盘，并查询当前流月（春分对应农历二月中至三月初）的宫位运势，包括财运、感情、事业的具体分析。"),
        ],
        "tips": "春分时节宜平衡规划，感情和事业两手抓。避免极端决策，利用阴阳等分的能量做长期布局。",
    },
    {
        "slug": "qingming",
        "name": "清明",
        "date": "4月4日或5日",
        "wuxing": "木",
        "season": "春",
        "meaning": "天气清朗，万物洁净，木气开始向火过渡。",
        "mingli": "清明是传统祭祖节气，命理上此时与「祖德荫庇」相关，父母宫和福德宫的影响在此节气前后较为显著。命盘福德宫旺盛者，清明前后往往感受到无形助力。",
        "faqs": [
            ("清明节气对命理运势有什么特殊影响？", "清明五行木气渐退、火气渐生。命理上此节气象征「清算」与「更新」，旧的事项得到了结，新的气运开始积累。此时查看命盘父母宫与福德宫，可了解祖先福荫对当年运势的影响。"),
            ("清明是否不宜做重大决策？", "民间习俗认为清明前后阴气较重，不宜大动土木或开张。从八字命理角度，清明对应卯月末至辰月初，五行从木转土，属于气运交接期，确实不宜冒进。但若个人命盘流年大吉，则不必过度迷信。"),
            ("清明时节哪些宫位需要关注？", "清明对应流月父母宫和福德宫能量较强。紫微斗数中「天梁」星（代表长辈庇护）在此节气若入旺宫，往往有长辈相助或遗产方面的好消息；若化忌则需注意长辈健康。"),
            ("清明扫墓对运势有影响吗？", "从命理风水角度，清明祭祖有助于激活「祖德」能量，对命盘福德宫偏弱的人有补气作用。扫墓时宜保持虔诚态度，可通过问星AI了解自身福德宫状态。"),
        ],
        "tips": "清明节气宜祭祖、整理心绪、规划下季度目标。不宜仓促签约或大额投资，以气运平稳过渡为主。",
    },
    {
        "slug": "guyu",
        "name": "谷雨",
        "date": "4月19日或20日",
        "wuxing": "土",
        "season": "春",
        "meaning": "雨水充沛，谷物生长，土气开始彰显。",
        "mingli": "谷雨是春季最后一个节气，土气渐旺、木气收尾。命理上此时是「收获春季努力」的节点，命盘田宅宫与财帛宫在谷雨前后能量变化显著，适合盘点财产和资产配置。",
        "faqs": [
            ("谷雨节气的五行属性是什么？", "谷雨五行属土（辰月），是春季的收尾节气。土能承载万物、藏纳能量，命理上此时适合稳固已有成果，而非开拓新领域。命盘中土系主星（天府、武曲）在谷雨前后运势稳健。"),
            ("谷雨时节财运如何？", "谷雨五行土旺，土能生金，财运方面偏向稳健积累。适合投资房产、固定资产类项目。八字日主为木者（木克土易有财）财运相对活跃；日主为水者（土克水）需防财务损耗。"),
            ("谷雨适合相亲或确定感情关系吗？", "谷雨土气稳健，是感情稳定落地的好时机。传统上此时结婚或订婚被认为象征「扎根稳固」。命盘夫妻宫入「天府」或「武曲」者，在谷雨前后确定感情关系最为吉利。"),
            ("谷雨时节命理上有什么禁忌？", "谷雨土旺克水，命盘中日主为水（壬癸日干）的人需注意财务和健康，防止土重埋水的压抑状态。建议此时保持情绪宣泄渠道畅通，避免积郁。"),
        ],
        "tips": "谷雨是盘点春季成果的时机，适合整理财务、稳固感情、做中期规划。避免急于拓展，以稳为主。",
    },
    {
        "slug": "lixia",
        "name": "立夏",
        "date": "5月5日或6日",
        "wuxing": "火",
        "season": "夏",
        "meaning": "夏季开始，阳气极盛，火气旺盛生发。",
        "mingli": "立夏是火气开始主宰的节气，紫微斗数中太阳星（代表名誉、事业、父亲）能量在此节气最为活跃。官禄宫和迁移宫在立夏前后变动往往与职场晋升或出行相关。",
        "faqs": [
            ("立夏节气对事业运势影响最大的是哪些人？", "立夏五行属火，对命盘中太阳星旺盛者尤为有利——官禄宫有太阳星的人，立夏前后往往有晋升或被赏识的机会。生肖属马、属蛇（火系）在此节气运势最旺。"),
            ("立夏是什么意思？命理上怎么解读？", "立夏标志夏季开始，五行火气当令。在四柱八字中，立夏之后进入「巳月」（纯火之月），八字中喜火者（日主为金、水者）在此节气运势明显上升。"),
            ("立夏时节健康运势需要注意什么？", "火旺克金，肺和大肠属金脏器，立夏前后需注意呼吸道和肠胃健康。心属火，火旺时心气亢进，需注意睡眠和情绪管理。命盘疾厄宫有「廉贞」「太阳」者尤需留意。"),
            ("立夏前后适合做哪些命理事项？", "立夏火旺，适合开展需要热情和曝光的事项——求职面试、公开演讲、签订合同、拓展人脉。命盘太阳化权或化科者，立夏节气是一年中事业最顺的阶段之一。"),
        ],
        "tips": "立夏是事业冲刺的黄金节气，适合主动出击、争取机会。火旺者注意情绪稳定，避免冲动伤人际。",
    },
    {
        "slug": "xiaoman",
        "name": "小满",
        "date": "5月20日或21日",
        "wuxing": "火",
        "season": "夏",
        "meaning": "万物渐满而未盈，火气旺盛，谷物灌浆。",
        "mingli": "小满「满而未溢」，命理上象征事情进入关键阶段但尚未完成，需要坚持。财帛宫在此节气往往有积累信号，但切忌过度乐观而提前挥霍资源。",
        "faqs": [
            ("小满节气在命理上有什么寓意？", "小满是「刚好」的状态——五谷灌浆但未完全成熟。命理上此节气提醒人们坚持现有方向，不可急于求成。命盘财帛宫在此节气能量积累，但「小满」本义提示财运还需再积蓄，不宜过早动用。"),
            ("小满时节投资理财怎么把握？", "小满五行火旺、土气渐生，财运处于积累阶段。适合中长期投资规划，不适合短线操作或高风险投机。日主为木（木生火，助旺财运）者在此节气财富积累速度较快。"),
            ("小满前后感情运势如何？", "小满象征渐丰但未溢，感情上处于「浓而未炽」的状态。此时感情关系最为甜蜜稳固，但过度满足感可能使人忽视对方需求。命盘夫妻宫有「天同」者小满前后感情生活惬意顺心。"),
            ("小满如何用AI命理进行个人运势分析？", "通过问星AI输入出生年月日时，可以查看个人紫微命盘在小满流月的具体运势——包括财帛宫、官禄宫、夫妻宫三个核心宫位的星曜状态和化曜影响，获得个性化的命理建议。"),
        ],
        "tips": "小满时节稳扎稳打效果最佳，适合细化执行已有计划。切忌急功近利，让努力在夏至前充分发酵。",
    },
    {
        "slug": "mangzhong",
        "name": "芒种",
        "date": "6月5日或6日",
        "wuxing": "火",
        "season": "夏",
        "meaning": "麦类有芒作物成熟收割，火气继续旺盛。",
        "mingli": "芒种是「播种与收割」并行的节气，命理上象征双线并进——既要收割春季成果，又要为下半年播种新机遇。命盘事业宫（官禄宫）在此节气最为活跃。",
        "faqs": [
            ("芒种节气对哪些方面的运势影响最大？", "芒种「收」「种」并行，命理上对官禄宫（事业）和田宅宫（资产）影响最大。此时适合一边整合已有成果，一边布局下半年的新项目。生肖属马者在芒种前后事业机遇最多。"),
            ("芒种时节换工作或创业好吗？", "芒种火气旺盛，行动力强，是转职或创业的活跃节气。但需结合个人八字和流年大运——命盘官禄宫逢生年化禄者，芒种创业吉；逢流年化忌冲命宫者则宜谨慎。"),
            ("芒种前后感情方面要注意什么？", "芒种火旺，情绪容易急躁。感情方面容易因为工作繁忙而疏忽伴侣，或因沟通不当产生争执。建议在此节气主动为感情创造仪式感，避免让事业压力侵蚀感情质量。"),
            ("怎么用紫微斗数判断芒种期间是否适合换工作？", "在问星AI中可以查看流年官禄宫的化曜状态：若流年天干化权落官禄宫，则芒种时期换工作大吉；若化忌入官禄宫，则建议等到下一个流年才行动。"),
        ],
        "tips": "芒种是上半年最后一个全力冲刺的节气，适合完成项目收尾、谈定合作。为夏至后的调整期留好余力。",
    },
    {
        "slug": "xiazhi",
        "name": "夏至",
        "date": "6月21日",
        "wuxing": "火",
        "season": "夏",
        "meaning": "白昼最长，阳气至极，火气达到顶峰后开始转阴。",
        "mingli": "夏至阳气至极，命理上是「物极必反」的转折节点。命盘中太阳星在夏至能量达到顶点，此后开始向阴柔过渡。大运处于「日月交辉」格局的人，夏至前后往往有重大人生转折。",
        "faqs": [
            ("夏至阳极转阴，对运势意味着什么？", "夏至阳气达到顶点后开始向阴转换，命理上象征「盛极而衰、否极泰来」的转机。对于上半年运势不顺的人来说，夏至是下半年运势开始积累的起点；对于上半年顺风顺水者，夏至提示需要开始蓄势而非继续激进扩张。"),
            ("夏至是一年中最特殊的命理节点吗？", "夏至与冬至并列为一年中阴阳转换最强烈的两个节点。在紫微斗数中，「太阳」星在夏至能量最强，而后逐渐转弱。夏至出生的人命盘往往带有「极」性——极旺或极弱，鲜少平衡。"),
            ("夏至时节哪些八字日主的人运势最旺？", "夏至火极旺，对八字日主为「丙丁」（火）的人能量最盛，但也最需注意「过旺无用」——火过旺克金，财官反而受损。日主为「庚辛金」者在夏至时期反而容易受到外部挑战，需低调应对。"),
            ("夏至适合做什么重要决策？", "夏至是一年的中转点，适合做下半年规划、评估上半年目标完成情况，以及做人事关系的整合。命盘入「七杀」或「破军」者，夏至前后往往有破旧立新的冲动，顺势而为效果最佳。"),
        ],
        "tips": "夏至是全年运势的高点或转折点，宜总结上半年、规划下半年。阳气转阴后蓄力为主，减少对外扩张。",
    },
    {
        "slug": "xiaoshu",
        "name": "小暑",
        "date": "7月6日或7日",
        "wuxing": "火",
        "season": "夏",
        "meaning": "暑热开始，火气仍旺但阴气渐增。",
        "mingli": "小暑火旺而湿热交织，命理上「热而不定」，容易出现情绪化决策。命盘中「廉贞」星（代表激情与争端）在此节气能量突出，需注意人际冲突。",
        "faqs": [
            ("小暑节气运势有什么特点？", "小暑五行火旺夹湿土，能量躁动不安。命理上此节气容易出现突发事件和情绪化行为。建议此时放慢决策节奏，避免在暑热中做出后悔的选择。命盘廉贞化忌者小暑前后最需谨慎。"),
            ("小暑时期感情容易出什么问题？", "小暑暑气逼人，容易烦躁，夫妻宫或感情宫位在此节气摩擦增多。特别是命盘廉贞星落夫妻宫者，小暑前后需主动营造轻松氛围，避免因琐事争执影响感情基础。"),
            ("小暑健康方面命理上需要注意什么？", "小暑湿热并重，脾胃属土，火旺克金伤肺。命盘疾厄宫有「廉贞」「太阳」者需注意心血管和消化系统。此节气宜清淡饮食、避免熬夜，保持情绪平和。"),
            ("小暑时候如何通过命理化解不利运势？", "命盘流年出现化忌冲克者，可在小暑前后通过调整工作节奏、减少不必要的争论来化解煞气。问星AI可分析个人流年化忌落宫位置，提供针对性的化解建议。"),
        ],
        "tips": "小暑宜静心修整，避免冲动决策和情绪化争执。保持规律作息，利用暑期整合资源、低调蓄力。",
    },
    {
        "slug": "dashu",
        "name": "大暑",
        "date": "7月22日或23日",
        "wuxing": "火土",
        "season": "夏",
        "meaning": "一年中最热时节，火气极盛，土气同旺。",
        "mingli": "大暑是全年火气最盛的节气，命理上「过热则燥」，容易出现极端情况。命盘太阳化禄者在此节气荣耀达顶；命盘有大量火土堆积者，则需防「燥土无用」导致财务混乱。",
        "faqs": [
            ("大暑是全年运势最旺的节气吗？", "大暑虽然火气最盛，但并非所有人运势最旺——火旺对八字喜火者（日主为金、水）确实有利，但对日主本已属火者则过旺反凶。运势最旺的是命盘中太阳化禄或禄存在官禄宫的人。"),
            ("大暑节气财运如何？", "大暑火旺生土，土为财库，但过热的土易干燥无用。财运方面，适合整合已有资源，不宜新增大额投资。命盘财帛宫入「武曲」（正财星）者大暑前后财务稳健；入「贪狼」者则有偏财机遇。"),
            ("大暑时节感情和婚姻如何？", "大暑极热，感情上容易爆发积压的矛盾，也可能在极热中产生强烈的吸引力。这是个两极化的节气——感情要么热烈升华，要么彻底爆发。命盘夫妻宫有「天同」者相对稳定；有「廉贞七杀」者需特别注意。"),
            ("大暑适合出行吗？从命理角度如何看待？", "大暑炎热，传统民俗不主张长途出行。命理上迁移宫在此节气受火旺影响，出行易有变动。如命盘流年迁移宫有化忌，大暑前后出行需更加谨慎，提前做好应急准备。"),
        ],
        "tips": "大暑是全年能量最极端的节气，宜稳守为主。感情和财务都避免极端行动，以平和心态等待暑热过后的清凉转机。",
    },
    {
        "slug": "liqiu",
        "name": "立秋",
        "date": "8月7日或8日",
        "wuxing": "金",
        "season": "秋",
        "meaning": "秋季开始，金气初生，肃杀之气渐起。",
        "mingli": "立秋标志金气开始主宰，紫微斗数中武曲（正财星）和七杀（行动星）能量上升。命盘官禄宫和财帛宫在立秋前后最易有重大变动，秋季是一年中事业财务行动力最强的时段。",
        "faqs": [
            ("立秋节气在命理上标志着什么？", "立秋是秋季第一个节气，五行金气开始主导。命理上金主「收」「刚」「决断」，此时是全年做重大财务决策和事业布局的最佳窗口期之一。命盘武曲星旺盛者，立秋前后往往有重要的财务机遇。"),
            ("立秋时节哪些生肖运势转好？", "立秋金气上升，生肖猴、鸡（庚辛金）在此节气最得天时；金克木，生肖虎、兔（寅卯木）需注意事业压力。金生水，生肖猪、鼠的财运在此节气开始积累。"),
            ("立秋是否适合换工作或谈判加薪？", "立秋金气旺，武曲星（财与事业之星）能量强。适合进行薪资谈判、签订合同、推进商业合作。命盘官禄宫逢流年化权者，立秋是争取晋升的最佳时机。"),
            ("立秋后下半年运势如何用紫微斗数判断？", "在问星AI中输入生辰八字，可以查看下半年各流月的宫位运势变化。立秋之后进入申月（金月），是秋季行动力最强的起点，也是判断全年大运节奏的关键参考点。"),
        ],
        "tips": "立秋是下半年行动的起跑线，适合主动争取晋升、推进谈判、整合财务资源。金气刚锐，果断行动效果最佳。",
    },
    {
        "slug": "chushu",
        "name": "处暑",
        "date": "8月22日或23日",
        "wuxing": "金",
        "season": "秋",
        "meaning": "暑气消退，秋凉渐来，金气稳健。",
        "mingli": "处暑「出暑」，代表暑热退去，金气稳定发挥。命理上是整合资源、落实计划的最佳节气。命盘田宅宫（房产资产）在处暑前后最易有稳健的进展。",
        "faqs": [
            ("处暑节气的命理特点是什么？", "处暑金气平稳，是全年最适合「落地执行」的节气之一。命理上此时不适合激进扩张，而是将立秋的冲劲转化为踏实的行动。命盘天府星（稳健财库）入旺宫者，处暑前后资产积累效果最佳。"),
            ("处暑时节财运怎么样？", "处暑金气稳健，偏向「正财」稳定积累，不利偏财投机。适合储蓄、购置固定资产、落实已谈好的合作。命盘财帛宫有「武曲」「天府」者在处暑前后财运扎实；有「贪狼」者偏财运相对较弱。"),
            ("处暑前后感情和婚姻运势如何？", "处暑气候宜人，感情趋于平稳。对于在暑期经历波折的感情，处暑是修复关系的好时机。命盘夫妻宫有「天同」或「太阴」者，处暑前后感情和谐，适合讨论婚恋大事。"),
            ("处暑节气适合整理命盘哪些方面？", "处暑是盘点立秋以来行动成果的节点。建议此时通过问星AI复盘个人财帛宫和官禄宫的流月状态，了解当前阶段的财运和事业节奏，为秋季后半段的行动调整策略。"),
        ],
        "tips": "处暑是执行落地的黄金时段，立秋种下的计划在此节气最能生根。感情以稳定修复为主，避免无谓折腾。",
    },
    {
        "slug": "bailu",
        "name": "白露",
        "date": "9月7日或8日",
        "wuxing": "金",
        "season": "秋",
        "meaning": "露水出现，金气充沛，阴气渐盛。",
        "mingli": "白露金气充沛、阴气渐长，命理上代表思虑趋于清晰、洞察力增强。命盘中天机星（思维与分析）和太阴星（直觉与阴柔智慧）在白露前后能量双旺，适合学习深造和战略规划。",
        "faqs": [
            ("白露节气在命理上有什么特殊意义？", "白露是秋季金气最纯粹的节气，象征清晰与洞察。命理上此时人的判断力和洞察力最强，适合做深度分析和战略规划。命盘天机星旺盛者，白露前后学习效率极高，考试运也相当不错。"),
            ("白露时节感情运有什么特点？", "白露阴气渐长，太阴星能量上升，感情上更加细腻敏感。此时情感需求增加，容易因为细节而心生波动。命盘夫妻宫有太阴星者白露前后感情最为浓郁，也最脆弱。需要伴侣更多的陪伴和细心关怀。"),
            ("白露节气适合做哪些投资理财决策？", "白露金气旺盛，思虑清晰，是评估投资组合的最佳时机。但此时阴气渐强，市场可能出现回调。适合减持高风险资产、增加稳健配置。命盘财帛宫逢白露流月化权者，可适当进行资产调配。"),
            ("白露前后如何利用命理调整工作状态？", "白露金气清肃，思路清晰，是整理工作思路的好时机。可通过问星AI查询官禄宫白露流月状态，了解哪些工作方向值得加大投入，哪些项目需要适时退出。"),
        ],
        "tips": "白露是思考与规划的最佳节气，适合学习进修、战略调整、整理财务结构。感情细心经营，避免因敏感引发误会。",
    },
    {
        "slug": "qiufen",
        "name": "秋分",
        "date": "9月22日或23日",
        "wuxing": "金",
        "season": "秋",
        "meaning": "昼夜再次等长，金气至盛，阴阳平衡转为阴长阳消。",
        "mingli": "秋分是秋季的中轴，金气达到顶峰。命理上此时财运和事业运都处于年内的高峰期之一，命盘武曲化禄、天府化科者在秋分前后往往有重大财务收获或事业突破。",
        "faqs": [
            ("秋分是收获的节气，命理上如何解读？", "秋分金气至盛，是全年财运和事业运的重要高峰节点。在紫微斗数中，秋分对应的流月宫位若有武曲（财星）或天府（库星）入驻，则此时正是谈判签约、收取财务回报的最佳时机。"),
            ("秋分时节哪些命盘格局最受益？", "秋分受益最大的是命盘有「金局」（申酉戌三合金局）特征的人——日主为木者在此节气财运丰厚，日主为金者则能量至旺；生肖猴、鸡人在秋分前后综合运势最佳。"),
            ("秋分感情运势怎么样？", "秋分阴阳平衡，感情运处于全年较好的状态。此时感情中的矛盾容易化解，适合推进婚恋大事。命盘夫妻宫有「天相」星者秋分前后感情最为顺遂，适合此时确定关系或求婚。"),
            ("秋分之后运势会下滑吗？如何提前布局？", "秋分之后金气开始向水过渡，事业和财运的高峰期逐渐过去。建议在秋分前后完成最重要的财务决策和事业谈判，秋分之后转入收尾和积累阶段。通过问星AI可以具体查看个人流月趋势。"),
        ],
        "tips": "秋分是全年财运和事业运的顶点之一，把握好这个窗口期完成重要谈判和决策，将一年的努力转化为实际收益。",
    },
    {
        "slug": "hanlu",
        "name": "寒露",
        "date": "10月7日或8日",
        "wuxing": "金水",
        "season": "秋",
        "meaning": "露水变冷，金气收敛，水气初现。",
        "mingli": "寒露金水交接，命理上象征智慧与财富双向流动。命盘中天机（智慧）与武曲（财富）同宫或对宫者，寒露前后往往有结合头脑与资源的绝佳机遇。",
        "faqs": [
            ("寒露节气命理特点是什么？", "寒露金气收敛、水气初生，五行能量从阳刚转向阴柔智慧。命理上此时适合内省和学习，减少对外冒进。命盘天机化科者寒露前后考试和学习运极佳；天机化忌者则需防信息误判。"),
            ("寒露时节财运怎么看？", "寒露金水相生，财运从「收获」转为「流通」。适合将秋季的财务成果转化为新的投资方向，偏向金融类、知识类资产。命盘财帛宫有「贪狼」（偏财）者寒露前后偶有意外之财。"),
            ("寒露节气对健康运势有什么影响？", "寒露气温骤降，肺属金、肾属水，此节气需重点关注呼吸系统和泌尿系统健康。命盘疾厄宫有「太阴」或「天同」星者，寒露前后免疫力相对下降，需加强保暖和休息。"),
            ("寒露前后适合进行哪些命理事项？", "寒露适合学习进修、梳理人脉、整理过去一年的命理运势轨迹。通过问星AI可以在寒露时节系统回顾个人流年运势，为明年的大运规划做准备。"),
        ],
        "tips": "寒露是从行动模式转入思考模式的时机，适合学习深造、梳理人脉、规划来年。健康方面注意防寒保暖。",
    },
    {
        "slug": "shuangjiang",
        "name": "霜降",
        "date": "10月23日",
        "wuxing": "土",
        "season": "秋",
        "meaning": "霜冻出现，土气收敛，秋季进入尾声。",
        "mingli": "霜降是秋季最后一个节气，土气收敛，万物归藏。命理上此时是「盖棺定论」的节点——全年运势格局基本确定，命盘中田宅宫（家庭与资产）的状态在此节气最能真实体现。",
        "faqs": [
            ("霜降节气运势有什么特点？", "霜降土气收敛，能量向内积聚。命理上此时是总结全年、做资产盘点的好时机。对于命盘土系主星（天府、武曲）旺盛者，霜降前后往往有资产固化或房产相关的重要进展。"),
            ("霜降时节感情和婚姻运势如何？", "霜降土气稳定，感情趋向踏实落地。是谈婚论嫁的好节气，双方关系在此时容易达成共识。命盘夫妻宫有「天府」或「武曲」者，霜降前后感情关系最为稳固，适合确定终身大事。"),
            ("霜降时期对命理中的「煞星」有什么影响？", "霜降土旺，能一定程度克制水系煞星。对于命盘有「陀罗」「擎羊」等六煞星落在水系宫位者，霜降前后这些煞星影响相对减弱。但土系煞星（陀罗在土宫）反而能量增强，需注意拖延和阻碍。"),
            ("霜降如何为来年做命理规划？", "霜降是回顾全年的最佳时机。建议通过问星AI输入生辰，系统回顾当年各流月的宫位运势，总结哪些宫位影响了关键事件，为来年的流年大运规划提供参考依据。"),
        ],
        "tips": "霜降是全年收尾的节气，宜盘点资产、稳固感情、梳理年度得失。为来年立下清晰目标，秋收之后蓄势待发。",
    },
    {
        "slug": "lidong",
        "name": "立冬",
        "date": "11月7日或8日",
        "wuxing": "水",
        "season": "冬",
        "meaning": "冬季开始，水气当令，万物收藏。",
        "mingli": "立冬水气开始主宰，紫微斗数中天同星（代表福德与享受）和太阴星（代表阴柔智慧）能量上升。命盘福德宫在立冬前后最能体现精神层面的满足感，适合内修与积累。",
        "faqs": [
            ("立冬节气在命理上意味着什么？", "立冬标志一年进入收藏阶段，五行水气开始主导。命理上此时适合「蓄」而非「动」，积累资源和能量为来年春季萌发做准备。命盘天同化禄者立冬前后生活质量提升，精神满足感强。"),
            ("立冬时节什么事情不适合做？", "立冬水气收藏，命理上不适合开展高风险的扩张行动、大额投资或感情上的剧烈变化。此时行事求稳，顺应「收」的节气能量，将精力用于积累和学习。"),
            ("立冬时节哪些生肖运势最旺？", "立冬水气当令，生肖猪、鼠（亥子水）在此节气最得天时；水生木，生肖虎、兔的运势也开始积累。属火的生肖（马、蛇）在立冬后需注意能量消耗，适当休养。"),
            ("立冬适合做年终命理总结吗？", "立冬是年终命理复盘的绝佳时机。通过问星AI可以回顾全年各流月的命盘运势变化，总结今年大运、流年与流月的实际应验情况，为来年制定更精准的命理规划策略。"),
        ],
        "tips": "立冬是养精蓄锐的开始，适合内修、学习、规划来年。减少不必要的外部争斗，把能量留给冬季的深度积累。",
    },
    {
        "slug": "xiaoxue",
        "name": "小雪",
        "date": "11月22日",
        "wuxing": "水",
        "season": "冬",
        "meaning": "开始降雪，水气增强，阴气更盛。",
        "mingli": "小雪水气增强，阴气深化，命理上象征「内敛」和「潜藏」。命盘中太阴星（阴柔智慧）在此节气能量最为深沉，对于需要依靠直觉和洞察力的决策尤为有利。",
        "faqs": [
            ("小雪节气的命理特点是什么？", "小雪水气渐旺，阴气增强，命理上进入一年中最「静」的阶段。此时适合深度思考和战略规划，而非激进行动。命盘太阴化科者小雪前后直觉力极强，适合从事研究、分析类工作。"),
            ("小雪时节感情运势如何？", "小雪水气深沉，感情上偏向细腻内敛。此时双方之间的心理距离变得重要，需要更深层的情感连接而非表面的热情。命盘夫妻宫有「太阴」者小雪前后感情最为深刻，适合深度沟通和心灵连接。"),
            ("小雪节气财运方面有什么特点？", "小雪水旺，水为财之载体，但水过旺则「财难聚」。此时适合整理财务结构，减少不必要的开支，将资金集中在稳健的渠道中。命盘财帛宫有「天府」（财库）者在小雪前后保存财富效果最好。"),
            ("小雪前后命理上适合做什么规划？", "小雪是一年中最适合进行来年命理规划的节点之一。通过问星AI输入生辰八字，可以生成来年流年命盘预览，提前了解来年的大运流年走势，制定相应的行动策略。"),
        ],
        "tips": "小雪是深度规划的绝佳时机，适合梳理来年目标、整理财务、深化感情连接。静心蓄力，等待明年春季的萌发。",
    },
    {
        "slug": "daxue",
        "name": "大雪",
        "date": "12月7日",
        "wuxing": "水",
        "season": "冬",
        "meaning": "降雪增多，水气充盛，阴气至深。",
        "mingli": "大雪水气充盛，是一年中阴气最深的节气之一（冬至之前）。命理上此时能量向内收藏，命盘福德宫（精神层面）和疾厄宫（健康）需要特别关注，以保持身心平衡度过深冬。",
        "faqs": [
            ("大雪节气对运势有什么影响？", "大雪水气充盛，能量深藏，命理上是一年中最需要「守」的节点。对于命盘喜水者（日主为火者），大雪前后反而有意想不到的福气；对于日主为土者则需注意土被水克，事业容易出现阻滞。"),
            ("大雪时节财运怎么把握？", "大雪水盛，流动性强但聚财难。适合将年底的财务收益安全入账，减少新的投入。命盘财帛宫入流年化忌者，大雪前后需格外防止财务漏洞，检查合同和账目。"),
            ("大雪节气感情运势如何？", "大雪深冬，感情需要温度。此时最适合陪伴与共处，感情中的「陪伴感」比「激情感」更为重要。命盘夫妻宫有「天同」者大雪前后享受安稳的家庭温暖；有「七杀破军」者需防感情中的孤独感。"),
            ("大雪节气如何用命理调整身体状态？", "大雪水气旺盛，肾属水，肾气在此节气最为活跃也最需保护。命盘疾厄宫有「天同」（水系）者需注意泌尿系统。建议此时早睡晚起，保护肾气，通过问星AI查看个人疾厄宫的当前流月状态。"),
        ],
        "tips": "大雪是深冬蓄养的时机，注重休息和健康，整理年终财务，珍惜家庭陪伴时光。减少外出和消耗，留足能量迎接冬至后的阳气回升。",
    },
    {
        "slug": "dongzhi",
        "name": "冬至",
        "date": "12月21日或22日",
        "wuxing": "水",
        "season": "冬",
        "meaning": "白昼最短，阴气至极，一阳始生。",
        "mingli": "冬至是「阴极阳生」的最重要节点，也是紫微斗数中计算「阴阳历转换」的关键。命理上此时是全年能量最低点，也是新一轮生发的起点。大运在冬至前后更替者，往往会经历深刻的人生转折。",
        "faqs": [
            ("冬至为什么被视为命理中最重要的节气之一？", "冬至是阴阳转换的极点，一阳始生。在紫微斗数中，冬至是推算「起运年龄」的重要参照；在八字命理中，冬至子月是天干地支循环的核心节点。许多命理师认为冬至是全年最适合启动命理咨询、重新规划人生的时间节点。"),
            ("冬至这天出生的人命盘有什么特点？", "冬至生人命盘往往带有「极」性——至阴之时阳气初生，意味着人生常经历从谷底反弹的历程。命盘太阳星（阳）虽在冬至能量最弱，但「一阳初生」象征强烈的生命力和逆势成长的能力。"),
            ("冬至适合做哪些命理事项？", "冬至一阳初生，是许多命理传统中「许愿」「设定目标」的神圣时刻。此时适合进行来年命理规划、确定人生方向，以及通过问星AI全面分析来年流年命盘，制定12个月的具体行动计划。"),
            ("冬至运势最差怎么办？有什么命理化解方法？", "冬至阴气至极，命盘中若此时正值「流年化忌冲命宫」，则此冬至前后运势确实偏弱。命理上化解方法：一是收敛行事，避免大动作；二是强化「用神」五行，如命盘用神为火者可佩戴红色饰品增加阳气；三是通过问星AI获取针对个人命盘的详细化解建议。"),
        ],
        "tips": "冬至是全年最重要的节气转折点。在此立下来年目标，规划12个月的命理运势走向，让一阳初生的能量为来年的每一步提供指引。",
    },
    {
        "slug": "xiaohan",
        "name": "小寒",
        "date": "1月5日或6日",
        "wuxing": "水",
        "season": "冬",
        "meaning": "寒冷加剧，水气极盛，阳气缓缓萌动。",
        "mingli": "小寒是一年中最寒冷的节气之一，水气极盛。命理上此时肾气（水系）能量达到顶峰，适合「藏精」——储备能量和资源为来年生发做准备。命盘天同、太阴旺盛者在小寒前后精神状态最为内敛深沉。",
        "faqs": [
            ("小寒节气命理上有什么特别之处？", "小寒与大寒是全年水气最旺的两个节气，也是阴气最盛的时段。命理上此时适合「蓄势」，将全年积累的能量凝聚为来年行动的燃料。命盘日主为木者（水生木）在此节气悄悄积累了大量向上生长的潜能。"),
            ("小寒时节事业和财运方面怎么布局？", "小寒不适合激进行动，而是规划和准备的时机。此时适合学习新技能、建立人脉网络、研究市场机会。命盘官禄宫有「天机」者在小寒前后思路清晰，战略规划能力最强。"),
            ("小寒前后健康方面需要注意什么？", "小寒最寒冷，肾属水是此时最需要保护的脏器。命盘疾厄宫有「廉贞」（火系）者需注意心血管在低温下的应激反应；有「太阴」者需注意泌尿系统和生殖系统的寒气侵入。"),
            ("小寒是否适合算命咨询或规划来年命盘？", "小寒是一年中最适合进行系统命理规划的时节——阳气初动、思路清晰，恰好在来年立春（新年起点）之前。通过问星AI在小寒前后进行全年命理分析，可以为来年的紫微斗数流年运势做出最完整的规划。"),
        ],
        "tips": "小寒是来年规划的最佳时机，在春季到来前完成所有战略思考和资源准备。蓄好能量，立春一到即可全力出发。",
    },
    {
        "slug": "dahan",
        "name": "大寒",
        "date": "1月20日",
        "wuxing": "水土",
        "season": "冬",
        "meaning": "一年中最寒冷时节，水气极盛转而交接丑土。",
        "mingli": "大寒是旧年的最后一个节气，水气最盛后开始向下一个轮回交接。命理上是「旧年归档、新年预备」的时刻，命盘中所有「未了事宜」在大寒前后都会有最终的答案和了结。",
        "faqs": [
            ("大寒是一年命理循环的终点吗？", "大寒是农历年的最后一个节气，也是命理循环即将完成的时刻。命盘中流年最后的流月（大寒前后）往往会呈现全年运势的终结信号——悬而未决的事情在此时得到结果，无论好坏。"),
            ("大寒时节如何做年终命理盘点？", "大寒适合系统回顾全年命盘运势：哪些宫位（财帛、官禄、夫妻）带来了重大影响？哪些化曜（化禄、化权、化科、化忌）应验了预测？通过问星AI可以生成全年流月命盘报告，逐月复盘。"),
            ("大寒出生的人命盘有什么特点？", "大寒生人处于水土交接之际，命盘往往兼具水（智慧、流动）和土（稳重、务实）的特质。性格上既有深沉的思考力，又有落地的执行力。但两种能量的平衡需要后天用心培养。"),
            ("大寒之后就是立春，如何做好新旧年命理交接？", "大寒到立春是命理「年柱更替」的关键窗口。此时通过问星AI完成当年流年复盘和新年流年预测，可以精准把握八字年柱交替带来的运势变化，为立春后的全力冲刺做好最完整的准备。"),
        ],
        "tips": "大寒是做年终总结和来年规划的最后时机。完成旧年所有事项的收尾，在立春前清空负担，以最轻盈的状态迎接新一年的命理循环。",
    },
]


def make_page(jq):
    slug = jq["slug"]
    name = jq["name"]
    date = jq["date"]
    wuxing = jq["wuxing"]
    meaning = jq["meaning"]
    mingli = jq["mingli"]
    tips = jq["tips"]
    faqs = jq["faqs"]

    faq_items_html = ""
    for q, a in faqs:
        faq_items_html += f"""
      <details class="faq-item">
        <summary class="faq-q">{q}</summary>
        <p class="faq-a answer">{a}</p>
      </details>"""

    faq_schema_items = []
    for q, a in faqs:
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"https://wenxingai.top/24jieqi/{slug}.html",
                "url": f"https://wenxingai.top/24jieqi/{slug}.html",
                "name": f"{name}命理运势 | 二十四节气玄学解读 - 问星AI",
                "description": f"{name}（{date}）五行{wuxing}，{meaning}本文从紫微斗数与八字命理角度解读{name}节气对运势的影响，并提供个性化AI命盘分析。",
                "inLanguage": "zh-CN",
                "isPartOf": {"@id": "https://wenxingai.top/#website"},
                "breadcrumb": {"@id": f"https://wenxingai.top/24jieqi/{slug}.html#breadcrumb"}
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"https://wenxingai.top/24jieqi/{slug}.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "问星AI首页", "item": "https://wenxingai.top/"},
                    {"@type": "ListItem", "position": 2, "name": "二十四节气命理", "item": "https://wenxingai.top/24jieqi/"},
                    {"@type": "ListItem", "position": 3, "name": f"{name}命理运势", "item": f"https://wenxingai.top/24jieqi/{slug}.html"}
                ]
            },
            {
                "@type": "Article",
                "@id": f"https://wenxingai.top/24jieqi/{slug}.html#article",
                "headline": f"{name}命理运势完全解析：五行{wuxing}、紫微斗数与八字影响",
                "description": f"{name}节气（{date}）五行{wuxing}，{mingli[:60]}",
                "url": f"https://wenxingai.top/24jieqi/{slug}.html",
                "datePublished": "2026-05-07T00:00:00+08:00",
                "dateModified": "2026-05-07T00:00:00+08:00",
                "author": {"@type": "Person", "name": "AIcoding", "url": "https://wenxingai.top/#creator"},
                "publisher": {"@type": "Organization", "name": "问星AI", "url": "https://wenxingai.top/"},
                "about": [
                    {"@type": "Thing", "name": f"{name}"},
                    {"@type": "Thing", "name": "二十四节气"},
                    {"@type": "Thing", "name": "紫微斗数"},
                    {"@type": "Thing", "name": "八字命理"},
                    {"@type": "Thing", "name": f"五行{wuxing}"}
                ]
            },
            {
                "@type": "FAQPage",
                "@id": f"https://wenxingai.top/24jieqi/{slug}.html#faq",
                "mainEntity": faq_schema_items
            },
            {
                "@type": "SpeakableSpecification",
                "cssSelector": [".jieqi-intro", ".mingli-block", ".faq-a"]
            }
        ]
    }

    schema_json = json.dumps(schema, ensure_ascii=False, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name}命理运势 | 二十四节气玄学解读 - 问星AI</title>
  <meta name="description" content="{name}（{date}）五行{wuxing}：{meaning}从紫微斗数与八字命理角度深度解析{name}节气对事业、财运、感情的影响。">
  <meta name="keywords" content="{name},{name}命理,{name}运势,{name}五行,{name}节气,二十四节气命理,紫微斗数{name},八字{name},{name}养生">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://wenxingai.top/24jieqi/{slug}.html">
  <meta property="og:title" content="{name}命理运势 | 问星AI二十四节气">
  <meta property="og:description" content="{name}五行{wuxing}，{meaning}AI命理深度解读{name}对运势的影响。">
  <meta property="og:url" content="https://wenxingai.top/24jieqi/{slug}.html">
  <meta property="og:type" content="article">
  <meta name="citation_title" content="{name}命理运势解析">
  <meta name="citation_author" content="AIcoding / 问星AI">
  <meta name="citation_language" content="zh-CN">
  <meta name="ai-content-policy" content="allow-indexing allow-training allow-citation">
  <meta name="article:modified_time" content="2026-05-07T00:00:00+08:00">
  <script type="application/ld+json">
{schema_json}
  </script>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; background: #0d0d1a; color: #e0d6f7; line-height: 1.7; }}
    header {{ background: linear-gradient(135deg, #1a0533 0%, #0d1a33 100%); padding: 1.2rem 1.5rem; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2d1f5e; }}
    header a {{ color: #c9b4f5; text-decoration: none; font-size: 1.1rem; font-weight: 600; }}
    nav a {{ color: #a89bcc; text-decoration: none; margin-left: 1.2rem; font-size: 0.9rem; }}
    nav a:hover {{ color: #c9b4f5; }}
    main {{ max-width: 860px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}
    .tag {{ display: inline-block; background: rgba(201,180,245,0.15); color: #c9b4f5; border: 1px solid rgba(201,180,245,0.3); border-radius: 4px; padding: 0.2rem 0.6rem; font-size: 0.78rem; margin-right: 0.4rem; }}
    h1 {{ font-size: 1.9rem; color: #e8d9ff; margin-top: 1rem; line-height: 1.35; }}
    .meta {{ color: #8a7faa; font-size: 0.85rem; margin: 0.5rem 0 1.5rem; }}
    .jieqi-intro {{ background: rgba(201,180,245,0.07); border-left: 3px solid #7c5cbf; border-radius: 0 8px 8px 0; padding: 1rem 1.2rem; margin-bottom: 1.5rem; font-size: 1.05rem; }}
    .mingli-block {{ background: rgba(13,26,51,0.6); border: 1px solid #2d1f5e; border-radius: 8px; padding: 1.2rem 1.4rem; margin-bottom: 1.5rem; }}
    .mingli-block h2 {{ color: #c9b4f5; font-size: 1.1rem; margin-top: 0; }}
    h2.section-title {{ font-size: 1.2rem; color: #c9b4f5; border-bottom: 1px solid #2d1f5e; padding-bottom: 0.5rem; margin-top: 2rem; }}
    .faq-item {{ border: 1px solid #2d1f5e; border-radius: 8px; margin-bottom: 0.8rem; overflow: hidden; }}
    .faq-q {{ padding: 0.9rem 1.2rem; cursor: pointer; font-weight: 600; color: #d4c2f5; list-style: none; background: rgba(45,31,94,0.3); }}
    .faq-q:hover {{ background: rgba(45,31,94,0.6); }}
    .faq-a {{ padding: 1rem 1.2rem; margin: 0; border-top: 1px solid #2d1f5e; color: #c8bde8; }}
    .tips-box {{ background: rgba(124,92,191,0.12); border: 1px solid rgba(124,92,191,0.4); border-radius: 8px; padding: 1rem 1.3rem; margin: 1.5rem 0; }}
    .tips-box strong {{ color: #c9b4f5; }}
    .cta-block {{ text-align: center; background: linear-gradient(135deg, rgba(124,92,191,0.2), rgba(13,26,51,0.5)); border: 1px solid #4a3480; border-radius: 12px; padding: 2rem; margin: 2rem 0; }}
    .cta-block h2 {{ color: #e8d9ff; }}
    .cta-btn {{ display: inline-block; background: linear-gradient(135deg, #7c5cbf, #4a3480); color: #fff; text-decoration: none; padding: 0.8rem 2rem; border-radius: 8px; font-weight: 700; font-size: 1rem; margin-top: 0.8rem; }}
    .cta-btn:hover {{ opacity: 0.9; }}
    .breadcrumb {{ font-size: 0.82rem; color: #7a6fa0; margin-bottom: 1rem; }}
    .breadcrumb a {{ color: #9a8ec0; text-decoration: none; }}
    .breadcrumb a:hover {{ color: #c9b4f5; }}
    footer {{ text-align: center; color: #5a5070; font-size: 0.82rem; padding: 2rem; border-top: 1px solid #1e1640; }}
    footer a {{ color: #7a6fa0; text-decoration: none; }}
  </style>
</head>
<body>
  <header>
    <a href="https://wenxingai.top/">✦ 问星AI</a>
    <nav>
      <a href="https://wenxingai.top/24jieqi/">二十四节气</a>
      <a href="https://wenxingai.top/glossary.html">命理词典</a>
      <a href="https://wenxingai.top/geo-answers.html">常见问题</a>
    </nav>
  </header>

  <main>
    <nav class="breadcrumb" aria-label="面包屑导航">
      <a href="https://wenxingai.top/">首页</a> &rsaquo;
      <a href="https://wenxingai.top/24jieqi/">二十四节气命理</a> &rsaquo;
      {name}命理运势
    </nav>

    <span class="tag">节气命理</span>
    <span class="tag">五行{wuxing}</span>
    <span class="tag">紫微斗数</span>
    <h1>{name}命理运势完全解析</h1>
    <p class="meta">节气时间：{date} &nbsp;|&nbsp; 五行属性：{wuxing} &nbsp;|&nbsp; 作者：AIcoding / 问星AI &nbsp;|&nbsp; 更新：2026年5月</p>

    <p class="jieqi-intro">{meaning}</p>

    <div class="mingli-block">
      <h2>命理解读</h2>
      <p>{mingli}</p>
    </div>

    <h2 class="section-title">常见问题解答</h2>
    {faq_items_html}

    <div class="tips-box">
      <strong>节气行动指南：</strong> {tips}
    </div>

    <div class="cta-block">
      <h2>查询你的{name}个人运势</h2>
      <p>输入生辰八字，通过问星AI生成专属紫微命盘，查看{name}流月的财运、感情、事业走势。</p>
      <a class="cta-btn" href="https://wenxingai.top/" rel="noopener">免费生成命盘 →</a>
    </div>

    <p style="color:#6a6090;font-size:0.85rem">相关页面：
      <a href="https://wenxingai.top/glossary.html" style="color:#9a8ec0">命理词典</a> ·
      <a href="https://wenxingai.top/geo-answers.html" style="color:#9a8ec0">AI命理常见问题</a> ·
      <a href="https://wenxingai.top/mingli-xuanxue-news.html" style="color:#9a8ec0">玄学热点资讯</a>
    </p>
  </main>

  <footer>
    <p>&copy; 2026 问星AI (wenxingai.top) &nbsp;|&nbsp;
      <a href="https://wenxingai.top/">首页</a> &nbsp;|&nbsp;
      <a href="https://wenxingai.top/24jieqi/">二十四节气</a> &nbsp;|&nbsp;
      <a href="https://wenxingai.top/glossary.html">命理词典</a>
    </p>
    <p style="font-size:0.75rem;color:#3d3560">本站内容仅供文化参考与娱乐，不构成任何决策建议。</p>
  </footer>
</body>
</html>"""
    return html


def make_index():
    items_html = ""
    for jq in JIEQI:
        items_html += f"""    <li><a href="{jq['slug']}.html">{jq['name']}</a> — {jq['date']}，五行{jq['wuxing']}，{jq['meaning'][:28]}…</li>\n"""

    item_list_schema = []
    for i, jq in enumerate(JIEQI, 1):
        item_list_schema.append({
            "@type": "ListItem",
            "position": i,
            "name": f"{jq['name']}命理运势",
            "url": f"https://wenxingai.top/24jieqi/{jq['slug']}.html"
        })

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": "https://wenxingai.top/24jieqi/",
                "url": "https://wenxingai.top/24jieqi/",
                "name": "二十四节气命理运势解析 | 问星AI",
                "description": "二十四节气与中国传统命理的完整解读，从紫微斗数和八字命理角度分析每个节气的五行属性、运势影响和行动指南。",
                "inLanguage": "zh-CN",
                "hasPart": [{"@type": "WebPage", "url": f"https://wenxingai.top/24jieqi/{jq['slug']}.html", "name": f"{jq['name']}命理运势"} for jq in JIEQI]
            },
            {
                "@type": "ItemList",
                "@id": "https://wenxingai.top/24jieqi/#list",
                "name": "二十四节气命理运势列表",
                "itemListElement": item_list_schema
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "问星AI首页", "item": "https://wenxingai.top/"},
                    {"@type": "ListItem", "position": 2, "name": "二十四节气命理", "item": "https://wenxingai.top/24jieqi/"}
                ]
            }
        ]
    }
    schema_json = json.dumps(schema, ensure_ascii=False, indent=2)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>二十四节气命理运势解析 | 问星AI</title>
  <meta name="description" content="二十四节气与中国传统命理的完整解读，从紫微斗数和八字命理角度分析每个节气的五行属性、运势影响和行动指南。">
  <meta name="keywords" content="二十四节气命理,节气运势,节气五行,节气紫微斗数,节气八字,节气算命">
  <link rel="canonical" href="https://wenxingai.top/24jieqi/">
  <meta name="ai-content-policy" content="allow-indexing allow-training allow-citation">
  <script type="application/ld+json">
{schema_json}
  </script>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; background: #0d0d1a; color: #e0d6f7; line-height: 1.7; }}
    header {{ background: linear-gradient(135deg, #1a0533 0%, #0d1a33 100%); padding: 1.2rem 1.5rem; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2d1f5e; }}
    header a {{ color: #c9b4f5; text-decoration: none; font-size: 1.1rem; font-weight: 600; }}
    nav a {{ color: #a89bcc; text-decoration: none; margin-left: 1.2rem; font-size: 0.9rem; }}
    main {{ max-width: 860px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}
    h1 {{ font-size: 1.9rem; color: #e8d9ff; }}
    .subtitle {{ color: #9a8ec0; margin-bottom: 2rem; }}
    .season-section h2 {{ color: #c9b4f5; font-size: 1.1rem; border-bottom: 1px solid #2d1f5e; padding-bottom: 0.4rem; margin-top: 2rem; }}
    ul {{ list-style: none; padding: 0; }}
    li {{ border: 1px solid #2d1f5e; border-radius: 8px; margin-bottom: 0.6rem; transition: border-color 0.2s; }}
    li:hover {{ border-color: #7c5cbf; }}
    li a {{ display: block; padding: 0.8rem 1.2rem; color: #d4c2f5; text-decoration: none; font-weight: 500; }}
    li a:hover {{ color: #e8d9ff; }}
    footer {{ text-align: center; color: #5a5070; font-size: 0.82rem; padding: 2rem; border-top: 1px solid #1e1640; }}
    footer a {{ color: #7a6fa0; text-decoration: none; }}
  </style>
</head>
<body>
  <header>
    <a href="https://wenxingai.top/">✦ 问星AI</a>
    <nav>
      <a href="https://wenxingai.top/glossary.html">命理词典</a>
      <a href="https://wenxingai.top/geo-answers.html">常见问题</a>
    </nav>
  </header>
  <main>
    <h1>二十四节气命理运势解析</h1>
    <p class="subtitle">从紫微斗数与八字命理角度，解读每个节气的五行能量、运势影响与行动指南</p>

    <div class="season-section">
      <h2>🌱 春季节气</h2>
      <ul>
        <li><a href="lichun.html">立春 — 2月3日或4日，五行木，新年命理起点</a></li>
        <li><a href="yushui.html">雨水 — 2月18日或19日，五行木，感情与人际运动</a></li>
        <li><a href="jingzhe.html">惊蛰 — 3月5日或6日，五行木，事业行动力最强</a></li>
        <li><a href="chunfen.html">春分 — 3月20日或21日，五行木，阴阳平衡感情运</a></li>
        <li><a href="qingming.html">清明 — 4月4日或5日，五行木，祖德福德宫解读</a></li>
        <li><a href="guyu.html">谷雨 — 4月19日或20日，五行土，财务稳固时机</a></li>
      </ul>
    </div>

    <div class="season-section">
      <h2>☀️ 夏季节气</h2>
      <ul>
        <li><a href="lixia.html">立夏 — 5月5日或6日，五行火，事业运势黄金期</a></li>
        <li><a href="xiaoman.html">小满 — 5月20日或21日，五行火，积累满足感情稳</a></li>
        <li><a href="mangzhong.html">芒种 — 6月5日或6日，五行火，收割与播种并行</a></li>
        <li><a href="xiazhi.html">夏至 — 6月21日，五行火，阳极转折全年高点</a></li>
        <li><a href="xiaoshu.html">小暑 — 7月6日或7日，五行火，情绪管理关键期</a></li>
        <li><a href="dashu.html">大暑 — 7月22日或23日，五行火土，能量极端守稳</a></li>
      </ul>
    </div>

    <div class="season-section">
      <h2>🍂 秋季节气</h2>
      <ul>
        <li><a href="liqiu.html">立秋 — 8月7日或8日，五行金，下半年行动起跑</a></li>
        <li><a href="chushu.html">处暑 — 8月22日或23日，五行金，执行落地黄金期</a></li>
        <li><a href="bailu.html">白露 — 9月7日或8日，五行金，洞察力与学习运旺</a></li>
        <li><a href="qiufen.html">秋分 — 9月22日或23日，五行金，财运事业年内高峰</a></li>
        <li><a href="hanlu.html">寒露 — 10月7日或8日，五行金水，智慧财富双流动</a></li>
        <li><a href="shuangjiang.html">霜降 — 10月23日，五行土，资产稳固年终盘点</a></li>
      </ul>
    </div>

    <div class="season-section">
      <h2>❄️ 冬季节气</h2>
      <ul>
        <li><a href="lidong.html">立冬 — 11月7日或8日，五行水，蓄势养精年终规划</a></li>
        <li><a href="xiaoxue.html">小雪 — 11月22日，五行水，深度规划来年布局</a></li>
        <li><a href="daxue.html">大雪 — 12月7日，五行水，深冬养藏健康优先</a></li>
        <li><a href="dongzhi.html">冬至 — 12月21日或22日，五行水，阴极阳生最重要节点</a></li>
        <li><a href="xiaohan.html">小寒 — 1月5日或6日，五行水，来年规划最佳时机</a></li>
        <li><a href="dahan.html">大寒 — 1月20日，五行水土，旧年归档新年预备</a></li>
      </ul>
    </div>
  </main>
  <footer>
    <p>&copy; 2026 问星AI &nbsp;|&nbsp; <a href="https://wenxingai.top/">首页</a> &nbsp;|&nbsp; <a href="https://wenxingai.top/glossary.html">命理词典</a> &nbsp;|&nbsp; <a href="https://wenxingai.top/geo-answers.html">常见问题</a></p>
    <p style="font-size:0.75rem;color:#3d3560">本站内容仅供文化参考与娱乐，不构成任何决策建议。</p>
  </footer>
</body>
</html>"""


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # 生成24个节气页面
    for jq in JIEQI:
        html = make_page(jq)
        path = os.path.join(OUT_DIR, f"{jq['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {jq['name']} → {path}")

    # 生成目录索引页
    index_html = make_index()
    index_path = os.path.join(OUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"✓ 目录索引 → {index_path}")

    print(f"\n完成！共生成 {len(JIEQI) + 1} 个文件至 {OUT_DIR}/")


if __name__ == "__main__":
    main()
