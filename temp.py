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
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:return []
        n = len(nums)
        store = {}
        for i in range(n):
            if target-nums[i] in store:
                return [store[target-nums[i]],i]
            else:
                store[nums[i]] = i
        return []

solution = Solution()
nums = [2,7,11,15]
result = solution.twoSum(nums,9)
print(result)






