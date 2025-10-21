from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    """
    提供page目录下的单页应用
    """
    # 读取index.html文件内容
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/html')
    except FileNotFoundError:
        return HttpResponse("Page not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

def section(request, num):
    """Display section content based on section number"""
    if num == 1:
        return HttpResponse("""
            <h1>The Importance of Reading</h1>
            <p>Reading is one of the most fundamental skills in human development. It opens doors to knowledge, imagination, and understanding. Through reading, we can explore different cultures, learn new concepts, and expand our vocabulary. Regular reading improves cognitive function and enhances critical thinking abilities.</p>
            <p>Studies show that people who read regularly have better memory retention and analytical skills. Reading fiction can increase empathy by allowing us to experience life from different perspectives, while non-fiction provides valuable information about the world around us.</p>
        """)
    elif num == 2:
        return HttpResponse("""
            <h1>Benefits of Exercise</h1>
            <p>Regular physical activity is essential for maintaining good health and well-being. Exercise helps control weight, combat health conditions and diseases, improve mood, boost energy, and promote better sleep. The American Heart Association recommends at least 150 minutes of moderate-intensity aerobic activity per week.</p>
            <p>Different types of exercise provide various benefits. Cardiovascular exercises like running and swimming improve heart health, while strength training builds muscle mass and bone density. Flexibility exercises such as yoga enhance mobility and reduce injury risk.</p>
        """)
    elif num == 3:
        return HttpResponse("""
            <h1>Technology in Modern Education</h1>
            <p>The integration of technology in education has transformed traditional learning methods. Digital tools provide access to vast educational resources, enable personalized learning experiences, and facilitate collaboration among students and teachers worldwide. Online platforms offer interactive content that makes learning more engaging and effective.</p>
            <p>Educational technology includes learning management systems, virtual classrooms, educational apps, and AI-powered tutoring systems. These tools help bridge educational gaps and provide equal learning opportunities regardless of geographical location or socioeconomic status.</p>
        """)
    else:
        return HttpResponse(f"<h1>Section {num}</h1><p>Content for section {num} not found.</p>")