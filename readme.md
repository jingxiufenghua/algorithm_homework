今日刷题情况：
![image](img/刷题情况.png)

目标：6个月内 1500题，全站排名：1000名以内   参加微软、google面试

fighting！！！

个人刷题总结：

滑动窗口模板:
《挑战程序设计竞赛》这本书中把滑动窗口叫做「虫取法」，我觉得非常生动形象。因为滑动窗口的两个指针移动的过程和虫子爬动的过程非常像：前脚不动，把后脚移动过来；后脚不动，把前脚向前移动。

    def findSubArray(nums):
        N = len(nums) # 数组/字符串长度
        left, right = 0, 0 # 双指针，表示当前遍历的区间[left, right]，闭区间
        sums = 0 # 用于统计 子数组/子区间 是否有效，根据题目可能会改成求和/计数
        res = 0 # 保存最大的满足题目要求的 子数组/子串 长度
        while right < N: # 当右边的指针没有搜索到 数组/字符串 的结尾
            sums += nums[right] # 增加当前右边指针的数字/字符的求和/计数
            while 区间[left, right]不符合题意：# 此时需要一直移动左指针，直至找到一个符合题意的区间
                sums -= nums[left] # 移动左指针前需要从counter中减少left位置字符的求和/计数
                left += 1 # 真正的移动左指针，注意不能跟上面一行代码写反
            # 到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
            res = max(res, right - left + 1) # 需要更新结果
            right += 1 # 移动右指针，去探索新的区间
        return res
滑动窗口中用到了左右两个指针，它们移动的思路是：以右指针作为驱动，拖着左指针向前走。右指针每次只移动一步，而左指针在内部 while 循环中每次可能移动多步。右指针是主动前移，探索未知的新区域；左指针是被迫移动，负责寻找满足题意的区间。
作者：fuxuemingzhu
来源：力扣（LeetCode）

4.22日

304\307\363 一起做 前缀和

针对不同的题目，我们有不同的方案可以选择（假设我们有一个数组）：

数组不变，求区间和：「前缀和」、「树状数组」、「线段树」

多次修改某个数，求区间和：「树状数组」、「线段树」

多次整体修改某个区间，求区间和：「树状数组」、「线段树」

多次将某个区间变成同一个数，求区间和：「线段树」

「线段树」代码很长，而且常数很大，复杂度表现不算很好。我们只有在不得不用的时候才考虑「线段树」。

作者：AC_OIer

307「树状数组」的代码 当作模板

    class NumArray {
    int[] tree;
    int lowbit(int x) {
        return x & -x;
    }
    int query(int x) {
        int ans = 0;
        for (int i = x; i > 0; i -= lowbit(i)) ans += tree[i];
        return ans;
    }
    void add(int x, int u) {
        for (int i = x; i <= n; i += lowbit(i)) tree[i] += u;
    }

    int[] nums;
    int n;
    public NumArray(int[] _nums) {
        nums = _nums;
        n = nums.length;
        tree = new int[n + 1];
        for (int i = 0; i < n; i++) add(i + 1, nums[i]);
    }
    
    public void update(int i, int val) {
        add(i + 1, val - nums[i]);
        nums[i] = val;
    }
    
    public int sumRange(int l, int r) {
        return query(r + 1) - query(l);
    }
    }
模板：

    // 上来先把三个方法写出来
    {
        int[] tree;
        int lowbit(int x) {
            return x & -x;
        }
        // 查询前缀和的方法
        int query(int x) {
            int ans = 0;
            for (int i = x; i > 0; i -= lowbit(i)) ans += tree[i];
            return ans;
        }
        // 在树状数组 x 位置中增加值 u
        void add(int x, int u) {
            for (int i = x; i <= n; i += lowbit(i)) tree[i] += u;
        }
    }

    // 初始化「树状数组」，要默认数组是从 1 开始
      {
        for (int i = 0; i < n; i++) add(i + 1, nums[i]);
    }

    // 使用「树状数组」：
    {   
        void update(int i, int val) {
            // 原有的值是 nums[i]，要使得修改为 val，需要增加 val - nums[i]
            add(i + 1, val - nums[i]); 
            nums[i] = val;
        }
        
        int sumRange(int l, int r) {
            return query(r + 1) - query(l);
        }
    }

