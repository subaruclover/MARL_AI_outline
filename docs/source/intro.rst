多智能体强化学习
=====================

.. _intro:

现有的（多智能体）强化学习中文社区教材和讲义
--------------------------------------------

**Let's 站在前人的肩膀上** 

.. _marl_material: 

1. RLChina 强化学习社区
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ``链接``：http://rlchina.org/ (推荐指数★★★★☆ (●ﾟ▽ﾟ●) )

    .. `链接 <http://rlchina.org/>`_

    UCL 汪军教授《Multi-agent AI》课程（中文字幕）Bilibili：

    `Multi-agent AI - 视频链接 <https://www.bilibili.com/video/BV1fz4y1S72S?p=1&vd_source=38b5017372fe991e5b7e30cb941ee82c>`_

    Multi-agent AI 课程简介（侧重多智能体）：

    该课程主要介绍人工智能（AI）的一个子领域——多智能体机器学习。多智能体学习在多个领域中均有体现，多智能体间不仅能与环境相互作用，而且彼此相互作用。因此，相关应用也越来越多，比如 `无人机群` 的控制和仓库机器人的合作，以及分布式传感器网络/交通的优化以及机器竞标。该课程将机器学习的研究与博弈论和经济学的研究相结合，包括 ``博弈论`` 、 ``拍卖理论`` 、 ``算法机制设计`` 、 ``多智能体（深度）强化学习`` 等主题。同时还将覆盖和讨论相关的实际应用，包括在线广告、在线拍卖、生成模型的对抗训练、机器人规划以及玩在线游戏的智能体。

    Multi-agent AI 课程大纲 (* : 侧重)： ::

       1. 第0讲 引言
       2. 第1.1讲 博弈论的基本概念
       3. 第1.2讲 纯策略纳什均衡
       4. 第1.3讲 混合策略纳什均衡
       5. 第1.4讲 纳什均衡的存在性证明
       6. 第1.5讲 古诺双寡头模型
       7. 第2.1讲 重复博弈
       8. 第2.2讲 扩展形式博弈
       9. 第2.3讲 势博弈上
       10. 第2.4讲 势博弈下
       11. 第3.1讲 零和博弈及纳什均衡计算 *
       12. 第3.2讲 极大极小博弈
       13. 第3.3讲 纳什均衡的线性规划解法
       14. 第3.4讲 线性互补性问题
       15. 第3.5讲 Lemke-Howson算法求解线性互补性问题
       16. 第4.1讲 贝叶斯博弈 *
       17. 第4.2讲 在线拍卖的设置与步骤
       18. 第4.3讲 拍卖模式：一口价拍卖与密封式拍卖
       19. 第4.4讲 竞价策略与纳什均衡上
       20. 第4.5讲 竞价策略与纳什均衡下
       21. 第5.1讲 深度学习基础 *
       22. 第5.2讲 词嵌入
       23. 第5.3讲 深度神经网路层 *
       24. 第5.4讲 卷积神经网路 *
       25. 第5.5讲 循环神经网络 *
       26. 第5.6讲 网络信息搜索
       27. 第5.7讲 表征学习
       28. 第6.1讲 强化学习基础 *
       29. 第6.2讲 model-based方法 *
       30. 第6.3讲 model-free方法 *
       31. 第7.1讲 多智能体强化学习介绍及基本概念 *
       32. 第7.2讲 值迭代与策略迭代 *
       33. 第7.3讲 均衡学习
       34. 第7.4讲 最佳对策
       35. 第8.1讲 策略方法
       36. 第8.2讲 策略方法学习理论介绍
       37. 第8.3讲 理论分析
       38. 第9.1讲 采用策略预测的IGA
       39. 第9.2讲 类动态系统的梯度提升优化
       40. 第9.3讲 不同博弈中的学习
       41. 第9.4讲 虚拟模拟
       42. 第9.5讲 平滑虚拟博弈
       43. 第9.6讲 理性学习
       44. 第9.7讲 演化博弈论
       45. 第9.8讲 模仿者动态理论
       46. 第10.1讲 相关均衡与无悔学习
       47. 第10.2讲 多智能体评价 *
       48. 第10.3讲 多智能体强化学习：进阶主题 *

.. _marl_material2:

