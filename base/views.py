from django.shortcuts import render


article_data = [

{
'id':1,
'title':'All About India',
'desc':'India is a diverse country with rich culture and heritage.',
'image':'https://picsum.photos/id/1015/400/250'
},

{
'id':2,
'title':'All About Karnataka',
'desc':'Karnataka is famous for Mysore Palace and IT industry.',
'image':'https://picsum.photos/id/1011/400/250'
},

{
'id':3,
'title':'All About Asia',
'desc':'Asia is the largest continent with many cultures.',
'image':'https://picsum.photos/id/1024/400/250'
},

{
'id':4,
'title':'All About Telangana',
'desc':'Telangana is known for Hyderabad and Charminar.',
'image':'https://picsum.photos/id/1035/400/250'
},

{
'id':5,
'title':'All About Madhya Pradesh',
'desc':'MP is called the heart of India with forests and temples.',
'image':'https://picsum.photos/id/1043/400/250'
}

]



def Home(request):

    return render(request,'home.html',{'data':article_data})


def News(request):

    return render(request,'news.html',{'data':article_data})


def Events(request):

    event_data = [

        {
            "title": "Python Workshop 2026",
            "date": "April 5, 2026",
            "location": "Bangalore",
            "image": "https://picsum.photos/id/180/600/300",
            "desc": "Learn Python basics, functions, Django intro and build mini projects."
        },

        {
            "title": "Django Bootcamp",
            "date": "April 12, 2026",
            "location": "Hyderabad",
            "image": "https://picsum.photos/id/1/600/300",
            "desc": "Hands-on Django training with real-world website development."
        },

        {
            "title": "AI & Machine Learning Seminar",
            "date": "April 20, 2026",
            "location": "Chennai",
            "image": "https://picsum.photos/id/20/600/300",
            "desc": "Understand AI trends, ChatGPT usage, and career opportunities."
        },

        {
            "title": "Web Development Masterclass",
            "date": "April 28, 2026",
            "location": "Mumbai",
            "image": "https://picsum.photos/id/48/600/300",
            "desc": "Learn HTML, CSS, JavaScript and React basics in one session."
        }

    ]

    return render(request, "events.html", {"events": event_data})


def About(request):

    return render(request,'about.html')


def read(request,id):

    article=None

    for i in article_data:

        if i['id']==id:

            article=i

    return render(request,'read.html',{'data':article})