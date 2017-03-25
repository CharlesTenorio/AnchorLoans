import  re
class Validation:

  def  validate(self, card_number):
       raise NotImplementedError('Exception raised, Card validator is supposed to be an interface / abstract class!')


class Startwith(Validation):

    def validate(self,card_number):
        result_start = 'Invalid'

        if card_number.startswith('4'):
            result_start = 'Valid'
        elif card_number.startswith('5'):
            result_start = 'Valid'
        elif card_number.startswith('6'):
            result_start = 'Valid'
        else:
            result_start = 'Invalid'

        return result_start


class Exactly16(Validation):
    def validate(self, card_number):
        num_lenght = len(card_number.replace('-', ""))

        if num_lenght == 16:
            return 'Valid'

        if num_lenght > 16:
            return 'Invalid'

        if num_lenght < 16:
            return 'Invalid'


class Digits(Validation):
    def validate(self, card_number):
        msg = ''

        if card_number.isdigit():
            msg = 'Valid'
        else:
            msg = 'Invalid'

        return msg


class Group4(Validation):
    def validate(self, card_number):
        exp = re.match('(\d{4}-)+\d{4}$', card_number)
        if exp:
            return 'Valid'
        else:
            return 'Invalid'

class Separator(Validation):
    def validate(self, card_number):
        if card_number.find('-'):
            return 'Valid'
        else:
            return 'Invalid'


class Consecutive(Validation):
    def validate(self, card_number):
        last = ''
        results = []
        isconsecutive = 'Invalid'

        for character in card_number:
            if character == last:
                results[-1] = (character, results[-1][1] + 1)

            else:
                results.append((character, 1))
                last = character

        for i in range(len(results)):
            if results[i][1] >= 5:
                isconsecutive = 'Invalid'
                break
            else:
                isconsecutive = 'Valid'

        return isconsecutive
