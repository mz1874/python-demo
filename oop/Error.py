
if __name__ == '__main__':

    try:
        a = 10
        raise Exception("手动抛出异常")
        b = a / 0
    except (ValueError,IndexError):
        print("error")
        pass
    except Exception as result :
        print(result)
    else:
        print("没有异常会执行的代码")
        pass
    finally:
        print("最终执行的代码")
        pass