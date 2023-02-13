from django.urls import path 
from .views import index,bus,routes,busRoutes,available_bus_for_certain_routes
# ,routes,busRoutes,

urlpatterns = [
    path('', index, name="index"),
    path("buses/", bus, name="bus"),
    path("buses/<int:pk>/",busRoutes, name="busRoute"),
    path("routes/", routes ,name="route"),
    path('routes/<int:pk>/', available_bus_for_certain_routes, name="routesbus")
]
