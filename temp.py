# 基于用户的召回 u2u2i
def user_based_recommend(user_id, user_item_time_dict, u2u_sim, sim_user_topk, recall_item_num,
                         item_topk_click, item_created_time_dict, emb_i2i_sim):
    """
        基于文章协同过滤的召回
        :param user_id: 用户id
        :param user_item_time_dict: 字典, 根据点击时间获取用户的点击文章序列   {user1: [(item1, time1), (item2, time2)..]...}
        :param u2u_sim: 字典，文章相似性矩阵
        :param sim_user_topk: 整数， 选择与当前用户最相似的前k个用户
        :param recall_item_num: 整数， 最后的召回文章数量
        :param item_topk_click: 列表，点击次数最多的文章列表，用户召回补全
        :param item_created_time_dict: 文章创建时间列表
        :param emb_i2i_sim: 字典基于内容embedding算的文章相似矩阵

        return: 召回的文章列表 [(item1, score1), (item2, score2)...]
    """
    # 历史交互
    user_item_time_list = user_item_time_dict[user_id]  # {item1: time1, item2: time2...}
    user_hist_items = set([i for i, t in user_item_time_list])  # 存在一个用户与某篇文章的多次交互， 这里得去重

    items_rank = {}
    for sim_u, wuv in sorted(u2u_sim[user_id].items(), key=lambda x: x[1], reverse=True)[:sim_user_topk]:
        try:
            for i, click_time in user_item_time_dict[sim_u]:
                if i in user_hist_items:
                    continue
                items_rank.setdefault(i, 0)

                loc_weight = 1.0
                content_weight = 1.0
                created_time_weight = 1.0

                # 当前文章与该用户看的历史文章进行一个权重交互
                for loc, (j, click_time) in enumerate(user_item_time_list):
                    # 点击时的相对位置权重
                    loc_weight += 0.9 ** (len(user_item_time_list) - loc)
                    # 内容相似性权重
                    if emb_i2i_sim.get(i, {}).get(j, None) is not None:
                        content_weight += emb_i2i_sim[i][j]
                    if emb_i2i_sim.get(j, {}).get(i, None) is not None:
                        content_weight += emb_i2i_sim[j][i]

                    # 创建时间差权重
                    created_time_weight += np.exp(0.8 * np.abs(item_created_time_dict[i] - item_created_time_dict[j]))

                items_rank[i] += loc_weight * content_weight * created_time_weight * wuv
        except Exception as e:
            print(user_id)
    # 热度补全
    if len(items_rank) < recall_item_num:
        for i, item in enumerate(item_topk_click):
            if item in items_rank.items():  # 填充的item应该不在原来的列表中
                continue
            items_rank[item] = - i - 100  # 随便给个复数就行
            if len(items_rank) == recall_item_num:
                break

    items_rank = sorted(items_rank.items(), key=lambda x: x[1], reverse=True)[:recall_item_num]

    return items_rank


def get_user_hist_item_info_dict(all_click):
    # 获取user_id对应的用户历史点击文章类型的集合字典
    user_hist_item_typs = all_click.groupby('user_id')['category_id'].agg(set).reset_index()
    user_hist_item_typs_dict = dict(zip(user_hist_item_typs['user_id'], user_hist_item_typs['category_id']))

    # 获取user_id对应的用户点击文章的集合
    user_hist_item_ids_dict = all_click.groupby('user_id')['click_article_id'].agg(set).reset_index()
    user_hist_item_ids_dict = dict(zip(user_hist_item_ids_dict['user_id'], user_hist_item_ids_dict['click_article_id']))

    # 获取user_id对应的用户历史点击的文章的平均字数字典
    user_hist_item_words = all_click.groupby('user_id')['words_count'].agg('mean').reset_index()
    user_hist_item_words_dict = dict(zip(user_hist_item_words['user_id'], user_hist_item_words['words_count']))

    # 获取user_id对应的用户最后一次点击的文章的创建时间
    all_click_ = all_click.sort_values('click_timestamp')
    user_last_item_created_time = all_click_.groupby('user_id')['created_at_ts'].apply(
        lambda x: x.iloc[-1]).reset_index()

    max_min_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    user_last_item_created_time['created_at_ts'] = user_last_item_created_time[['created_at_ts']].apply(max_min_scaler)

    user_last_item_created_time_dict = dict(zip(user_last_item_created_time['user_id'],user_last_item_created_time['created_at_ts']))

    return user_hist_item_typs_dict, user_hist_item_ids_dict, user_hist_item_words_dict, user_last_item_created_time_dict

# click_trn_hist：训练集历史点击
# click_trn_last：最后一次点击
# recall_list_df：召回列表
# click_trn：训练集
# click_val/click_val_hist：验证集
# val_ans/click_val_last：验证集最后一次点击作为答案
# click_tst/click_tst_hist: 测试集 pd.read_csv(data_path+'testA_click_log.csv')

from  typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         if not nums:return []
#         n = len(nums)
#         store = {}
#         for i in range(n):
#             if target-nums[i] in store:
#                 return [store[target-nums[i]],i]
#             else:
#                 store[nums[i]] = i
#         return []

# solution = Solution()
# nums = [2,7,11,15]
# result = solution.twoSum(nums,9)
# print(result)
#
# class Solution:
#     def bubbleSort(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(len(nums)-i-1):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1] = nums[j+1],nums[j]
#         return nums
#
#     def selectSort(self,nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             minindex = i
#             for j in range(i+1,n):
#                 if nums[j]<nums[minindex]:
#                     minindex = j
#             nums[i],nums[minindex] = nums[minindex],nums[i]
#         return nums
#
#     def insertionSort(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             curNum,preIndex = nums[i+1],i
#             while preIndex>=0 and curNum<nums[preIndex]:
#                 nums[preIndex+1] = nums[preIndex]
#                 preIndex -=1
#             nums[preIndex+1] = curNum
#         return nums
#
#     def quickSort(self,nums:List[int]):
#         n = len(nums)
#         if n==1 :return nums
#         pivot = nums[0]
#         left = [nums[i] for i in range(1,n) if nums[i]<pivot]
#         right= [nums[j] for j in range(1,n) if nums[j]>=pivot]
#         return self.quickSort(left) + [pivot] + self.quickSort(right)
#
# import collections
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         queue = collections.deque()
#         queue.append(root)
#         res = []
#         while queue:
#             size = len(queue)
#             level = []
#             for _ in range(size):
#                 cur = queue.popleft()
#                 if not cur:
#                     continue
#                 level.append(cur.val)
#                 queue.append(cur.left)
#                 queue.append(cur.right)
#             if level:
#                 res.append(level)
#         return res

# 46
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first=0):
#             if first==n:
#                 res.append(nums[:])
#             for i in range(first,n):
#                 nums[first],nums[i] = nums[i],nums[first]
#                 backtrack(first+1)
#                 nums[i],nums[first] = nums[first],nums[i]
#
#         n = len(nums)
#         res = []
#         backtrack()
#         return res

class LinkNode:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next= self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = LinkNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size+=1
            if self.size>self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size-=1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)



    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
