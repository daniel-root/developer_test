from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DEFAULT_STRING_LENGTH = 256
class Survey(models.Model):
    name = models.CharField(max_length=DEFAULT_STRING_LENGTH,default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

class SurveyQuestion(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,default=None)
    survey_question_text = models.CharField(max_length=DEFAULT_STRING_LENGTH,default=None)

    def __str__(self):
        return self.survey_question_text

class SurveyQuestionAlternative(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,default=None)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE,default=None)
    survey_question_alternative_text = models.CharField(max_length=DEFAULT_STRING_LENGTH,default=None)

    def __str__(self):
        return self.survey_question_alternative_text

class SurveyUserAnswer(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,default=None)
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE,default=None)
    survey_question_alternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return '{}|{}'.format(self.user.username, self.survey_question_alternative.survey_question_alternative_text)