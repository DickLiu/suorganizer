# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:32:13 2017

@author: user
"""

from django.http import (
        Http404, HttpResponseRedirect)
from django.views.generic.dates import(
        DateMixin, MonthMixin as BaseMonthMixin,
        YearMixin as BaseYearMixin,
        _date_from_string)

class AllowFuturePermissionMixin():
    '''
    get_allow_future()是CBV預設的view
    藉由改寫這個view,讓沒有view_future_post的
    回傳false
    '''
    def get_allow_future(self):
        return self.request.user.has_perm(
                "blog.view_future_post")

   
class MonthMixin(BaseMonthMixin):
    month_format = '%m'
    month_query_kwarg = 'month'
    month_url_kwarg = 'month'
    
    def get_month(self):
        month = self.month
        if month is None:
            month = self.kwargs.get(
                    self.month_url_kwarg,
                    self.request.GET.get(
                            self.month_query_kwarg))
        if month is None:
            raise Http404('No month specified')
        return month
    
    
class YearMixin(BaseYearMixin):
    year_query_kwarg = 'year'
    year_url_kwarg = 'year'
    
    def get_year(self):
        year = self.year
        if year is None:
            year  = self.kwargs.get(
                    self.year_url_kwarg,
                    self.request.GET.get(
                            self.year_query_kwarg))
        if year is None:
            raise Http404('No year specified')
        return year
    
    
class DateObjectMixin(
        AllowFuturePermissionMixin,
        YearMixin, MonthMixin, DateMixin):
    
    def get_object(self, queryset=None):
        year = self.get_year()
        month = self.get_month()
        date = _date_from_string(
                year, self.get_year_format(),
                month, self.get_month_format(),
                )
        if queryset is None:
            queryset = self.get_queryset()
        if (not self.get_allow_future()
                and date > date.today()):
            raise Http404(
                    'Future {} not available because'
                    '{}.allow_future is False.'
                    .format(
                            (queryset.model._meta.verbose_name_plural),
                            self.__class__.__name__))
        filter_dict = (
                self._make_single_date_lookup(date))
        queryset = queryset.filter(**filter_dict)
        return super().get_object(
                queryset=queryset)
        
    def _make_single_date_lookup(self, date):
        #取得用來查詢過濾日期的kwargs
        date_field = self.get_date_field()
        if self.uses_datetime_field:
            since = self._make_date_lookup_arg(
                    date)
            #_make_date_lookup_arg()是當date如果是以datetimefield
            #儲存時會適當的設定其時區
            until = self._make_date_lookup_arg(
                    self._get_next_month(date))
            return {
                    '%s__gte' % date_field: since,
                    '%s__lt' % date_field: until,
                    }
        else:
            return {
                    '%s__gte' % date_field: date,
                    '%s__lt' % date_field:
                    self._get_next_month(date),
                    }

class PostFormValidMxin:
    
    def form_valid(self, form):
        self.object = form.save(self.request)
        return HttpResponseRedirect(
                self.get_success_url())
        
    
    
            
        

    
