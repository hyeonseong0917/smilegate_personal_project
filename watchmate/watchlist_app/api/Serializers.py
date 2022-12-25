from rest_framework import serializers
from watchlist_app.models import WatchList, GamePlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Review
        exclude=('watchlist',)
        # fields="__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    


    class Meta:
        model=WatchList
        fields="__all__"
        
class GamePlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializer(many=True, read_only=True)
    class Meta:
        model=GamePlatform
        fields="__all__"
        
    


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Movie name must be at least 2 characters")
    

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
 
#     description=serializers.CharField()
#     active=serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name', instance.name)
#         instance.description=validated_data.get('description', instance.description)
#         instance.active=validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError('Movie name cannot be the same as description')
#         else:
#             return data            

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Movie name must be at least 2 characters")
    #     return value
               
        

