from django.shortcuts import render, HttpResponse
from .parser import parsing
import logging


logger = logging.getLogger(__name__)


def rating(request):
    try:
        information, update_time, count_statements = parsing()
        logger.info("SUCCESSFLY GET INFO FROM PARSER")
        return render(request, "itmo_rating/rating.html", {
                    "information": information,
                    "update_time": update_time, 
                    "count_statements": count_statements})
    except BaseException:
        logger.critical("CAN NOT GET INFO FROM PARSER")
        return HttpResponse("error")
