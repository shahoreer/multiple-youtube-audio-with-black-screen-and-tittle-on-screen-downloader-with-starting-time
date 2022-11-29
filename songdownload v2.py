from pytube import YouTube
import ssl
from moviepy.editor import *
ssl._create_default_https_context = ssl._create_stdlib_context

background=VideoFileClip("/Users/shahoreertalha/Desktop/Coding/TheBro Music/codes/source/bk.mp4")
path="/Users/shahoreertalha/Desktop/Desktop/Work/TheBro Music/song draft"


os.chdir(path)

ins=input("Link, Start, Link2, Start2....Instruction: ").split(",")


def convtime(num): # 102(1 minute 2 sec) -> 62
    thetime=num
    if thetime>100:
        m=int(thetime/100)
        a=thetime-m*100
        num=m*60+a
    return num

def textclips(str):
    str=str.replace(".mp3","").split("/")[-1]
    n=20
    text_clips=[]
    split_strings=[str]
    split_strings = [str[i:i+n] for i in range(0, len(str), n)]
    y_pos=0

    b=0
    while(b<len(split_strings)):
        a=split_strings[b]
        newtextclip=TextClip(a, fontsize = 20, color = 'white')
        newtextclip = newtextclip.set_pos(('center',y_pos)).set_duration(5)
        y_pos+=30

        text_clips.append(newtextclip)
        b+=1
    return text_clips

def downloadvid(link,start):

    vd=YouTube(link)

    if start>2:
        start=convtime(start)-2
    end=start+65
    if end>vd.length:
        end=vd.length

    vd.streams.filter(only_audio=True).all()[0].download(path)
    aud_location=path+"/"+sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getctime)[-1]
    os.rename(aud_location,aud_location.replace("mp4","mp3"))
    aud_location=aud_location.replace("mp4","mp3")

    background.audio=AudioFileClip(aud_location).subclip(start,end)
    CompositeVideoClip([background.subclip(0,end-start),*textclips(aud_location)]).write_videofile(aud_location.replace("mp3","mp4"),codec='libx264',audio_codec='aac')

i=0
while i<len(ins):
    downloadvid(ins[i],int(ins[i+1]))
    i+=2