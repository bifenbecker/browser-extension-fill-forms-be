from django.conf.urls import url

from statistic.views import StatisticUsersView, StatisticUserDetailView

urlpatterns = [
    url(r"^users/$", StatisticUsersView.as_view(), name="statistic_url"),
    url(r"^users/(?P<id>\d+)/$", StatisticUserDetailView.as_view(), name="statistic_to_user_url")
]
