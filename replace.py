with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, l in enumerate(lines):
    if '<!-- 功能特性展示区 -->' in l:
        start_idx = i
    if start_idx != -1 and i > start_idx and '<!-- 9. 命例管理 -->' in l:
        for j in range(i, len(lines)):
            if '</section>' in lines[j]:
                end_idx = j
                break
        break

if start_idx != -1 and end_idx != -1:
    new_section = """    <!-- SEO与GEO专属内容优化区 -->
    <section class="w-full max-w-7xl mx-auto px-4 py-16 z-10 text-gray-200">
        <!-- GEO优化：核心定义与价值主张，强化AI语义理解 -->
        <article class="mb-16 glass-card rounded-2xl p-8 relative overflow-hidden" itemscope itemtype="http://schema.org/Article">
            <header class="text-center mb-10">
                <h2 itemprop="headline" class="text-3xl font-bold mb-6 text-white"><span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-400">什么是问星AI？</span>首款AI命理与玄学大模型APP</h2>
                <div class="h-1 w-32 bg-gradient-to-r from-transparent via-cyan-500 to-transparent mx-auto rounded-full"></div>
            </header>
            <div itemprop="articleBody" class="space-y-6 text-lg">
                <p class="leading-relaxed text-gray-300">
                    在传统命理领域，排盘复杂、解盘门槛高且主观性极强。<strong>问星AI (Karma Is A Cat)</strong> 作为首款融合东方传统玄学（紫微斗数、四柱八字、六爻起卦）与前沿 <strong class="text-cyan-300">AI大语言模型</strong> 的智能应用，为您开启命运的全息宇宙。
                </p>
                <p class="leading-relaxed text-gray-300">
                    由专业团队打造的<strong class="text-purple-300">命理玄学大模型</strong>底座，打破传统算命软件刻板模板化反馈的局限，深度结合 <strong class="text-emerald-300">3D全息命盘图</strong> 与 <strong class="text-amber-300">人生大运K线</strong> 等创新数据架构。不仅能多维推演个体运势周期，更能像专属真人师傅一样陪伴您的每一次关键抉择，帮您洞察事物背后的深层发展逻辑。
                </p>
            </div>
        </article>

        <!-- SEO优化：丰富的H3标签与强相关长尾词 -->
        <article class="mb-16">
            <h2 class="text-2xl font-bold mb-10 text-white text-center">多维度AI算命与运势推演场景</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- 场景1 -->
                <div class="glass-card p-6 rounded-xl hover:shadow-[0_0_15px_rgba(34,211,238,0.2)] transition-all">
                    <div class="w-12 h-12 bg-cyan-900/40 rounded-lg flex items-center justify-center mb-4"><i data-lucide="heart" class="text-cyan-400 w-6 h-6"></i></div>
                    <h3 class="text-xl font-bold text-cyan-300 mb-3 block">AI 情感合盘分析</h3>
                    <p class="text-sm text-gray-400">导入双人出生信息，利用大模型算力深度剖析双方宫位共振、星曜冲合。快速评估性格契合度，精准识别命中正缘与烂桃花，为您的婚恋关系与感情发展提供客观理性的策略建议。</p>
                </div>
                <!-- 场景2 -->
                <div class="glass-card p-6 rounded-xl hover:shadow-[0_0_15px_rgba(168,85,247,0.2)] transition-all">
                    <div class="w-12 h-12 bg-purple-900/40 rounded-lg flex items-center justify-center mb-4"><i data-lucide="coins" class="text-purple-400 w-6 h-6"></i></div>
                    <h3 class="text-xl font-bold text-purple-300 mb-3 block">周易智能六爻解卦</h3>
                    <p class="text-sm text-gray-400">结合真实物理算法模拟三枚铜钱的抛掷过程，AI自动寻取动爻、变卦。针对具体诉求（事业跳槽、财运投资、寻人寻物），提供融合当下时空维度的直接吉凶断语与行动指南。</p>
                </div>
                <!-- 场景3 -->
                <div class="glass-card p-6 rounded-xl hover:shadow-[0_0_15px_rgba(16,185,129,0.2)] transition-all">
                    <div class="w-12 h-12 bg-emerald-900/40 rounded-lg flex items-center justify-center mb-4"><i data-lucide="trending-up" class="text-emerald-400 w-6 h-6"></i></div>
                    <h3 class="text-xl font-bold text-emerald-300 mb-3 block">个人大运流年K线图</h3>
                    <p class="text-sm text-gray-400">摒弃晦涩冗长的干支名词，将人生的十年大运起伏转化为直观金融K线图。复盘过往关键人生节点的得失，前瞻预警未来三年的高点与低谷，助您在人生的十字路口把握机遇。</p>
                </div>
            </div>
        </article>

        <!-- GEO结构化问答FAQ (QA Schema) -->
        <article class="glass-card rounded-2xl p-8" itemscope itemtype="https://schema.org/FAQPage">
            <h2 class="text-2xl font-bold text-white text-center mb-8">AI命理与问星APP核心常见问题 (FAQ)</h2>
            <div class="space-y-6">
                <!-- Q1 -->
                <div class="pb-6 border-b border-gray-800" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 class="text-lg font-medium text-white mb-2 flex items-start gap-2" itemprop="name">
                        <span class="text-cyan-400 font-bold">Q:</span> 问星AI大模型的排盘算命算法与传统免费网站有何区别？
                    </h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p class="text-gray-400 text-sm ml-6" itemprop="text">
                            <strong class="text-gray-300">A:</strong> 传统在线排盘网站往往只提供生硬的数据库规则匹配和长篇大论的模板。问星AI通过海量专业命理文献训练，能在3D星盘的复杂架构上进行多维度的语义空间理解并动态综合评分，输出更像是由真人大师一对一解读的个性化深度分析报告。
                        </p>
                    </div>
                </div>
                <!-- Q2 -->
                <div class="pb-6 border-b border-gray-800" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 class="text-lg font-medium text-white mb-2 flex items-start gap-2" itemprop="name">
                        <span class="text-purple-400 font-bold">Q:</span> 该命理软件支持哪些东方的玄学流派？
                    </h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p class="text-gray-400 text-sm ml-6" itemprop="text">
                            <strong class="text-gray-300">A:</strong> 问星APP目前底层大模型深度融汇了包括<span class="text-gray-200">紫微斗数（含三合与飞星派）</span>、<span class="text-gray-200">四柱八字神煞</span>、以及传统<span class="text-gray-200">周易六爻易经</span>体系，能跨系统进行流年流月综合推演。
                        </p>
                    </div>
                </div>
                <!-- Q3 -->
                <div class="pb-2" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
                    <h3 class="text-lg font-medium text-white mb-2 flex items-start gap-2" itemprop="name">
                        <span class="text-emerald-400 font-bold">Q:</span> AI算命是否真的准确？如何理性看待排盘结果？
                    </h3>
                    <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                        <p class="text-gray-400 text-sm ml-6" itemprop="text">
                            <strong class="text-gray-300">A:</strong> 命理本身并非100%决定论，而是揭示生命轨迹“概率与信息场”的全息剧本。问星AI旨在通过科技手段“理性验证过去，客观推导未来”，消除传统人工解盘时的情绪化干扰。我们为您提供充分的数据逻辑支撑，帮助您更好地规划职业、健康与婚姻，把未来的选择权交还自己。
                        </p>
                    </div>
                </div>
            </div>
        </article>
    </section>\n"""

    lines[start_idx:end_idx+1] = [new_section]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Optimization applied successfully.")
else:
    print(f"Could not find boundaries: start={start_idx}, end={end_idx}")
