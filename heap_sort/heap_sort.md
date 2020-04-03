#### 完全二叉树
所谓完全二叉树是指，如果二叉树的第k层的叶子节点没有填满，则每个节点都以广度优先遍历的方式向叶子节点添加数据。

#### 数组里的数据如果填充到二叉树里面
数组的数据从左至右，分别从二叉树的根节点，向下每层从左至右填充，直到将数据填充完毕

#### 堆
堆是由完全二叉树构成，分为：大顶堆和小顶堆
大顶堆：父节点的值大于左右子节点的值
小顶堆：父节点的值小于子节点的值
所以，如果想找出数组里最大的值，直接构建一个大顶堆就可以了
同理，如果想找出数组里最小的值，直接构建一个小顶堆就可以了

#### 堆排序
顾名思义，就是用构建堆的方式来进行排序，类似于冒泡排序，冒泡排序是根据冒泡的方法来不断找出数组里最大的值；
同理，堆排序就是用构建堆的方法来不断找出数组里最大的值。
所以堆排序一共可以分为三步：
- 第一步，将数组看成一个堆，用数组构建大顶堆，构建完毕后，这个时候，数组里的最大值就跑到了数组index为0的位置；
- 第二步，将数组的最大值移动到数组的末尾，末尾的值移动到数组的开始；
- 第三步，剪去末尾节点【其实可以不用实际的剪去，只要将数组的长度减去1，作为剩下的数组就行】，将剩下的数组留下，回到第一步