2. 伯禹AI (由上海交通大学张伟楠教授团队出品)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ``链接``：https://www.boyuai.com/elites/ (推荐指数★★★★★ (✪ω✪) )

    伯禹AI强化学习课程：
    
    `强化学习课程链接 (需要登陆/注册) <https://www.boyuai.com/elites/course/xVqhU42F5IDky94x>`_
    

    伯禹AI 强化学习课程大纲 (每小节后有课后习题/代码实践 * )： 

    #. ``模块一 / 强化学习基础`` ::

        - 多臂老虎机 (Multi-armed bandits problem) / 
        - 马尔科夫决策过程 (Markov Decision Process (MDP)) / 
        - 基于动态规划的强化学习 (Dynamic Programing (DP)) 「代码实践」*

    #. ``模块二 / 模型无关强化学习方法 (model-free RL)`` ::

        - 蒙特卡罗方法 (Monte Carlo (MC) method) /
        - 蒙特卡罗价值预测 (MC value based evaluation (Prediction)) /
        - 重要性采样 (Importance sampling) /
        - 时序差分学习 (Temporal difference (TD) learning) /
        - SARSA 「代码实践」* / 
        - Q-learning 「代码实践」* /
        - 多步自助法 (n-step) /
        - 参数化值函数近似 (Function approximation) /
        - 状态值函数与状态-动作值函数 (State value function and state-action value function)/
        - 策略梯度方法 (Policy gradiant (PG) method) /
        - Actor-Critic

    #. ``模块三 / 基于模型的强化学习方法 (model-based RL)`` ::    

        - 代码实践：策略梯度
        - 规划与学习之入门算法与介绍 (Policy Programing) /
        - 规划与学习之采样方法 (Sampling) /
        - 规划与学习之决策时规划 (Policy)

    #. ``模块四 / 深度强化学习 (Deep RL)`` ::

        - 深度强化学习介绍 (Deep Reinforcement Learning) /
        - 深度Q网络 (Deep-Q network (DQN)) 「代码实践」* /
        - A3C (Asynchronous Advantage Actor-Critic) 「代码实践」* /
        - 信任域策略优化 (Trust region policy optimization (TRPO))/
        - 邻近策略优化 (Proximal policy optimization (PPO)) 「代码实践」* /
        - 确定性策略梯度 (Deterministic Policy Gradient (DPG)) /
        - 深度确定性策略梯度 (Deep Deterministic Policy Gradient (DDPG))

    #. ``模块五 / 强化学习进阶`` ::

        - 概率图强化学习：Soft Q-learning & Soft Actor-Critic /
        - 模仿学习 (Imitation learning) /
        - 行为克隆 /
        - 逆强化学习 (Inverse RL) /
        - 生成对抗模仿学习 (Generative adversarial imitation learning (GAIL)) /
        - 参数化动作空间 /
        - 模型预测控制 /
        - 基于模型的策略优化 /
        - 目标导向的强化学习 /
        # 多智能体强化学习 (MARL) /
        - 离线强化学习 (offline RL)

.. _marl_material3:

