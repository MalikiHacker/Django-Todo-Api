from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo

"""
Nous importons des sérialiseurs depuis DRF ainsi que notre fichier models.py. Ensuite, nous créons une classe TodoSerializer. 
Le format ici est très similaire à la façon dont nous créons des classes de modèle.
Nous spécifions le modèle à utiliser et les champs spécifiques que nous souhaitons exposer.
N'oubliez pas que l'identifiant est créé automatiquement par Django,
nous n'avons donc pas à le définir dans notre modèle Todo, mais nous l'utiliserons dans notre vue détaillée.
"""