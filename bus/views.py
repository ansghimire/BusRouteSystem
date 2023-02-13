from django.shortcuts import render
from django.db.models import Count
from .models import Bus, Route, TimeAssignModel
import django_tables2 as tables
from django_tables2.utils import A




class BusTable(tables.Table):
    bus_name = tables.Column()
    bus_number = tables.Column()
    num_of_routes = tables.LinkColumn("busRoute", args=[A("pk")])


class RouteTable(tables.Table):
    route = tables.Column()
    route_number = tables.Column()
    num_of_bus_run_this_route = tables.LinkColumn("routesbus", args=[A("pk")])

class BusRouteTable(tables.Table):
    route = tables.Column()
    route_number =tables.Column()
    from_time = tables.Column()
    to_time = tables.Column()

class AvailablebusForCertainRoutesTable(tables.Table):
    bus = tables.Column()
    bus_number =tables.Column()
    from_time = tables.Column()
    to_time = tables.Column()


def index(request):
    return render(request, 'bus/index.html')


def bus(request):
    qs = Bus.objects.annotate(num_of_routes=Count('routes'))
    # context = {'buses': qs}
    table = BusTable(qs)
    return render(request, 'bus/bus.html', {"table":table})



def busRoutes(request, pk=None):
    routes_qs = TimeAssignModel.objects.filter(bus = pk) 
    # context = {'available_routes':routes_qs}
    table = BusRouteTable(routes_qs)
    return render(request, 'bus/particularbusRoute.html',{"table":table, "items": routes_qs.count() })
    


def routes(request):
    qs = Route.objects.annotate(num_of_bus_run_this_route=Count(('bus')))
    # context = {'routes': qs}
    table = RouteTable(qs)
    return render(request, 'bus/routes.html', {"table":table})


def available_bus_for_certain_routes(request, pk=None):
    qs = TimeAssignModel.objects.filter(route = pk)
    # context = {'available_bus_in_this_particular_routes':qs}
    table = AvailablebusForCertainRoutesTable(qs)
    return render(request,'bus/busAvailableForRoute.html' ,{"table":table, "items":qs.count()})





