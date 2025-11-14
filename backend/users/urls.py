from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', views.UserViewSet)

# This automatically provides following urls:
#--------------------------------------------
# Method	    URL	         Action
#--------------------------------------------
# GET	      /users/	      list
# GET	    /users/<id>/	 retrieve
# POST	      /users/	      create
# PUT	    /users/<id>/	  update
# PATCH	    /users/<id>/   partial_update
# DELETE	/users/<id>/	 destroy
# POST	    /users/login/	  login
#--------------------------------------------

urlpatterns = router.urls