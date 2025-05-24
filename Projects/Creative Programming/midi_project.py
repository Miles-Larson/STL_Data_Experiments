# %%
notes = {'A':[], 
'A#':[], 
'B':[], 
'C':[], 
'C#':[], 
'D':[], 
'D#':[], 
'E':[], 
'F':[], 
'F#':[], 
'G':[], 
'G#':[], 
 }



# %%
notes['A'].append(9)
notes['A'].append(21)
notes['A'].append(33)
notes['A'].append(45)
notes['A'].append(57)
notes['A'].append(69)
notes['A'].append(81)
notes['A'].append(93)
notes['A'].append(105)
notes['A'].append(117)
notes['A#'].append(10)
notes['A#'].append(22)
notes['A#'].append(34)
notes['A#'].append(46)
notes['A#'].append(58)
notes['A#'].append(70)
notes['A#'].append(82)
notes['A#'].append(94)
notes['A#'].append(106)
notes['A#'].append(118)
notes['B'].append(11)
notes['B'].append(23)
notes['B'].append(35)
notes['B'].append(47)
notes['B'].append(59)
notes['B'].append(71)
notes['B'].append(83)
notes['B'].append(95)
notes['B'].append(107)
notes['B'].append(119)
notes['C'].append(0)
notes['C'].append(12)
notes['C'].append(24)
notes['C'].append(36)
notes['C'].append(48)
notes['C'].append(60)
notes['C'].append(72)
notes['C'].append(84)
notes['C'].append(96)
notes['C'].append(108)
notes['C'].append(120)
notes['C#'].append(1)
notes['C#'].append(13)
notes['C#'].append(25)
notes['C#'].append(37)
notes['C#'].append(49)
notes['C#'].append(61)
notes['C#'].append(73)
notes['C#'].append(85)
notes['C#'].append(97)
notes['C#'].append(109)
notes['C#'].append(121)
notes['D'].append(2)
notes['D'].append(14)
notes['D'].append(26)
notes['D'].append(38)
notes['D'].append(50)
notes['D'].append(62)
notes['D'].append(74)
notes['D'].append(86)
notes['D'].append(98)
notes['D'].append(110)
notes['D'].append(122)
notes['D#'].append(3)
notes['D#'].append(15)
notes['D#'].append(27)
notes['D#'].append(39)
notes['D#'].append(51)
notes['D#'].append(63)
notes['D#'].append(75)
notes['D#'].append(87)
notes['D#'].append(99)
notes['D#'].append(111)
notes['D#'].append(123)
notes['E'].append(4)
notes['E'].append(16)
notes['E'].append(28)
notes['E'].append(40)
notes['E'].append(52)
notes['E'].append(64)
notes['E'].append(76)
notes['E'].append(88)
notes['E'].append(100)
notes['E'].append(112)
notes['E'].append(124)
notes['F'].append(5)
notes['F'].append(17)
notes['F'].append(29)
notes['F'].append(41)
notes['F'].append(53)
notes['F'].append(65)
notes['F'].append(77)
notes['F'].append(89)
notes['F'].append(101)
notes['F'].append(113)
notes['F'].append(125)
notes['F#'].append(6)
notes['F#'].append(18)
notes['F#'].append(30)
notes['F#'].append(42)
notes['F#'].append(54)
notes['F#'].append(66)
notes['F#'].append(78)
notes['F#'].append(90)
notes['F#'].append(102)
notes['F#'].append(114)
notes['F#'].append(126)
notes['G'].append(7)
notes['G'].append(19)
notes['G'].append(31)
notes['G'].append(43)
notes['G'].append(55)
notes['G'].append(67)
notes['G'].append(79)
notes['G'].append(91)
notes['G'].append(103)
notes['G'].append(115)
notes['G'].append(127)
notes['G#'].append(8)
notes['G#'].append(20)
notes['G#'].append(32)
notes['G#'].append(44)
notes['G#'].append(56)
notes['G#'].append(68)
notes['G#'].append(80)
notes['G#'].append(92)
notes['G#'].append(104)
notes['G#'].append(116)


# %%
notes

# %%
notes.update( {'Ab': notes['G#']})
notes.update( {'Bb': notes['A#']})
notes.update( {'Db': notes['C#']})
notes.update( {'Eb': notes['D#']})
notes.update( {'Gb': notes['F#']})

notes


# %%

#mido is used to read and write midi files, winsound can play sounds by hertz input
import mido, winsound
#Pygame is used to synthesize and play midi tracks
import pygame
#datetime will be used to timestamp midi files for progress tracking
import io, datetime, random

# %%
#choose a note, if it chose flat or sharp, choose again, accept whatever the second option is
choose_note = random.choice(list(notes.keys()))
if (choose_note.find('b') > 0 or choose_note.find('#') > 0):
    choose_note = random.choice(list(notes.keys()))
choose_note

# %%
audio_file = mido.MidiFile() 
audio_track = audio_file.add_track('Amazing')
#save a series of midi_messages to the audio_track
for i in range(140):
    midi_message = mido.Message('note_on')
    #midi_message = midi_message.copy(note=(random.randrange(start=0,stop=128)))
    midi_message = midi_message.copy(note=(notes[choose_note][random.randrange(start=1,stop=len(notes[choose_note]))]))

    midi_message = midi_message.copy(channel=(random.randrange(start=1,stop=15)))
    midi_message = midi_message.copy(velocity=(random.randrange(start=44,stop=100)))
    midi_message = midi_message.copy(time=(random.randrange(start=0,stop=140)))
    audio_track.append(midi_message)

audio_file.save('new_song.mid')



# %%
print(audio_file)
pygame.init()
pygame.mixer.music.load(r"new_song.mid")
pygame.mixer.music.play()


