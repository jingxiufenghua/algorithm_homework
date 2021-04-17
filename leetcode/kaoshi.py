# [1,2,3,4,5,6]

# [4,5,6,1,2,3]
#didi 面试题，二分法
#自己当时主要考虑使用双指针，但是由于数组其实是有序的所以二分查找才更能利用数据的特性

from typing import List
# class Solution:
#     # 二分法
#     def minArray(self, numbers: List[int]) -> int:
#         n = len(numbers)
#         if not numbers:return -1
#         left,right = 0,n-1
#         while left<right:
#             mid = left + (right-left)//2
#             if numbers[mid]>numbers[right]:
#                 left = mid + 1
#             elif numbers[mid]<numbers[right]:
#                 right = mid
#             else:
#                 right-=1
#         return numbers[left]
#
# solution = Solution()
# nums = [1,2,1]
# result = solution.minArray(nums)
#
# print(result)

# 1. 蓄水

# class Solution:
#     def storeWater(self, bucket: List[int], vat: List[int]) -> int:
#         change = 0  # 升级了多少次桶
#         n = len(bucket)
#         full = [0 for _ in range(n)]  # 当前情况下，每个缸要装多少次能满足要求
#
#         for i in range(n):
#             # 如果桶是0，缸不是0，那么至少要把这个桶升级一次
#             if bucket[i] == 0:
#                 if vat[i] != 0:
#                     change += 1
#                     bucket[i] += 1
#                     full[i] = vat[i]
#             else:
#                 full[i] = ceil(vat[i] / bucket[i])
#
#         def arg_max(iter):
#             # 计算序列中的最大值及其下标，如果有多个也一并记录
#             if len(iter) == 0:
#                 return [-1]
#             m = iter[0]
#             p = [0]
#             for i in range(1, len(iter)):
#                 if iter[i] > m:
#                     p = [i]
#                     m = iter[i]
#                 elif iter[i] == m:
#                     p.append(i)
#             return p
#
#         which = arg_max(full)  # 需要倒水次数最多的缸是哪些
#         r = change + full[which[0]]
#         while True:
#             for w in which:
#                 bucket[w] += 1
#                 after = ceil(vat[w] / bucket[w])
#                 full[w] = after
#             imagine = arg_max(full)
#
#             temp = change + len(which) + full[imagine[0]]
#             if temp <= r:
#                 change += len(which)
#                 r = temp
#                 which = imagine
#             else:
#                 break
#         return r
#
# 作者：zesunlight
# 链接：https://leetcode-cn.com/problems/o8SXZn/solution/bi-sai-wan-liao-zuo-chu-lai-liao-ji-lu-y-54ag/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# from math import ceil
# class Solution:
#     def storeWater(self, bucket: List[int], vat: List[int]) -> int:
#         n,m = len(bucket),len(vat)
#         count = 0
#         for i in range(n):
#             if bucket[i] == 0 and vat[i]!=0:
#                 count+=1
#                 bucket[i] += 1
#
#         def multiple(bucket,vat):
#             multiple_list= []
#             for k,v in enumerate(bucket):
#                 if vat[k] == 0 :
#                     multiple_list.append(0)
#                 else:
#                     multiple_list.append(ceil(vat[k]/bucket[k]))
#             return multiple_list
#         multiple_list = multiple(bucket,vat)
#
#         def max_list(multiple_list):
#             max_multiple_list = []
#             for k,v in enumerate(multiple_list):
#                 if v == max(multiple_list):
#                     max_multiple_list.append(k)
#             return max_multiple_list
#
#         max_multiple_list = max_list(multiple_list)
#         while max_multiple_list:
#             for i in max_multiple_list:
#                 if vat[i]==0:
#                     mult = 0
#                 else:
#                     mult = ceil(vat[i]/(bucket[i]+1))
#                 if mult+1<=vat[i]:
#                     bucket[i] += 1
#                     count += 1
#                     multiple_list = multiple(bucket, vat)
#                     max_multiple_list = max_list(multiple_list)
#                     break
#                 else:
#                     return r
#
#
# solution = Solution()
# # nums =[3710,6067,2993,70,2340,2748,9385,3027,3456,5246,9739,1220,9539,9074,4729,7051,8462,6908,3649,9996,8890,2980,4350,7350,6344,6759,4420,269,9341,648,7737,8133,3717,2766,5807,4338,2077,5775,4905,7262,1258,613,3837,3475,437,3739,9814,4790,2075,7722,3290,5685,3499,6992,4421,934,6004,5763,3463,6138,8818,445,4778,4979,126,3969,2994,87,3739,8582,9559,8326,9132,257,8928,9147,1615,4665,9828,3925,6435,5326,836,519,298,600,5503,273,9580,5383,8966,4810,1386,7207,8060,678,8837,6946,1210,945]
# # vat = [6304,6509,4276,9645,6455,8167,9667,4385,8872,7889,9936,4413,9922,9894,8065,7627,9225,9907,7055,9996,9439,3351,9317,8363,9383,6850,4621,5389,9508,3391,9650,8363,8719,5594,8770,5403,7107,9941,9254,9355,4614,4640,4896,8759,4397,8441,9870,9906,2396,8092,6939,9432,8182,9090,8029,4930,7772,7066,7279,7778,9529,2947,6552,6930,5260,8470,8478,1371,9453,9767,9888,9964,9960,3990,9391,9377,3063,5374,9880,7684,7864,7078,2622,3754,617,9773,9415,8026,9883,5735,9233,6715,9105,7932,9178,1081,9340,7284,6621,1965]
# nums = [21,56]
# vat = [3230,8299]
# result = solution.storeWater(nums,vat)
# print(result)


