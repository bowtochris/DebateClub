def loadDeckEvent(player=None, args=None):
    shared.PromptDeck.shuffle()
    shared.SubjectDeck.shuffle()

def gameStartEvent(args=None):
    setGlobalVariable("judge",len(players))
    setGlobalVariable("debater1",1)
    if len(players) >= 2:
        setGlobalVariable("debater2",2)
    ret = getGlobalVariable("judge")
    ret = int(ret)
    for p in players:
        if p._id == ret:
            notify("{} is judge.".format(p))
            break

def nextjudge(group,x=0,y=0):
    ret = getGlobalVariable("judge")
    ret = int(ret)
    if ret == len(players):
        ret = 1
    else:
        ret = ret + 1
    for p in players:
        if p._id == ret:
            notify("{} is now judge.".format(p))
            setGlobalVariable("judge",ret)
            break

def becomejudge(group,x=0,y=0):
    notify("{} is now judge.".format(me))
    setGlobalVariable("judge",me._id)

def whosjudge(group,x=0,y=0):
    ret = getGlobalVariable("judge")
    ret = int(ret)
    for p in players:
        if p._id == ret:
            notify("{} is judge.".format(p))
            break

def becomedebater(group,x=0,y=0):
    d1 = getGlobalVariable("debater1")
    d2 = getGlobalVariable("debater2")
    if d2 == me._id:
        notify("{} remains the debater.".format(me))
    elif d1 == me._id:
        setGlobalVariable("debater1",d2)
        setGlobalVariable("debater2",d1)
        notify("{} remains the debater.".format(me))
    else:
        setGlobalVariable("debater1",d2)
        setGlobalVariable("debater2",me._id)
        notify("{} becomes a debater.".format(me))
        
def whosdebater(group,x=0,y=0):
    d1 = ""
    d2 = ""
    ret = getGlobalVariable("debater1")
    ret = int(ret)
    for p in players:
        if p._id == ret:
            d1 = "{}".format(p)
            break
    ret = getGlobalVariable("debater2")
    ret = int(ret)
    for p in players:
        if p._id == ret:
            d2 = "{}".format(p)
            break
    notify("The debaters are " + d1 + " and " + d2 + ".")

def listplayers(group, x = 0, y = 0):
    notify("{}".format(players))

def draw_prompt(group, x = 0, y = 0):
    for i in range(3):
        if len(shared.PromptDeck) == 0: break
        mute()
        shared.PromptDeck[0].moveTo(me.hand)
    if i > 0:
        notify("{} draws some Prompt cards.".format(me))
    else:
        notify("{} couldn't draw Prompt cards!".format(me))

def draw_subject(group, x = 0, y = 0):
    while len(me.hand) > 0:
        me.hand[0].moveTo(shared.Discard)
    for i in range(7):
        if len(shared.SubjectDeck) == 0: break
        mute()
        shared.SubjectDeck[0].moveTo(me.hand)
    if i > 0:
        notify("{} draws some Subject cards.".format(me))
    else:
        notify("{} couldn't draw Subject cards!".format(me))

def submit(card, x = 0, y = 0):
  mute()
  ret = getGlobalVariable("judge")
  ret = int(ret)
  for p in players:
    if p._id == ret:
        card.moveTo(p.submissions)
        break


def discard(card, x = 0, y = 0):
  mute()
  src = card.group
  fromText = " from the table" if src == table else " from their " + src.name
  card.moveTo(shared.Discard)
  notify("{} discards {}{}.".format(me, card, fromText))

def listSubmissions(group, x = 0, y = 0):
    if isJudge(group, x, y):
        whisper(','.join(map(lambda x: x.name, me.submissions)))

def isJudge(group, x = 0, y = 0):
    ret = getGlobalVariable("judge")
    ret = int(ret)
    return me._id == ret
