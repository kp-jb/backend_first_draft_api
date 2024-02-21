from openai import OpenAI

from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def openai_request_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt', '')
            
            # response = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":prompt}])
            
            # content = response.choices[0].message.content

            # return JsonResponse({'success': True, 'generated_text': content})

            return JsonResponse({
                "success": True,
                "generated_text": "Dear Hiring Manager,\n\nI am writing to express my interest in the Software Engineer Intern position at CooperSurgical. With a strong background in full-stack software development and a passion for innovative problem-solving, I am excited about the opportunity to contribute to your dynamic product development team.\n\nIn my most recent role as a Software Developer, I have honed my skills in JavaScript and Python to create impactful projects such as A-MAZE-ING, cocktail lover, and systematic mutagenesis of TFIIH subunit p52/Tfb2. These projects demonstrate my ability to develop software application features, troubleshoot and fault find software defects, and document designs effectively.\n\nAs a current Computer Science student entering my Senior year, I am eager to apply my knowledge in cloud applications architecture, web application design, and programming languages to assist with the product development of SaaS applications at CooperSurgical. I am familiar with technologies such as C#, HTML5, CSS3, JavaScript, and AWS, and I am excited to learn more about DevOps practices and continuous integration/continuous deployment.\n\nI am confident that my technical skills, attention to detail, and ability to work independently make me a strong candidate for this internship opportunity. I am enthusiastic about the prospect of working on relevant engineering projects, prototyping software applications, and contributing to the growth and success of CooperSurgical.\n\nThank you for considering my application. I look forward to the opportunity to discuss how my experiences align with the responsibilities and qualifications for the Software Engineer Intern position at CooperSurgical.\n\nSincerely,\nJacob Bassett"
              });
        
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': f'Invalid JSON format: {str(e)}'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Only POST requests are allowed.'}, status=405)
