class Page:
    def __init__(self,current_page,total_count,per_page,max_page):
        self.current_page = current_page #获取当前页码
        self.total_count = total_count   #获取数据的总长度
        self.per_page = per_page         #设置每页显示多少条数据
        self.max_page = max_page         #设置页码范围，即显示当前页码的前几页和后几页
    
    @property
    def start(self):
        return (self.current_page-1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    #'start'和'end'的用法：比如要展示的数据总量是个列表LIST，那么每页展示对应的数据应该是obj = LIST[self.start:self.end]，然后把obj渲染进去模板就行了

    @property
    def total_page(self):
        total_page,y = divmod(self.total_count,self.per_page)
        if y:
            total_page += 1
            return total_page


    def page_setting(self,base_url):
        if self.current_page > self.total_page:
            self.current_page = self.total_page
       #如果当前页大于总页数，那就限制当前页等于总页数 
        if self.max_page > self.total_page:
            self.max_page = self.total_page

        half_max_page = self.max_page // 2

        start_page = self.current_page - half_max_page
        end_page = self.current_page + half_max_page
        #起始页和结束页


        if start_page <= 1:
            start_page = 1
            end_page = self.max_page
        #如果起始页比1还小，那就定起始页显示为1，结束页为最大显示页数11，也就是【1、2、3、4、5、6、7、8、9、10、11】，否则会出现负数页数显示在页面上
        if end_page > self.total_page:
            end_page = self.total_page
            start_page = self.total_page - self.max_page +1
        #如果结束页比总页数还大，那就定结束页为最后一页，起始页为总页数前10页，比如说总页数是20，那就是【10、11、12、13、14、15、16、17、18、19、20】，这是防止出现20页以后还出现更大的页码

        page_str = []
        #创建空列表用于接收插入的html标签

        page_str.append('<div class="page"><a href="%s?p=1">首页</a></div>'%(base_url))
        #用%s格式化传入的网址

        if self.current_page <= 1:
            page_str.append('<div class="page hide"><a href="%s?p=%s">上一页</a></div>'%(base_url,self.current_page-1))
        else:
            page_str.append('<div class="page"><a href="%s?p=%s">上一页</a></div>'%(base_url,self.current_page-1))
        #这里定义如果当前页小于等于1的时候，隐藏掉“上一页”这个按钮。至于隐藏的样式，大家可以自己在模板中设置css

        for i in range(start_page,end_page):
            if i == self.current_page:
                temp = '<div class="page active"><a href="%s?p=%s">%s</a></div>' %(base_url,i,i)
            else:
                temp = '<div class="page"><a href="%s?p=%s">%s</a></div>' %(base_url,i,i)

            page_str.append(temp)
        #这里的for循环才是关键，可以看到range的范围是我们计算好的，比如显示上下5页，里面的start_page和end_page是是表示显示前多少页后多少页的，这个不用你计算，上面都已经封装好了

        if self.current_page >= self.total_page:
            page_str.append('<div class="page hide"><a href="/url_list/?p=%s">下一页</a></div>'%(self.current_page+1))
        else:
            page_str.append('<div class="page"><a href="/url_list/?p=%s">下一页</a></div>'%(self.current_page+1))
        #这里和“上一页”的显示原理一样

        page_str.append('<div class="page"><a href="/url_list/?p=%s">尾页</a></div>'%(self.total_page))

        page_html = "".join(page_str)
        #最后拼接成字符串，不然在网页上显示会有很多”[']之类的符号
        return page_html
        #这里返回的page_html是已经包含了以上功能的结果，直接在你views视图中，用render渲染它就可以了，当然，你还要找个变量把它接收一下，这样会比较稳妥
