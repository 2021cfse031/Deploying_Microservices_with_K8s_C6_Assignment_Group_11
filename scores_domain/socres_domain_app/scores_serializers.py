from rest_framework import serializers
from socres_domain_app.scores_models import Scores

class ScoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = '__all__'
