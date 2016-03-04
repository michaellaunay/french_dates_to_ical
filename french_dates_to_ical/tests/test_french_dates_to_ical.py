# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015 by Ecreall under licence AGPL V3 terms
# avalaible on http://www.gnu.org/licenses/agpl.html
#
# file: test_french_dates_to_ical.py
# author: Michael Launay
#

import french_dates_to_ical.french_dates_grammar as french_dates_grammar

# Teste tous les jours
test_data_tous_les_jours = (
    ("Tous les jours", []),
)

# Teste tous les jours à
test_data_tous_les_jours_a = (
    ("Tous les jours à 8h00", []),
)

# Teste du au
test_data_du_au = (
    ("Du 14 juin au 21 juillet du lundi au dimanche de 14h à 18h, sauf le mardi et les jours fériés", []),
    ("Du 25 mai au 9 juillet tous les jours sauf le lundi, mercredi, jeudi et samedi", []),
    ("Du 3 janvier au 14 janvier 2007 tous les jours sauf le mardi, le samedi, et le dimanche", []),
    ("Du 20 juin au 26 juillet du mardi au samedi de 14h à 18h (fermé les jours fériés)", []),
    ("Du 7 au 30 juin (fermé le lundi)", []),
    ("Du 17 au 23 juin (fermé du lundi au mercredi)", []),
    ("Du 7 au 13 juin (fermé du jeudi au mardi)", []),
    ("Du 15 au 23 juin (fermé du vendredi au mercredi)", []),
    ("Du 1er juin au 3 août (fermé du 1er lundi au 3ème mercredi)", []),
    ("Du 5 juillet au 1er septembre du mardi au vendredi de 9h à 12h et de 14h à 18h, le lundi de 15h à 18h, les 10, 17 et 24 juin de 9h à 12h et de 15h à 15h30 (fermeture du 24 juillet au 20 août)", []),
    ("Du 4 juin au 12 juillet du lundi au dimanche de 14h à 18h, sauf le 1er mardi du mois et les jours fériés", []),
    ("Du 1er septembre au 1er décembre", []),
    ("Du 1er octobre au 30 novembre de 9h à 12h, le weekend de 9h à 12h et de 14h à 18h, fermé le lundi", []),
)

# teste Jusqu'au
test_data_jusqu_au = (
    ("Jusqu'au 1er décembre, tous les soirs à 20h30, le 25 juin à 15h30, relâche les lundis et dimanches", []),
    ("Jusqu'au 1er juillet, tous les soirs à 20h30, le 25 juin à 15h30, relâche les lundis et dimanches", []),
    ("Jusqu'au 31 août", []),
    ("Jusqu'au 2 janvier 2007 à 20h", []),
    ("Jusqu'au 11 décembre", []),
    ("Jusqu'au 28 février tous les midis", []),
    ("Jusqu'au 19 août à 20h", []),
)

# teste Le
test_data_le = (
    ("Le 19/01/1973 à 18h41", ['RDATE;VALUE=DATE-TIME:19730119T184100']),
    ("Le 13/12/1975 à 11h", ['RDATE;VALUE=DATE-TIME:19751213T110000']),
    ("Le 1er janvier à 18h", []),
    ("Le 28 février à partir de 18h", []),
    ("Le 3 mars à partir de 20h", []),
    ("Le 22 juin à 15h30 et le 23 juin à 20h30", []),
    ("Le 25 juin à 15h30 et le 26 juin à 10h30, à 16h11 et à 22h", []),
    ("Le 22 juillet de 21h30 jusqu'à plus soif", []),
    ("Le 23 août de 11h30 jusqu'à l'aube", []),
    ("Le 24 septembre de 21h30 à 23h", []),
    ("Le 25 octobre départ à 14h53", []),
    ("Le 26 novembre dès 12h", []),
    ("Le 9 décembre à 12h, 14 décembre à 19h et le 15 décembre à 18h", []),
    ("Le 12 janvier à 12h, le 13 juin à 15h et le 14 juin à 18h", []),
    ("Le 4 mai à 12h, le 13 juin à 15h et le 14 juin à 18h", []),
    ("Le 31 décembre 2006 à 12h, le 13 janvier 2007 à 15h et le 14 juin 2007 à 18h", []),
    ("Le 19 avril à 10h30, 14h30 et 16h30 et le 20 avril à 14h30 et 16h30", []),
    ("Le 18 à 13h, le 19 de 16h à 17h, le 20 de 10h à 12h et de 14h à 17h, et le 21 juin 2006 à 11h, 12h, 13h et 14h et le 1er janvier 2007 à 1h", []),
)

