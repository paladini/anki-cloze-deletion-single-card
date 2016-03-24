# -*- coding: utf-8 -*-
# Copyright: Fernando Paladini <fnpaladini@gmail.com>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
# A very simple Anki plugin that allows you to add as many cloze deletions 
# to a card as you want, always showing it up in a single card.
#
from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showInfo, tooltip
import re

def newOnCloze(self):
    # check that the model is set up for cloze deletion
    if not re.search('{{(.*:)*cloze:',self.note.model()['tmpls'][0]['qfmt']):
        if self.addMode:
            tooltip(_("Warning, cloze deletions will not work until you switch the type at the top to Cloze."))
        else:
            showInfo(_("""\
To make a cloze deletion on an existing note, you need to change it \
to a cloze type first, via Edit>Change Note Type."""))
            return
    # always use 'c1' as Cloze Deletion tag.
    self.web.eval("wrap('{{c1::', '}}');")

Editor.onCloze = newOnCloze
