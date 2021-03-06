import logging

from tmi.model import SpiderTag, Card

from tmi.spiders.openduka import OpenDuka
from tmi.spiders.wiki import Wikipedia
from tmi.spiders.opencorp import OpenCorporates

log = logging.getLogger(__name__)

SPIDERS = {
    'OpenDuka': OpenDuka,
    'OpenCorporates': OpenCorporates,
    'Wikipedia': Wikipedia
}


def lookup(card, spider_name):
    if SpiderTag.find(card, spider_name):
        return
    
    cls = SPIDERS.get(spider_name)
    try:
        spider = cls()
        if card.category == Card.PERSON:
            spider.search_person(card)
        elif card.category == Card.COMPANY:
            spider.search_company(card)
        elif card.category == Card.ORGANIZATION:
            spider.search_organization(card)
        else:
            spider.search_generic(card)
    except Exception, e:
        log.exception(e)

    SpiderTag.done(card, spider_name)
