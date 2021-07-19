from .models import Kullanici, Magaza, Yorum


# set this context processor in settings.py

# ** After logging out, this Kullanici query
# ** causes DoesNotExist exception.
def kullanici_slug(request):
    try:
        curr_user = request.user.id
        k_slug = Kullanici.objects.get(id=curr_user).slug
        return {
            "k_slug": k_slug
        }
    except:
        return {
            "k_slug": "AnonymousUser"
        }


def isMagaza(request):
    try:
        curr_user = request.user
        curr_magaza = Magaza.objects.get(user=curr_user)

        if curr_magaza:
            return {
                "isMagaza": True
            }

    except:
        return {
            "isMagaza": False
        }
