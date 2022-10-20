多智能体强化学习
=====================

.. _intro:

现有的(多智能)体强化学习中文社区教材和讲义
--------------------------------------------

.. _marl_material:

1. RLChina 强化学习社区
^^^^^^^^^^^^^^^^^^^^^^^^^

    链接：http://rlchina.org/

    UCL 汪军教授《Multi-agent AI》课程（中文字幕）

    https://www.bilibili.com/video/BV1fz4y1S72S?p=1&vd_source=38b5017372fe991e5b7e30cb941ee82c

.. _marl_material2:

2. 伯禹AI(由上海交通大学张伟楠教授团队出品)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ``链接``：https://www.boyuai.com/elites/

    强化学习课程：https://www.boyuai.com/elites/course/xVqhU42F5IDky94x

    伯禹AI 强化学习课程大纲： 

    #. ``模块一 / 强化学习基础`` ::

        - 多臂老虎机 (Multi-armed bandits problem) / 
        - 马尔科夫决策过程 (Markov Decision Process (MDP)) / 
        - 基于动态规划的强化学习 (Dynamic Programing (DP)) 「代码实践」

    #. ``模块二 / 模型无关强化学习方法 (model-free RL)`` ::

        - 蒙特卡罗方法 (Monte Carlo (MC) method) /
        - 蒙特卡罗价值预测 (MC value based evaluation (Prediction)) /
        - 重要性采样 (Importance sampling) /
        - 时序差分学习 (Temporal difference (TD) learning) /
        - SARSA 「代码实践」/ 
        - Q-learning 「代码实践」/
        - 多步自助法 (n-step) /
        - 参数化值函数近似 (Fucntion approximation) /
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
        - 深度Q网络 (Deep-Q network (DQN)) 「代码实践」 /
        - A3C (Asynchronous Advantage Actor-Critic) 代码实践」/
        - 信任域策略优化 (Trust region policy optimization (TRPO))/
        - 邻近策略优化 (Proximal policy optimization (PPO)) 「代码实践」/
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

3. 西湖大学(课本，视频)赵世钰教授团队，飞行器控制领域
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    书籍链接 https://github.com/MathFoundationRL/Book-Mathmatical-Foundation-of-Reinforcement-Learning

    课程视频（中文）
    Bilibili https://space.bilibili.com/2044042934 
    Youtube频道 https://www.youtube.com/channel/UCztGtS5YYiNv8x3pj9hLVgg/playlists

.. _marl_material4:

4. 其他相关课程和资料
^^^^^^^^^^^^^^^^^^^^^^^^

    伯克利+上海交通大学 RL

    AAAI-22 中科院自动化所-飞行器智能技术，多智能体AI团队
    Concentration network for Reinforcement Learning of Large-scale Multi-agent systems


参考文献（MARL survey）list

 RL 溯源，分支 -> control theory, neuroscience (old paper)


课程设计
----------------

当前在强化学习领域中，对MARL这一块目前没有很系统的介绍，最初RL用于单个个体 (single agent) 在和环境和互动中习得如何做决策，学习达到奖励的策略。现在大量的关注涌向了多智能体的领域，状态空间，状态-行为空间急速上升，其他智能体和环境的仅部分可观测特性使得适用于单智能体的算法在多智能体的情况下往往不再适用。我们可以按照任务的标准或者模型的标准来划分各种多智能体的算法分类。

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

    参考文件: https://github.com/subaruclover/MARL_AI_outline/tree/main/docs/source/_static/references

