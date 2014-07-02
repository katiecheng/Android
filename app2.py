import android

droid = android.Android()

title = "Hashtag me"
msg = "Type a short phrase:"

tag = droid.dialogGetInput(title, msg).result
tag_list = tag.split(" ")

hashtag = '#'

for word in tag_list:
   hashtag += word

droid.makeToast(hashtag)