3. 西湖大学 (课本、视频) 赵世钰教授团队，飞行器控制领域
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    《强化学习的数学原理》（从零开始透彻理解强化学习）侧重从数学基础推导出发，从零基础开始介绍强化学习，并配套对应的书籍(不断更新中)和视频课程讲解，推荐没有 **强化学习基础** 同学学习。每周一/二更新，线上线下同步，预计2022年年底前更新完毕。

    ``链接`` `书籍和课件链接 <https://github.com/MathFoundationRL/Book-Mathmatical-Foundation-of-Reinforcement-Learning>`_ (推荐指数★★★★★ (✪ω✪) )

    课程视频（中文）Bilibili 和 Youtube频道：

    `Bilibili 视频链接 <https://space.bilibili.com/2044042934>`_

    `Youtube频道视频链接 <https://www.youtube.com/channel/UCztGtS5YYiNv8x3pj9hLVgg/playlists>`_

    课程大纲

    .. image:: /_static/images/mathRL.png
        :width: 900
        :alt: MathFoundationRL_chapterRelationship

    #. ``第0课 | 课程介绍`` ::

        - 0.1 开发这门课的动因 
        - 0.2 AlphaGo的故事，强化学习的历史、分类等 

    #. ``第1课 | 基本概念`` ::
    
        - 1.1 State, action, policy等 
        - 1.2 Reward, Return, MDP等
    
    #. ``第2课 | 贝尔曼公式`` ::

        - 2.1 例子说明Return的重要性
        - 2.2 State value的定义
        - 2.3 贝尔曼公式的详细推导
        - 2.4 公式向量形式与求解
        - 2.5 Action value的定义

    #. ``第3课 | 贝尔曼最优公式`` ::
    
        - 3.1 例子-如何改进策略
        - 3.2 最优策略和公式推导
        - 3.3 公式求解以及最优性
        - 3.4 最优策略的有趣性质
    
    #. ``第4课 | 值迭代与策略迭代`` ::
        
        - 4.1 值迭代算法
        - 4.2 策略迭代算法
        - 4.3 截断策略迭代算法

    #. ``第5课 | 蒙特卡罗方法`` ::
        
        - 5.1 通过例子介绍蒙特卡罗
        - 5.2 MC Basic算法介绍
        - 5.3 MC Basic算法例子
        - 5.4 MC Exploring Starts算法
        - 5.5 MC Epislon-Greedy算法介绍
        - 5.6 MC Epislon-Greedy算法例子

    #. ``第6课 | 随机近似与随机梯度下降`` ::
        
        - 6.1 通过例子介绍Iterative mean estimation
        - 6.2 Robbins-Monro（RM）算法介绍与例子
        - 6.3 Robbins-Monro算法收敛性及应用
        - 6.4 随机梯度下降（Stochastic Gradient Descent）算法介绍
        - 6.5 随机梯度下降收敛性及例子
        - 6.6 随机梯度下降有趣的性质
        - 6.7 随机梯度下降（SGD）对比BGD（Batch GD）、MBGD（Mini-batch GD）
    
    #. ``第7课 | 时序差分学习（TD Learning）`` ::
        
        - 7.1 例子
        - 7.2 SARSA
        - 7.3 Q-learning
        - 7.4 

    #. ``第8课 | Value function approx`` ::
        
        - 8.1 例子
        - 8.2 目标函数
        - 8.3 优化算法
        - 8.4 线性函数近似
        - 8.5 DQN
   
    #. ``第9课 | Policy function approx (PG)`` ::
        
        - 9.1 策略梯度概念
        - 9.2 
        - 9.3 
        - 9.4 

    #. ``第10课 | Actor-Critic methods`` ::
        
        - 10.1 
        - 10.2 
        - 10.3 
        - 10.4 

.. _marl_material4:

4. 其他相关课程和资料
^^^^^^^^^^^^^^^^^^^^^^^^

    英文学习材料：

    #. 强化学习课程 RL Course by David Silver （2015） `课程视频(Youtube)和课件 <https://www.davidsilver.uk/teaching/>`_

    #. CS285 (English) @ UC Berkeley 深度强化学习（DRL）课程 `CS285课程视频(Youtube)和课件 <http://rail.eecs.berkeley.edu/deeprlcourse/>`_

    #. OpenAI Spinning Up (`Spinning Up in Deep RL <https://spinningup.openai.com/en/latest/>`_)

    #. OpenAI bootcamp (`视频和课件 <https://sites.google.com/view/deep-rl-bootcamp/lectures>`_)

    中文学习材料：

    #. 天授平台 (`英文文档 <https://tianshou.readthedocs.io/en/master/>`_， `中文文档 <https://tianshou.readthedocs.io/zh/master/>`_)

    #. 强化学习课程 by UCLA 周博磊教授 (`Github <https://github.com/zhoubolei/introRL>`_, `Bilibili <https://space.bilibili.com/511221970/channel/seriesdetail?sid=764099&ctype=0>`_)

    #. 莫烦python - `强化学习 <https://mofanpy.com/tutorials/machine-learning/reinforcement-learning/>`_， `GitHub Repo on RL with TF <https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow>`_

    #. 机器学习与深度学习、强化学习 邹博 （2019）

.. _marl_material5:

