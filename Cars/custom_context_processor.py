from .models import CarPoster


def get_carposter(request):
    return {"fresh_new": CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')[:6],
            "fresh_new_1_3": CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')[:3],
            "fresh_new_3_6": CarPoster.objects.filter(status__exact='a').all().order_by('-poster_date')[3:6],
            "highest_price_1_3": CarPoster.objects.filter(status__exact='a').all().order_by('-car_poster_price')[:3],
            "highest_price_3_6": CarPoster.objects.filter(status__exact='a').all().order_by('-car_poster_price')[3:6],
            "most_liked_1_3": CarPoster.objects.filter(status__exact='a').all().order_by('-sellers_likes')[:3],
            "most_liked_3_6": CarPoster.objects.filter(status__exact='a').all().order_by('-sellers_likes')[3:6],
            "number_of_cars": CarPoster.objects.filter(status__exact='a').count()}