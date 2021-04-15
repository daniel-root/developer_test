from rest_framework import viewsets

from .serializers import SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer, SurveyUserAnswerSerializer
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative, SurveyUserAnswer
# Create your views here.
class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer