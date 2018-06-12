
is_exit = True      # 判断退出的标志位
# is_login = False    # 判断是否已经登录,默认未登录

def login_type(is_type):         # 装饰器参数，判断以每个页面以哪种方式进行验证登录


    def login(func):         # 装饰器函数

        with open('user info', 'r') as file1:   # 文件中的内容是验证是否登录的
            is_login = file1.read()

        def inner():
            nonlocal is_login     # 因为当密码输入正确的时候，需要修改登录文件中的内容，所以提前声明
            if is_login == 'false':
                if is_type == 'weixin':          # 判断某个页面是以什么方式进行登录的，然后在相应的文件中提取账户密码
                    with open('weixin', 'r') as file:
                        user_info = eval(file.read())      # 将文件中的内容以字典的形式拿出
                elif is_type == 'jindong':
                    with open('jindong', 'r') as file:
                        user_info = eval(file.read())
    ####

                your_id = input('Please enter your ID:').strip()
                your_passwd = input('Please enter your password:').strip()

                if your_id in user_info and your_passwd == user_info[your_id]:   # 验证账号密码是否正确
                    func()         # 密码正确执行函数
                    is_login = 'true'
                    with open('user info', 'w') as file2:    # 登录成功，将结果记入验证登录文件
                        file2.write(is_login)
                else:
                    print('id or password is error!')

            elif is_login == 'true':   # 如果已经登录过，直接执行相应的页面函数
                # print('ok')
                func()

        # is_login = little_is_login   # 将little_is_login的值再次赋给

        return inner

    return login

@login_type('jindong')
def home():  # home page source function
    print('welcome to home page!')

@login_type('weixin')
def book():   # book page source function
    print('welcome to book page!')

@login_type('jindong')
def foot():   # foot page source function
    print('welcome to foot page!')



while is_exit == True:
    show_pages()       # 展示全部的页面信息
    user_choice = input('Which page do you want to go to?')
    if user_choice == '1':
        home()        # 如果输入相应的序号就执行相应的函数
    elif user_choice == '2':
        book()
    elif user_choice == '3':
        foot()
    elif user_choice == 'exit':      # 如果输入exit，退出程序
        print('welcome again!')
        is_exit = False
    elif len(user_choice) == 0:
        continue
    else:
        print('input error!')
        continue



