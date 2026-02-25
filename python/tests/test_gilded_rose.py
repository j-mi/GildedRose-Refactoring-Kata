# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def update(self, name, sell_in, quality, days=1):
        items = [Item(name, sell_in, quality)]
        goods = GildedRose(items)
        for _ in range(days):
            goods.update_quality()
        return items[0]

    def test_normal_item_degrades_by_1_before_sell_date(self):
        item = self.update("foo", sell_in=10, quality=20)
        self.assertEqual(9, item.sell_in)
        self.assertEqual(19, item.quality)

    def test_normal_item_degrades_by_2_after_sell_date(self):
        item = self.update("foo", sell_in=0, quality=20)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_quality_never_negative(self):
        item = self.update("foo", sell_in=0, quality=0)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_aged_brie_increases(self):
        item = self.update("Aged Brie", sell_in=2, quality=0)
        self.assertEqual(1, item.sell_in)
        self.assertEqual(1, item.quality)

    def test_aged_brie_capped_at_50(self):
        item = self.update("Aged Brie", sell_in=2, quality=50)
        self.assertEqual(1, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_sulfuras_never_changes(self):
        item = self.update("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        self.assertEqual(80, item.quality)
        self.assertEqual(0, item.sell_in)

    def test_backstage_pass_increases_by_1_when_more_than_10_days(self):
        item = self.update("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=15)
        self.assertEqual(10, item.sell_in)
        self.assertEqual(16, item.quality)

    def test_backstage_pass_increases_by_2_when_10_days_or_less(self):
        item = self.update("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=15)
        self.assertEqual(9, item.sell_in)
        self.assertEqual(17, item.quality)

    def test_backstage_pass_increases_by_3_when_5_days_or_less(self):
        item = self.update("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=15)
        self.assertEqual(4, item.sell_in)
        self.assertEqual(18, item.quality)

    def test_backstage_pass_quality_drops_to_0_after_concert(self):
        item = self.update("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=15)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)

    def test_conjured_degrades_twice_as_fast_before_sell_date(self):
        item = self.update("Conjured Magic Hat", sell_in=2, quality=4)
        self.assertEqual(1, item.sell_in)
        self.assertEqual(2, item.quality)

    def test_conjured_degrades_four_times_as_fast_after_sell_date(self):
        item = self.update("Conjured Magic Hat", sell_in=0, quality=8)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(4, item.quality)

if __name__ == "__main__":
    unittest.main()