5. **多智能体强化学习文献综述（MARL survey）& Papers:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    （In year order）

    * Hernandez-Leal, Pablo, Bilal Kartal, and Matthew E. Taylor. "A survey and critique of multiagent deep reinforcement learning." *Autonomous Agents and Multi-Agent Systems* 33.6 (2019): 750-797.

    * Nguyen, Thanh Thi, Ngoc Duy Nguyen, and Saeid Nahavandi. "Deep reinforcement learning for multiagent systems: A review of challenges, solutions, and applications." *IEEE transactions on cybernetics* 50.9 (2020): 3826-3839.

    * Zhang, Kaiqing, Zhuoran Yang, and Tamer Başar. "Multi-agent reinforcement learning: A selective overview of theories and algorithms." *Handbook of Reinforcement Learning and Control* (2021): 321-384.

    * Oroojlooy, Afshin, and Davood Hajinezhad. "A review of cooperative multi-agent deep reinforcement learning." *Applied Intelligence* (2022): 1-46.

    * Fu, Wei, Chao Yu, Zelai Xu, Jiaqi Yang, and Yi Wu. "Revisiting some common practices in cooperative multi-agent reinforcement learning." *arXiv preprint* arXiv:2206.07505 (2022).

    * Fu, Qingxu, et al. "Concentration Network for Reinforcement Learning of Large-Scale Multi-Agent Systems." *arXiv preprint* arXiv:2203.06416 (2022).  (AAAI-22 中科院自动化所-飞行器智能技术，多智能体AI， `视频讲解训练全过程展示 <https://www.bilibili.com/video/BV1vF411M7N9?share_source=copy_web&vd_source=3a42fd9dcf75064acaf3ec0f8218e373>`_ )


    * 【多智能体强化学习】新手入门算法论文大总结 `知乎专栏1 <https://zhuanlan.zhihu.com/p/432241482>`_ 

    * 基于通信的多智能体强化学习方法——简介及研究现状 `知乎专栏2 <https://zhuanlan.zhihu.com/p/421098367>`_


    .. RL 溯源，分支 -> control theory, neuroscience (old paper)

``小结当前的单智能体RL``：基本上所有的课程和讲义，都涵盖了MDP、DP、MC、TD方法、PG方法，其中又可分为model-based/free的情形。无论参考哪一个学习路径，这些都是RL学习中需要掌握和理解的概念。

.. _marl_course_design:

本课程设计大纲（MARL部分）
-----------------------------

.. _marl_preface:

1. 前言 - 为什么使用腾讯开悟平台学习多智能体强化学习?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Preface - why MARL with AI Arena

当前在强化学习领域中，对MARL这一块目前没有很系统的介绍，最初RL用于单个个体 (single agent) 在和环境和互动中习得如何做决策，学习达到奖励的策略。现在大量的关注涌向了多智能体的领域，状态空间，状态-行为空间急速上升，其他智能体和环境的仅部分可观测特性使得适用于单智能体的算法在多智能体的情况下往往不再适用。当然，如果我们可以把智能体当成单个的智能体，其他智能体和环境全都看做环境，这样的“独立”智能体简单的将多智能体的问题转化成单智能体的考虑范畴，但这样做训练效果往往不尽人意。越来越多的科研人员从不同的角度提出了许多效果还不错的算法。
我们可以按照任务的标准或者模型的标准来划分各种多智能体的算法分类。而本课程的多智能体RL部分，将对每一个类别中比较具有代表性的算法进行讲解，每一种算法都会从论文本身出发，配合代码讲解。此外，腾讯开悟平台是首个国内以游戏 **王者荣耀** 为实验平台开发的API，可以实现 *1v1 ~ 5v5* 的不同数量的智能体的合作/对抗实验测试，是本课程MARL部分将使用的测试平台，同学们将通过学习如何配置实验环境，如何将不同的算法应用在开悟平台中，理解和掌握RL的算法和实验过程。

.. 分类 advantage function, baselines, COMA, MAAC, SAC, QMIX, VDN

.. 现有的解决方案

.. 实例讲解（代码实践）

.. _marl_background:

2. MARL概念和背景知识
^^^^^^^^^^^^^^^^^^^^^^^^^

* 追溯MARL（不仅仅是MA-DRL）的历史，联合行为（joint action）、联合策略（joint policy）、最优解（optimal policy）等的表达式。
* 初代MARL，零和（zero-sum）MAL，最大最小Q方法（minimax-Q）
* MARL的收敛情况，其他常见的问题
* 各种不同方法的主旨：改善POMDP带来的问题

