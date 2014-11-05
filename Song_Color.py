import json, urllib.request

class Song_Color:

    def __init__(self, id):
        url = "http://developer.echonest.com/api/v4/track/" \
              "profile?api_key=AFUD2LVWLLXSYMNBC&" \
              "format=json&bucket=audio_summary&id="
        url += id
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))

        value = data['response']['track']['audio_summary']
        self.speech = value['speechiness']
        self.tempo = value['tempo']
        self.energy = value['energy']
        self.liveness = value['liveness']
        self.acoustic = value['acousticness']
        self.dance = value['danceability']
        self.valence = value['valence']

    def rgb_to_hex(rgb_value):
        return '#%02x%02x%02x' % rgb_value

    def hex_to_rgb(hex_value):
        hex_value = hex_value.lstrip('#')
        return tuple(int(hex_value[i:i + len(hex_value) // 3], 16)for i in range(0, len(hex_value), len(hex_value)//3))

#print(Song_Color.rgb_to_hex((255,1,255)))
#print(hex_to_rgb("#ff01ff"))

#color = Song_Color("spotify:track:1CmUZGtH29Kx36C1Hleqlz")
#color = Song_Color("spotify:track:5a5so8nqDGq75MI5WMbBtT")
#color = Song_Color("spotify:track:7FXj7Qg3YorUxdrzvrcY25")
color = Song_Color("spotify:track:4rwpZEcnalkuhPyGkEdhu0")
hex = Song_Color.rgb_to_hex((color.dance*255, color.speech*255, color.energy*255))
print(hex)