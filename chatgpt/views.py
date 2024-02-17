from openai import OpenAI

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)

@csrf_exempt
def openai_request_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt', '')
            
            response = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":prompt}])
            
            content = response.choices[0].message.content

            return JsonResponse({'success': True, 'generated_text': content})
        
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': f'Invalid JSON format: {str(e)}'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Only POST requests are allowed.'}, status=405)