.. _marl_taxonomy:

3. 主流的MARL分类（Taxonomy）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

主要在多智能体深度强化学习（MADRL/MDRL）范围展开

不同分类下的代表算法-当前提出的算法 (分别根据不同的分类标准)
    
    * 基于进化（涌现）的行为 （Based on emergent behaviors）
  
       * OpenAI: Learning to Cooperate, Compete, and Communicate ( `Emergence of grounded compositional language in multi-agent populations. <https://openai.com/blog/learning-to-cooperate-compete-and-communicate/>`_)
       * OpenAI hide and seek (`Emergent Tool Use From Multi-Agent Autocurricula <https://openai.com/blog/emergent-tool-use/>`_)
       * Riddle (Decentrailaized-centerailized)

    * 智能体之间引入通信/交流 Learning communication
       
       * RIAL
       * DIAL
       * MADDPG (理解DDPG的前提下)
       * 其他方法 
 
    * 智能体之间合作 Cooperative MARL
       
       * VDN
       * QMIX
       * COMA
       * MADDPG
   
    * 基于模型的MARL Agents modeling agent (need people who are working on this to elaborate on)

.. _marl_algs:

4. 算法介绍，代码（Algorithms introduction and code）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * 和第3部分（ :ref:`marl_taxonomy`）结合，对每一种算法进行详细的介绍、代码演示、结果分析。
   * 不同算法之间的比较（在同一个环境和实验任务中，结合baselines）

.. _marl_aiarena:

5. 与腾讯开悟平台结合的MARL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    #. 开悟平台介绍（目前开源的平台以及提供的baselines介绍）
    #. 实例讲解 
    #. 代码实践 （选择上面介绍的MARL中的一些算法进行实际实验）


**一些拓展**
    * Attention is all you need (Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30.) `paper <https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf>`_
    * GNN+RL，与图神经网络结合的RL部分，在MARL中的应用

**细化课程要点：**

``每堂课的课后习题（Q&A设计）``

``实例讲解``

``助教答疑（团队）``

``课件模板（实战云template、theme）``

.. note::
    多智能体部分是进阶内容

    .. 要明确这不是一门零基础课

    .. 是进阶课
    
    时间：以年为单位

    参考文献、书籍 链接: `Github link <https://github.com/subaruclover/MARL_AI_outline/tree/main/docs/source/_static/references>`_ （ ``要注意书籍版权`` ）

    ``Books and papers (不断补充中)`` 

    * For Multi-Agent Systems:
        `Multiagent Systems - algorithmic, game-theoretic & logical foundations <https://github.com/subaruclover/MARL_AI_outline/blob/main/docs/source/_static/references/Multiagent%20Systems%20algorithmic%2C%20game-theoretic%20and%20logical%20foundations.pdf>`_ 


    * 强化学习（ + 每一个文档的链接）:
        | Sutton (1st & 2nd edition)
        | Algorithms RL 
        | MDP 2013
        | Shiyu Zhao 2022 MathFoundationRL
        | Weinan Zhang 2022 (hands on RL in Chinese, new book)
        | etc...
        | paper (DRL, MARL)
        | hands on DRL (books)
    
    
    * 机器学习:
        | PRML Bishop (Link)

    * 腾讯开悟平台:
        | Ye. D, et al. **Towards Playing Full MOBA Games with Deep Reinforcement Learning** (`paper1 <https://github.com/subaruclover/MARL_AI_outline/blob/main/docs/source/_static/references/Towards%20Playing%20Full%20MOBA%20Games%20with%20Deep%20Reinforcement%20Learning.pdf>`_), 2020 NeurIPS 
        | Wei. H et al, **Honor of Kings Arena: an Environment for Generalization in Competitive Reinforcement Learning** (`paper2 <https://github.com/subaruclover/MARL_AI_outline/blob/main/docs/source/_static/references/Honor%20of%20Kings%20Arena-%20an%20Environment%20for%20Generalization%20in%20Competitive%20Reinforcement%20Learning.pdf>`_), 2022 NeurIPS (`Github repo <https://github.com/tencent-ailab/hok_env>`_)

       
