# 手动双面打印pdf

## 需求
组里的打印机双面打印会卡纸，只能手动单面打印两次实现双面打印的效果。但是打印完奇数页后，需要从后往前打印偶数页，否则就得手动reverse打印出来的奇数页……太麻烦了

## 依赖
```shell
$ pip install pdfrw
```

## 使用方法
```shell
$ python manualprintPDF.py <path/to/input/pdf/file> <pah/to/outout/pdf/file>
# example: python manualprintPDF.py ./demo.pdf ./output.pdf
```
**效果**：将原pdf文件分割成两个pdf文件。其中奇数页正序排列，偶数页倒序排列。

**ps:** 当然考虑到有的文档是奇数页的，在最后插入了一个空白页凑成偶数页。
