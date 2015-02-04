#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2014 by Ecreall under licence AGPL terms,
# avalaible on http://www.gnu.org/licenses/agpl.html
#
# file: french_dates_grammar.py
# author: Michael Launay


from parsimonious import Grammar, NodeVisitor

exp_le = """
EXP_LE = LE_DATE_A / LE_DATE_PERIODE / LE_DATE
LE_DATE_A = LE_DATE ESPACE A ESPACE HORAIRE
LE_DATE_PERIODE = LE_DATE ESPACE PERIODE
LE_DATE = LE ESPACE (NOMS_JOUR / DATE)
"""

exp_les = """
EXP_LES = LES_DATES_A / LES_DATES_PERIODE / LES_DATES
LES_DATES_A = LES_DATES ESPACE A ESPACE HORAIRE
LES_DATES_PERIODE = LES_DATES ESPACE PERIODE
LES_DATES = LES ESPACE (DATES / LISTE_JOURS)
"""

exp_tous = """
EXP_TOUS = TOUS_LES_JOURS_A / TOUS_LES_JOURS_SAUF / TOUS_LES_JOURS / TOUS_LES_NOMS_JOURS_A / TOUS_LES_NOMS_JOURS
TOUS_LES_JOURS_A = TOUS_LES_JOURS ESPACE A ESPACE HORAIRE
TOUS_LES_NOMS_JOURS_A = TOUS_LES_NOMS_JOURS ESPACE A ESPACE HORAIRE
TOUS_LES_JOURS_SAUF = TOUS_LES_JOURS_SAUF_LE / TOUS_LES_JOURS_SAUF_LES
TOUS_LES_JOURS_SAUF_LE = TOUS_LES_JOURS ESPACE SAUF ESPACE LE_DATE
TOUS_LES_JOURS_SAUF_LES = TOUS_LES_JOURS ESPACE SAUF ESPACE LES_DATES
TOUS_LES_NOMS_JOURS = TOUS_LES ESPACE NOMS_JOURS
"""

exp_s = """
S = EXP_LES / EXP_LE / EXP_TOUS
"""

french_dates_grammar = exp_s + exp_les + exp_le + exp_tous +"""
HORAIRE = HEURES HEURE_SYMBOLE MINUTES
LISTE_JOURS = NOMS_JOURS (VIRGULE ESPACE NOMS_JOURS)+
DATE = JOUR DATE_SEPARATEUR MOIS DATE_SEPARATEUR ANNEE
DATES = DATE (VIRGULE ESPACE DATE)+
DATE_SEPARATEUR = "/"
PERIODE = DE ESPACE HORAIRE ESPACE A ESPACE HORAIRE
TOUS_LES_JOURS = "tous les jours"
TOUS_LES = "tous les"
LES = "les"
LE = "le"
DE = "de"
A = "à"
SAUF = "sauf"
ESPACE = ~"[ \t]+"
HEURES = ~"(1[0-9]|2[0-3]|[0-9])"
HEURE_SYMBOLE = "h"
MINUTES = ~"[0-5][0-9]"
JOUR = ~"[1-2][0-9]" / ~"3[0-1]" / ~"0?[1-9]"
MOIS = ~"1[0-2]" / ~"0?[1-9]"
ANNEE = ~"20[0-9][0-9]" / ~"19[0-9][0-9]"
VIRGULE = ","
RANG = "1er" / "2ème" / "3ème" / "4ème" / "5ème"
NOMS_RANG = "premier" / "deuxième" / "troisième" / "quatrième" / "cinquième"
NOMS_RANGS = "premiers" / "deuxièmes" / "troisièmes" / "quatrièmes" / "cinquièmes"
NOMS_JOUR = "lundi" / "mardi" / "mercredi" / "jeudi" / "vendredi" / "samedi" / "dimanche"
NOMS_JOURS = "lundis" / "mardis" / "mercredis" / "jeudis" / "vendredis" / "samedis" / "dimanches"
NOMS_MOIS = "janvier" / "février" / "mars" / "avril" / "mai" / "juin" / "juillet" / "août" / "septembre" / "octobre" / "novembre" / "décembre"
"""

rang = ("1er", "2ème", "3ème", "4ème", "5ème")
noms_rang = ("premier", "deuxième", "troisième", "quatrième", "cinquième")
noms_rangs = ("premiers", "deuxièmes", "troisièmes", "quatrièmes", "cinquièmes")
jour = ("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche")
jours = ("lundis", "mardis", "mercredis", "jeudis", "vendredis", "samedis", "dimanches")
mois = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre")

grammar = Grammar(french_dates_grammar)

class GrammarTraceVisitor(NodeVisitor):
    def visit_(self, node, childs):
        pass


def do_nothing(self, node, childs):
    pass

def trace_method(f, name):
    def func(self, node, childs):
        print("visit_%s(self=%s, node=%s, childs=%s)\n\n"%(name, self, node, childs))
        f(self, node, childs)
    return func

expression_names = [x.split("=")[0].strip() for x in french_dates_grammar.split("\n") if x.find("=") != -1]

for name in expression_names:
    visitor = GrammarTraceVisitor
    dir_visitor = dir(visitor)
    visit_name = "visit_%s"%name
    if visit_name not in dir_visitor:
        setattr(visitor, visit_name, trace_method(do_nothing, visit_name))

if __name__ == "__main__":
    import sys
    while 1 :
        print("Saisisez une expression à tester : ")
        s = sys.stdin.readline()[:-1]
        root = grammar.parse(s)
        hv = GrammarTraceVisitor()
        hv.visit(root)

