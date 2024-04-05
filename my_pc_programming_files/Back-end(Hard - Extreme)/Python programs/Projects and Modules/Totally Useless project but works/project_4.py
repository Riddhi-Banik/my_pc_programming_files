class query_block:
    def __init__(self, _query:str, _choices:list, _reflections:list):
        self.answer = None
        self._query = _query.capitalize()
        self._reflections = _reflections
        self._choice = _choices

    def Decision(self, answer:str):
        self.answer = answer
        return {'_str' : self._reflections[self._choice.index(self.answer)],
                '_ind' : self._choice.index(answer)}

    def __str__(self):
        return f'{self._query}\n({" -> ".join(self._choice)})'



_query1 = query_block("You got stuck in a middle of a island and see a strange boat\nWhat do you want to do?",
                      ["Shout out loud","Try to signal using fire", "Stay quiet and ignore"],
                      ["You shouted but you lost all your energy and got fainted and they couldn't hear.",
                       "They managed to spot you and took with you.",
                       "The ship ignored you as you ignored them.."])
print(_query1)
_indx = _query1.Decision(input("--> "))
print(_indx['_str'])
if _indx['_ind'] == 1:
    _query1_1 = query_block("The strange boat is getting attacked by a group of bombers!\nWhat do you want to do?",
                            ["Swim out of the ship", "try to find a ranged weapon or firearm to defend the ship"],
                            ["You swam but then the explosion of the ship killed you",
                             "you found a homing missile in a secret case but it was too late because the bomb hit before you could"])
    print(_query1_1)
    print(str(_query1_1.Decision(input("--> "))['_str']))
print("Game over.")
