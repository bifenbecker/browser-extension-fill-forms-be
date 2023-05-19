import json
import csv
import io
import zipfile
from collections import Counter

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from django.db.models import Avg
from rest_framework.renderers import JSONRenderer
from customers.models import CustomUser, FillField
from customers.serializers import CustomerStatisticSerializer
from pprint import pprint


class StatisticUsersView(TemplateView):
    template_name = 'users_statistic.html'

    def get_context_data(self, **kwargs):
        users = CustomUser.objects.all()
        return {
            'users': users
        }


class StatisticUserDetailView(View):
    template_name = 'user_detail_statistic.html'

    def post(self, request, **kwargs):
        user_id = kwargs.get('id', None)
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            sites = []
            statistics_query = user.settings.statistic
            serializer = CustomerStatisticSerializer(statistics_query.filter(success=True), many=True)
            statistics_success = json.loads(JSONRenderer().render(serializer.data))
            serializer = CustomerStatisticSerializer(statistics_query.filter(success=False), many=True)
            statistics_failed = json.loads(JSONRenderer().render(serializer.data))
            serializer = CustomerStatisticSerializer(statistics_query, many=True)
            statistics = json.loads(JSONRenderer().render(serializer.data))

            general_sites = [stat['site'] for stat in statistics]
            success_sites = [stat['site'] for stat in statistics_success]
            failed_sites = [stat['site'] for stat in statistics_failed]
            default = {
                "ikea": 0,
                "waterstones": 0,
                "roh": 0,
                "etsy": 0,
                "rocketblocks": 0,

            }
            general_counter = Counter(general_sites, **default)
            success_counter = Counter(success_sites, **default)
            failed_counter = Counter(failed_sites, **default)
            for site in default.keys():
                fields_db = FillField.objects.filter(statistic__in=statistics_query.filter(success=True, site=site),
                                                     is_filled=True)
                counter = Counter([field.name for field in fields_db])
                fields = []
                for field_name in counter:
                    fields.append({
                        "name": field_name,
                        "count": counter[field_name]
                    })
                avg_price = statistics_query.filter(success=True, site=site, price__gte=0).aggregate(Avg('price'))[
                    'price__avg']
                sites.append({
                    "fields": fields,
                    "name": site,
                    "general_count": general_counter[site],
                    "success_count": success_counter[site],
                    "failed_count": failed_counter[site],
                    "avg_price": round(avg_price, 2) if avg_price else 0.0,
                    "filled_fields": FillField.objects.filter(
                        statistic__in=statistics_query.filter(success=True, site=site),
                        is_filled=True).count(),
                })

            fieldnames = ['avg_price', 'failed_count', 'filled_fields', 'general_count', 'name', 'success_count',
                          'fields']
            response = HttpResponse(
                content_type="text/csv",
                headers={"Content-Disposition": 'attachment; filename="statistic.csv"'},
            )
            writer = csv.DictWriter(response, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sites)
            return response

    def get(self, request, **kwargs):
        user_id = kwargs.get('id', None)
        user = CustomUser.objects.filter(id=user_id).first()
        if user:
            sites = []
            statistics_query = user.settings.statistic
            serializer = CustomerStatisticSerializer(statistics_query.filter(success=True), many=True)
            statistics_success = json.loads(JSONRenderer().render(serializer.data))
            serializer = CustomerStatisticSerializer(statistics_query.filter(success=False), many=True)
            statistics_failed = json.loads(JSONRenderer().render(serializer.data))
            serializer = CustomerStatisticSerializer(statistics_query, many=True)
            statistics = json.loads(JSONRenderer().render(serializer.data))

            general_sites = [stat['site'] for stat in statistics]
            success_sites = [stat['site'] for stat in statistics_success]
            failed_sites = [stat['site'] for stat in statistics_failed]
            default = {
                "ikea": 0,
                "waterstones": 0,
                "roh": 0,
                "etsy": 0,
                "rocketblocks": 0,

            }
            general_counter = Counter(general_sites, **default)
            success_counter = Counter(success_sites, **default)
            failed_counter = Counter(failed_sites, **default)
            for site in default.keys():
                fields_db = FillField.objects.filter(statistic__in=statistics_query.filter(success=True, site=site),
                                                     is_filled=True)
                counter = Counter([field.name for field in fields_db])
                fields = []
                for field_name in counter:
                    fields.append({
                        "name": field_name,
                        "count": counter[field_name]
                    })
                avg_price = statistics_query.filter(success=True, site=site, price__gte=0).aggregate(Avg('price'))[
                    'price__avg']
                sites.append({
                    "fields": fields,
                    "name": site,
                    "general_count": general_counter[site],
                    "success_count": success_counter[site],
                    "failed_count": failed_counter[site],
                    "avg_price": round(avg_price, 2) if avg_price else 0.0,
                    "filled_fields": FillField.objects.filter(
                        statistic__in=statistics_query.filter(success=True, site=site),
                        is_filled=True).count(),
                })
            pprint(sites)
            context = {
                'page_title': user_id,
                'user': user,
                'sites': sites,
            }
            return render(request=request, template_name=self.template_name, context=context)
        return {}
