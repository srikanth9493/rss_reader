from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,View,TemplateView
from  .models import  RSS_Reader_Model
from .forms import Rss_Form
from django.shortcuts import redirect,reverse

import  feedparser


class Home_View(TemplateView):
    template_name = "reader/home.html"
    form_class = Rss_Form()
    def get(self,request):
        form=Rss_Form();
        return  render(request,'reader/home.html',{'form':form})

    def post(self, request):
        form=Rss_Form(request.POST)
        url=request.POST.get('url')
            # print(url)
        return redirect("/rss/feeds")







def  Feed_View(request,**args):
    template_name = "reader/feeds.html"
    if request.method=="POST":
        url=request.POST.get('url')
        data={}
        feed = feedparser.parse(url)
        print(args)
        post=[]
        for i in range(len(feed)):
            # published = date(pub_date[0], pub_date[1], pub_date[2])

            x=feed['entries'][i]
            # print(x)
            data={
                'title': feed['entries'][i].title,
                'summary': feed['entries'][i].summary,
                'link': feed['entries'][i].link,
                # 'content': feed['entries'][i].content,
                # 'date': published
            }
            try:
                data['image']= x['media_thumbnail'][0]['url']
            except Exception:
                pass


            post.append(
                    data
            )


        data["feed"]=post
        return render(request,"reader/feeds.html",data)

