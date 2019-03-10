# thanos-py

타노스가 당신의 컴퓨터에 도착했어요! 그는 당신의 파일을 파괴하러 왔어요..!
그는 당신의 파일중 절반을 건틀렛과 함께 손을 튕겨서 날려버릴거에요..!
당신이 정말 운이좋다면, 그는 별 중요하지 않은 파일들만 날려버리겠죠? 행운을 빌어요 :D

## Install

`pip install thanos-py`

## Usage

-   remove root dir : `thanos-py /`
-   another location : `thanos-py /Your/Own/Location/`

## Technical Details
-   그래요, 이건 파일을 지워줘요 [ 이 패키지가 무엇을 하는지 잘 모르는 사람을 위하여 (찡긋)]
-   이것은 `os.remove()` 함수를 통해서 파일을 지워요
-   이것은 명령이 실행된 디렉토리의 모든 하위디렉토리를 돌아다녀요. 그러니 폴더안에 있는 파일도 지워질 수 있어요
-   이것이 정확하게 2/1개의 파일을 지울지는 저도 잘 모르겠어요 (야!!)
```py
search(target)
random.shuffle(filelist)
print("[😈] Death note is ready...")
filecount = len(filelist)
for i in range(0, int(filecount / 2)):
    deletelist.append(filelist[i])
    print (deletelist[i])
for i in range(filecount + 1):
    os.remove(str(deletelist[i]))
	// logic to delete the file
}
```
