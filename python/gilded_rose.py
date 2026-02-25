# -*- coding: utf-8 -*-

class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED = "Conjured Magic Hat"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if self._is_sulfuras(item):
                continue

            self._update_item_quality(item)

            item.sell_in -= 1

            if item.sell_in < 0:
                self._apply_expired_rules(item)


    def _update_item_quality(self, item):
        if self._is_aged_brie(item):
            self._increase_quality(item, 1)
            return

        if self._is_backstage(item):
            self._increase_quality(item, 1)
            if item.sell_in <= 10:
                self._increase_quality(item, 1)
            if item.sell_in <= 5:
                self._increase_quality(item, 1)
            return

        self._decrease_quality(item, self._decrease_rate(item))

    def _apply_expired_rules(self, item):
        if self._is_aged_brie(item):
            self._increase_quality(item, 1)
            return

        if self._is_backstage(item):
            item.quality = 0
            return

        self._decrease_quality(item, self._decrease_rate(item))

    ####### Quality helpers #######

    def _increase_quality(self, item, amount):
        if item.quality + amount > 50:
            value = 50
        else:
            value = item.quality + amount
        item.quality = value

    def _decrease_quality(self, item, amount):
        if item.quality - amount < 0:
            value = 0
        else:
            value = item.quality - amount
        item.quality = value

    def _decrease_rate(self, item):
        if self._is_conjured(item):
            return 2
        else:
            return 1

    ####### Type checks #######

    def _is_aged_brie(self, item):
        return item.name == self.AGED_BRIE

    def _is_backstage(self, item):
        return item.name == self.BACKSTAGE

    def _is_sulfuras(self, item):
        return item.name == self.SULFURAS

    def _is_conjured(self, item):
        return item.name == self.CONJURED


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
