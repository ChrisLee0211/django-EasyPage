# django-EasyPage
5 steps to make your page become what you need

只要把utils文件夹，放到项目的根目录下即可。

示例：

在views.py中：
  from utils import EasyPage
  LIST = []
  for i in range(209):
    LIST.append(i)

  def url_list(request):
      current_page = request.GET.get('p',1)
      current_page = int(current_page)
      count_long = len(LIST)
    
      obj = EasyPage.Page(current_page,len(LIST),10,11)

      data = LIST[obj.start:obj.end]

      page_html = obj.page_setting("/url_list/")
        
      return render(request,'url_list.html',{'li':data,'page_html':page_html})
      
 具体参数含义，在EasyPage.py里面已经全部表明清楚了，只需要传入自己想要的参数，就会自动生成页码内容，并打包成一个page_html对象输出，最后渲染它就行了
