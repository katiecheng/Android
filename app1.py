import android

droid = android.Android()

droidMsg = "Katie's first app"
droid.dialogCreateAlert(droidMsg)

droid.dialogSetNegativeButtonText('BOOO')
droid.dialogSetPositiveButtonText('COOL')
droid.dialogShow()
resp = droid.dialogGetResponse().result

if resp["which"]=="positive":
    droid.makeToast("Peace out bro!")
else:
    droid.makeToast("Bye dude.")