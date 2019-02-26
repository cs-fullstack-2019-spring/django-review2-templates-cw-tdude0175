from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

songs = [
    {
        'song_id': 0,
        'song_title': 'The New America',
        'song_band': 'Bad Religion',
        'song_album': 'The New America',
        'song_lyrics': 'https://genius.com/Bad-religion-new-america-lyrics',
        'song_audio': 'https://youtu.be/ZUYMVJ8-1yM'
    },
    {
        'song_id': 1,
        'song_title': 'What Do You Do?',
        'song_band': 'Saigon Kick',
        'song_album': 'Saigon Kick',
        'song_lyrics': 'https://genius.com/Saigon-kick-what-do-you-do-lyrics',
        'song_audio': 'https://youtu.be/p1nnx7QTfWE'
    },
    {
        'song_id': 2,
        'song_title': 'MIA',
        'song_band': 'Rancid',
        'song_album': '...and Out Come the Wolves',
        'song_lyrics': 'https://genius.com/Rancid-listed-mia-lyrics',
        'song_audio': 'https://youtu.be/wx4Q2cgNjSw'
    },
    {
        'song_id': 3,
        'song_title': 'Motivational',
        'song_band': 'Toadies',
        'song_album': 'Stars Above, Hell Below',
        'song_lyrics': 'https://genius.com/Toadies-motivational-lyrics',
        'song_audio': 'https://youtu.be/VO5qF1hn7YY'
    },
    {
        'song_id': 4,
        'song_title': 'God Save the Queen',
        'song_band': 'Sex Pistols',
        'song_album': 'Nevermind the Bollocks, Heres the Sex Pistols',
        'song_lyrics': 'https://genius.com/Sex-pistols-god-save-the-queen-lyrics',
        'song_audio': 'https://youtu.be/02D2T3wGCYg'
    },
    {
        'song_id': 5,
        'song_title': 'I Want You to Want Me',
        'song_band': 'Cheap Trick',
        'song_album': 'Live at Budokan',
        'song_lyrics': 'https://genius.com/Cheap-trick-i-want-you-to-want-me-live-lyrics',
        'song_audio': 'https://youtu.be/BJs_L7yq5qE'
    },
    {
        'song_id': 6,
        'song_title': 'I Think That the World...',
        'song_band': 'Bouncing Souls',
        'song_album': 'Ghosts on the Boardwalk',
        'song_lyrics': 'https://genius.com/The-bouncing-souls-i-think-that-the-world-lyrics',
        'song_audio': 'https://youtu.be/ZRK59k1G3sY'
    },
    {
        'song_id': 7,
        'song_title': 'My Own Worst Enemy',
        'song_band': 'Lit',
        'song_album': 'A Place in the Sun',
        'song_lyrics': 'https://genius.com/Lit-my-own-worst-enemy-lyrics',
        'song_audio': 'https://youtu.be/sc5iTNVEOAg'
    },
    {
        'song_id': 8,
        'song_title': 'Deep Fried and Satisfied',
        'song_band': 'Claude Hay',
        'song_album': 'Deep Fried and Satisfied',
        'song_lyrics': 'https://www.musixmatch.com/lyrics/Claude-Hay/Deep-Fried-Satisfied',
        'song_audio': 'https://youtu.be/Eo7oGCUYE3w'
    }
]

def index(request):
    return HttpResponse('test')

# they all have links to eachother
def list_songs(request):
    content = \
        {
            'songList': songs
        }
    return render(request, 'r_2_app/index.html', content)

def list_song(request, song_id):
    content = \
        {
            'song':songs[song_id]
        }
    return render(request, 'r_2_app/details.html',content)

def list_songDetails(request, song_id):
    content = \
        {
            'song':songs[song_id]
        }
    return render(request, 'r_2_app/outsideLinks.html',content)