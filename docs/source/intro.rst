多智能体强化学习
=====================

.. _intro:

现有的(多智能体)强化学习中文社区教材和讲义
--------------------------------------------

.. _marl_material:

1. RLChina 强化学习社区
^^^^^^^^^^^^^^^^^^^^^^^^^

    ``链接``：http://rlchina.org/

    .. `链接 <http://rlchina.org/>`_

    UCL 汪军教授《Multi-agent AI》课程（中文字幕）Bilibili：

    `Bilibili 视频链接 <https://www.bilibili.com/video/BV1fz4y1S72S?p=1&vd_source=38b5017372fe991e5b7e30cb941ee82c>`_

    Multi-agent AI 课程简介 (侧重多智能体)：

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

    ``链接``：https://www.boyuai.com/elites/

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

    《强化学习的数学原理》（从零开始透彻理解强化学习）侧重从数学基础推导出发，从零基础开始介绍强化学习，并配套对应的书籍(不断更新中)和视频课程讲解，推荐没有 **强化学习基础** 同学学习。每周一更新。

    ``链接`` `书籍和课件链接 <https://github.com/MathFoundationRL/Book-Mathmatical-Foundation-of-Reinforcement-Learning>`_

    课程视频（中文）Bilibili 和 Youtube频道：

    `Bilibili 视频链接 <https://space.bilibili.com/2044042934>`_

    `Youtube频道视频链接 <https://www.youtube.com/channel/UCztGtS5YYiNv8x3pj9hLVgg/playlists>`_

    课程大纲

    .. image:: /_static/images/mathRL.png
        :alt: MathFoundationRL_chapterRelationship

    #. ``第0课 | 课程介绍`` ::

        - 开发这门课的动因 / 
        - AlphaGo的故事，强化学习的历史、分类等 / 

    #. ``第1课 | 基本概念`` ::
    
        - State, action, policy等 
        - Reward, return, MDP等
    
    #. ``第2课 | 贝尔曼公式`` ::

        - 例子
        - state value
        - 公式
        - 公式
        - action 

    #. ``第3课 | 贝尔曼公式`` ::
    
        - 例子
        - 2
        - 3
        - 4
    
    #. ``第4课 | 值迭代和策略迭代`` ::
        
        - 例子
        - 2
        - 3

    #. ``第5课 | 蒙特卡罗方法`` ::
        
        - 例子
        - 2
        - 3
        - 4
        - 5
        - 6

    #. ``第6课 | 随机近似与随机梯度下降`` ::
        
        - 例子
        - 2
        - 3
        - 4
        - 5
        - 6
        - 7    
    
    #. ``第7课 | TD`` ::
        
        - 例子
        - 2
        - 3
        - 4

    #. ``第8课 | value function approx`` ::
        
        - 例子
        - 2
        - 3
        - 4
   
    #. ``第9课 | policy function approx (PG)`` ::
        
        - 例子
        - 2
        - 3
        - 4

    #. ``第10课 | AC methods`` ::
        
        - 例子
        - 2
        - 3
        - 4

.. _marl_material4:

1. 其他相关课程和资料
^^^^^^^^^^^^^^^^^^^^^^^^

    伯克利+上海交通大学 RL

    CS285 (English)

    OpenAI SpinningUp

    Tianshou platform

    AAAI-22 中科院自动化所-飞行器智能技术，多智能体AI团队
    Concentration network for Reinforcement Learning of Large-scale Multi-agent systems


参考文献（MARL survey）list

 RL 溯源，分支 -> control theory, neuroscience (old paper)


课程设计
----------------

前言 - 为什么使用腾讯开悟平台学习多智能体强化学习?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Preface - why MARL with AI Arena

当前在强化学习领域中，对MARL这一块目前没有很系统的介绍，最初RL用于单个个体 (single agent) 在和环境和互动中习得如何做决策，学习达到奖励的策略。现在大量的关注涌向了多智能体的领域，状态空间，状态-行为空间急速上升，其他智能体和环境的仅部分可观测特性使得适用于单智能体的算法在多智能体的情况下往往不再适用。我们可以按照任务的标准或者模型的标准来划分各种多智能体的算法分类。腾讯开悟平台是首个国内以游戏 **王者荣耀** 为实验平台开发的API，可以实现 *1v1 ~ 5v5* 的不同数量的智能体的合作/对抗实验测试。

分类

现有的解决方案

实例讲解（代码实践）

.. _marl_outline:

课程设计outline 
^^^^^^^^^^^^^^^^^^^

MARL Concept
^^^^^^^^^^^^^^^^^^^

Classification
^^^^^^^^^^^^^^^^^^^

Current solutions (based on different criteria)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    --Cooperative
   
    --Model

Algorithms introduction and code review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect with AI Arena platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


课后习题（后面设计）

实例讲解

助教答疑（团队）


课件模板

.. note::
    要明确这不是一门零基础课

    是进阶课

    但是也不担心学不明白
    
    时间：以年为单位

    参考文献: https://github.com/subaruclover/MARL_AI_outline/tree/main/docs/source/_static/references

    ``Books and papers (不断补充中)``

    * For Multiagent Systems:

        `Multiagent Systems - algorithmic, game-theoretic & logical foundations <https://github.com/subaruclover/MARL_AI_outline/tree/main/docs/source/_static/references>`_


    * 强化学习:

        Sutton
        Algorithms
        MDP 2013
        Shiyu Zhao 2022
        Weinan Zhang (hands on RL, new book)
        etc
        paper (DRL, MARL)
    
    
    * 机器学习:
        PRML Bishop

    * 腾讯开悟平台:
        2020 NeurIPS (github)
        2022 NeurIPS (github)

       
