"""Madlibs Stories."""

stories = []
class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ['adjective1', 'noun1', 'verb_past_tense', 'adverb', 'adjective2', 'noun2', 'noun3', 'adjective3'], 
    """Today I went to the zoo. I saw a big {adjective1} {noun1} jumping up and down in its tree.
He {verb_past_tense} {adverb} through the large tunnel that led to its {adjective2} {noun2}.I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop
of ice cream. It filled my stomach."""
)

story3 = Story(
    ['food', 'name', 'noun' 'adjective', 'verb1', 'verb2', 'verb3'],
    """It was {food} day at school, and {name} was super {adjective} for lunch. But when she went outside to eat, a {noun} stole her {food}! {name} chased the {noun} all over school. She {verb1}, {verb2}, and {verb3} through the playground. Then she tripped on her {noun} and the {noun} escaped! Luckily, {noun}’s friends were willing to share their {food} with her.""")

stories = [story, story2, story3]