# 5726. 数组元素积的符号
# class Solution:
#     def arraySign(self, nums: List[int]) -> int:
#         n = len(nums)
#
#         product = 1
#         for i in range(n):
#             product = product * nums[i]
#         if product>0:
#             return 1
#         elif product==0:
#             return 0
#         else:
#             return -1

5727. 找出游戏的获胜者
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n ==1 : return n
        n_list = [i for i in range(1,n+1)]
        i = 1
        index = 0
        # while len(n_list)>1:
        #     temp = n_list[(index+k)%len(n_list)]
        #     del n_list[(index+k-1)%len(n_list)]
        #     index = n_list.index(temp)

        while len(n_list)>1:
            id = (index+k-1)%len(n_list)
            del n_list[id]
            index = id

        return n_list[0]
solution = Solution()
result = solution.findTheWinner(6,5)
print(result)

# 5729. 求出 MK 平均值
# class MKAverage:
#     import numpy as np
#     def __init__(self, m: int, k: int):
#         self.bur = []
#         self.stack = []
#         self.m = m
#         self.k = k
#         self.size = 0
#     def addElement(self, num: int) -> None:
#         self.stack.append(num)
#         self.size = len(self.stack)
#
#     def calculateMKAverage(self) -> int:
#         if self.m>self.size:
#             return -1
#         else:
#             self.bur = self.stack[-self.m:]
#             self.bur.sort()
#             if len(self.bur)>self.k*2:
#                 res_list = self.bur[self.k:-self.k]
#                 return sum(res_list)//len(res_list)
#             else:
#                 return -1
#
# # Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(28,13)
# operation = ["calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement","calculateMKAverage","addElement","addElement","addElement","addElement","addElement","addElement","addElement","addElement"]
# nums = [[],[999],[998],[997],[996],[995],[994],[993],[992],[991],[],[989],[988],[987],[986],[985],[984],[983],[982],[981],[],[979],[978],[977],[976],[975],[974],[973],[972],[971],[],[969],[968],[967],[966],[965],[964],[963],[962],[961],[],[959],[958],[957],[956],[955],[954],[953],[952],[951],[],[949],[948],[947],[946],[945],[944],[943],[942],[941],[],[939],[938],[937],[936],[935],[934],[933],[932],[931],[],[929],[928],[927],[926],[925],[924],[923],[922],[921],[],[919],[918],[917],[916],[915],[914],[913],[912],[911],[],[909],[908],[907],[906],[905],[904],[903],[902],[901],[],[899],[898],[897],[896],[895],[894],[893],[892],[891],[],[889],[888],[887],[886],[885],[884],[883],[882],[881],[],[879],[878],[877],[876],[875],[874],[873],[872],[871],[],[869],[868],[867],[866],[865],[864],[863],[862],[861],[],[859],[858],[857],[856],[855],[854],[853],[852],[851],[],[849],[848],[847],[846],[845],[844],[843],[842],[841],[],[839],[838],[837],[836],[835],[834],[833],[832],[831],[],[829],[828],[827],[826],[825],[824],[823],[822],[821],[],[819],[818],[817],[816],[815],[814],[813],[812],[811],[],[809],[808],[807],[806],[805],[804],[803],[802],[801],[],[799],[798],[797],[796],[795],[794],[793],[792],[791],[],[789],[788],[787],[786],[785],[784],[783],[782],[781],[],[779],[778],[777],[776],[775],[774],[773],[772],[771],[],[769],[768],[767],[766],[765],[764],[763],[762],[761],[],[759],[758],[757],[756],[755],[754],[753],[752],[751],[],[749],[748],[747],[746],[745],[744],[743],[742],[741],[],[739],[738],[737],[736],[735],[734],[733],[732],[731],[],[729],[728],[727],[726],[725],[724],[723],[722],[721],[],[719],[718],[717],[716],[715],[714],[713],[712],[711],[],[709],[708],[707],[706],[705],[704],[703],[702],[701],[],[699],[698],[697],[696],[695],[694],[693],[692],[691],[],[689],[688],[687],[686],[685],[684],[683],[682],[681],[],[679],[678],[677],[676],[675],[674],[673],[672],[671],[],[669],[668],[667],[666],[665],[664],[663],[662],[661],[],[659],[658],[657],[656],[655],[654],[653],[652],[651],[],[649],[648],[647],[646],[645],[644],[643],[642],[641],[],[639],[638],[637],[636],[635],[634],[633],[632],[631],[],[629],[628],[627],[626],[625],[624],[623],[622],[621],[],[619],[618],[617],[616],[615],[614],[613],[612],[611],[],[609],[608],[607],[606],[605],[604],[603],[602],[601],[],[599],[598],[597],[596],[595],[594],[593],[592],[591],[],[589],[588],[587],[586],[585],[584],[583],[582],[581],[],[579],[578],[577],[576],[575],[574],[573],[572],[571],[],[569],[568],[567],[566],[565],[564],[563],[562],[561],[],[559],[558],[557],[556],[555],[554],[553],[552],[551],[],[549],[548],[547],[546],[545],[544],[543],[542],[541],[],[539],[538],[537],[536],[535],[534],[533],[532],[531],[],[529],[528],[527],[526],[525],[524],[523],[522],[521],[],[519],[518],[517],[516],[515],[514],[513],[512],[511],[],[509],[508],[507],[506],[505],[504],[503],[502],[501],[],[499],[498],[497],[496],[495],[494],[493],[492],[491],[],[489],[488],[487],[486],[485],[484],[483],[482],[481],[],[479],[478],[477],[476],[475],[474],[473],[472],[471],[],[469],[468],[467],[466],[465],[464],[463],[462],[461],[],[459],[458],[457],[456],[455],[454],[453],[452],[451],[],[449],[448],[447],[446],[445],[444],[443],[442],[441],[],[439],[438],[437],[436],[435],[434],[433],[432],[431],[],[429],[428],[427],[426],[425],[424],[423],[422],[421],[],[419],[418],[417],[416],[415],[414],[413],[412],[411],[],[409],[408],[407],[406],[405],[404],[403],[402],[401],[],[399],[398],[397],[396],[395],[394],[393],[392],[391],[],[389],[388],[387],[386],[385],[384],[383],[382],[381],[],[379],[378],[377],[376],[375],[374],[373],[372],[371],[],[369],[368],[367],[366],[365],[364],[363],[362],[361],[],[359],[358],[357],[356],[355],[354],[353],[352],[351],[],[349],[348],[347],[346],[345],[344],[343],[342],[341],[],[339],[338],[337],[336],[335],[334],[333],[332],[331],[],[329],[328],[327],[326],[325],[324],[323],[322],[321],[],[319],[318],[317],[316],[315],[314],[313],[312],[311],[],[309],[308],[307],[306],[305],[304],[303],[302],[301],[],[299],[298],[297],[296],[295],[294],[293],[292],[291],[],[289],[288],[287],[286],[285],[284],[283],[282],[281],[],[279],[278],[277],[276],[275],[274],[273],[272],[271],[],[269],[268],[267],[266],[265],[264],[263],[262],[261],[],[259],[258],[257],[256],[255],[254],[253],[252],[251],[],[249],[248],[247],[246],[245],[244],[243],[242],[241],[],[239],[238],[237],[236],[235],[234],[233],[232],[231],[],[229],[228],[227],[226],[225],[224],[223],[222],[221],[],[219],[218],[217],[216],[215],[214],[213],[212],[211],[],[209],[208],[207],[206],[205],[204],[203],[202],[201],[],[199],[198],[197],[196],[195],[194],[193],[192],[191],[],[189],[188],[187],[186],[185],[184],[183],[182],[181],[],[179],[178],[177],[176],[175],[174],[173],[172],[171],[],[169],[168],[167],[166],[165],[164],[163],[162],[161],[],[159],[158],[157],[156],[155],[154],[153],[152],[151],[],[149],[148],[147],[146],[145],[144],[143],[142],[141],[],[139],[138],[137],[136],[135],[134],[133],[132],[131],[],[129],[128],[127],[126],[125],[124],[123],[122],[121],[],[119],[118],[117],[116],[115],[114],[113],[112],[111],[],[109],[108],[107],[106],[105],[104],[103],[102],[101],[],[99],[98],[97],[96],[95],[94],[93],[92],[91],[],[89],[88],[87],[86],[85],[84],[83],[82],[81],[],[79],[78],[77],[76],[75],[74],[73],[72],[71],[],[69],[68],[67],[66],[65],[64],[63],[62],[61],[],[59],[58],[57],[56],[55],[54],[53],[52],[51],[],[49],[48],[47],[46],[45],[44],[43],[42],[41],[],[39],[38],[37],[36],[35],[34],[33],[32],[31],[],[29],[28],[27],[26],[25],[24],[23],[22],[21],[],[19],[18],[17],[16],[15],[14],[13],[12],[11],[],[9],[8],[7],[6],[5],[4],[3],[2]]
# for k,v in enumerate(operation):
#     if v == "calculateMKAverage":
#         print(obj.calculateMKAverage())
#     elif v == "addElement":
#         obj.addElement(nums[k][0])


# obj.addElement(3)       #// 当前元素为 [3]
# obj.addElement(1)      #// 当前元素为 [3,1]
# obj.calculateMKAverage() #// 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
# obj.addElement(12)       #// 当前元素为 [3,1,10]
# obj.addElement(5)       #// 当前元素为 [3,1,10]
# obj.addElement(3)       #// 当前元素为 [3,1,10]
# obj.addElement(4)       #// 当前元素为 [3,1,10]
# print(obj.calculateMKAverage())#// 最后 3 个元素为 [3,1,10]
#                           #// 删除最小以及最大的 1 个元素后，容器为 [3]
#                           #// [3] 的平均值等于 3/1 = 3 ，故返回 3
# obj.addElement(5)        #// 当前元素为 [3,1,10,5]
# obj.addElement(5)      #// 当前元素为 [3,1,10,5,5]
# obj.addElement(5)       #// 当前元素为 [3,1,10,5,5,5]
# obj.calculateMKAverage() #// 最后 3 个元素为 [5,5,5]
#                           #// 删除最小以及最大的 1 个元素后，容器为 [5]
#                           #// [5] 的平均值等于 5/1 = 5 ，故返回 5


