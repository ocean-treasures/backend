def choose_words(game):
    guessed_words = []
    correct_word = game.words.exclude(id__in=guessed_words).order_by('?').first()
    chosen_pictures = game.words.exclude(id=correct_word.id).order_by('?')[:3]
    words = [
        {
            'url': picture.picture_url,
            'id': picture.id
        }
        for picture in chosen_pictures
    ]
    words.append(
        {
            'url': correct_word.picture_url,
            'id': correct_word.id
        }
    )
    word = {
        'id': correct_word.id,
        'word': correct_word.text
    }
    return word, words