# teste Les
test_data_les = (
    ("Les 23, 24 à 20h30 et 25 juin à 17h", []),
    ("Les 23, 24 juin à 20h30 et 25 juin à 17h", []),
    ("Les 30 juin et 1er juillet à 20h30", []),
    ("Les 21, 22, 23, 28 et 29 juin de 20h à 22h", []),
    ("Les 28, 29, 30 juin et 1er juillet à 20h30", []),
    ("Les 28, 29, 30 juin et le 1er juillet à 20h30", []),
    ("Les 12 à 15h, 13 à 20h30, 16 et 17 février à 15h", []),
    ("Les 12 à 15h, 13 à 20h30, 16 et 17 juillet à 15h", []),
    ("Les 19, 26 juillet et le 2 août à 20h", []),
    ("Les 28, 29, 30 juin et les 1er, 2, 3, 4 juillet à 20h30", []),
)

# Teste Du au
test_data_du_au = (
    ("Du 23 au 29 juin", []),
    ("Du mardi au samedi soir à 22h", []),
    ("Du 28 janvier 2006 au 14 septembre 2007", []),
    ("Du 3 mars au 3 septembre", []),
    ("Du 5 au 11 août à 14h30", []),
    ("Du 5 mai au 25 juin du mardi au vendredi de 9h à 17h, les samedis et dimanches de 14h à 18h", []),
    ("Du 14 juin au 21 juillet du lundi au dimanche de 14h à 18h, sauf le mardi et les jours fériés", []),
    ("Du 25 mai au 9 juillet tous les jours sauf le lundi de 11h à 18h", []),
    ("Du 1er au 30 juin du lundi au vendredi de 8h à 12h et de 14h à 18h, le samedi de 14h à 18h", []),
    ("Du 3 janvier au 14 janvier 2007 tous les jours sauf mardi de 10h à 12h et de 14h à 17h30, le samedi jusqu'à 18h30, le dimanche de 14h à 18h30", []),
    ("Du 2 juin 2006 au 14 janvier 2007 les lundis, mercredis, jeudis et vendredis de 10h à 12h et de 14h à 17h30, le samedi jusqu'à 18h30, le dimanche de 14h à 18h30", []),
    ("Du 1er au 30 juin les jeudis, vendredis et samedis de 15h à 19h et sur RDV", []),
    ("Du 20 juin au 26 juillet du mardi au samedi de 14h à 18h (fermé les jours fériés)", []),
    ("Du 7 au 30 juin (fermé le lundi)", []),
    ("Du 5 juin au 1er septembre du mardi au vendredi de 9h à 12h et de 14h à 18h, le lundi de 15h à 18h, les 10, 17 et 24 juin de 9h à 12h et de 15h à 15h30 (fermeture du 24 juillet au 20 août)", []),
    ("Du 1er septembre au 30 octobre de 9h à 12h et de 14h à 18h le week-end fermé le lundi", []),
    ("Du 1er septembre au 30 octobre de 9h à 12h, le week-end de 9h à 12h et de 14h à 18h, fermé le lundi", []),
)

# ***************** ENTRÉES MAL FORMATÉES NE DEVANT PAS ÊTRE RECONNUES ****************

# test doit refuser les JusquAu
test_data_bad_jusqu_au = (
    ("Jusqu'au 1 septembre les lundis et mardi", []),
    ("Jusqu'au 1er septembre les lu ndis et mardi", []),
)

# Test doit refuser Le
test_data_bad_le = (
    ("Le 11er janvier à 18h", []),
    ("Le 29 février à partir de 18h", []),
)

# test doit refuser Les
test_data_bad_les = (
    ("Les 25, 24 à 20h30 et 25 juin à 17h", []),
    ("Les 32, 24 juin à 20h30 et 25 juin à 17h", []),
    ("Les 3, 12 juillet à 20h30 et 25 juin à 17h", []),
    ("Les 30 juin 2006 et 1er juillet 2005 à 20h30", []),
)

# test doit refuser Du au
test_data_bad_du_au = (
    ("Du 7 au 32 juin (fermé le lundi)", []),
    ("Du 35 juin au 11er septembre du mardi au vendredi de 9h à 12h et de 14h à 18h, le lundi de 15h à 18h, les 10, 17 et 24 juin de 9h à 12h et de 15h à 15h30 (fermeture du 24 juillet au 20 août)", []),
)


def test_le():
    for v, r in test_data_le:
        assert french_dates_grammar.main(v) == r


def test_tous_les_jours():
    for v, r in test_data_tous_les_jours[:0]:
        assert french_dates_grammar.main(v) == r

def test_tous_les_jours_a():
    for v, r in test_data_tous_les_jours_a[:0]:
        assert french_dates_grammar.main(v) == r
