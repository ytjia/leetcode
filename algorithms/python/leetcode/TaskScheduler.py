# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where
different letters represent different tasks.Tasks could be done without original order. Each task
could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must
be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

https://leetcode.com/problems/task-scheduler/description/
"""

from Queue import PriorityQueue


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        task_stat = dict()
        for task in tasks:
            if task in task_stat:
                task_stat[task] += -1
            else:
                task_stat[task] = -1

        p_queue = PriorityQueue()
        for task, cnt in task_stat.items():
            p_queue.put((cnt, task))

        interval_cnt = 0
        while not p_queue.empty():
            buff = list()
            for i in range(n + 1):
                if not p_queue.empty():
                    cur_task = p_queue.get()
                    if cur_task[0] + 1 < 0:
                        buff.append((cur_task[0] + 1, cur_task[1]))
                    interval_cnt += 1
                # 还有待处理的任务
                elif len(buff) > 0:
                    interval_cnt += n + 1 - i
                    break
                else:
                    break
            for t_s in buff:
                p_queue.put(t_s)

        return interval_cnt
