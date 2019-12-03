# EasyFNBot

## Introduction

> With EasyFNBot you can easily create you own Fortnite Lobby Bot in less then 5 minutes

## Installation

> 1. Download and unzip [this](https://github.com/LupusLeaks/EasyFNBot/releases/download/EasyFNBot/EasyFNBot.zip)
> 2. In the unzipped folder open "Settings.json" and modify it as you want
> 3. Run "Start.bat" , if you close the command prompt your bot will shut down

## How to make this 24/7
I am currently working on the 24/7 version :)

## Settings
```
{
    "BotVersion": "0.0.1",
    "Email": "YOUR_EMAIL", #The bots epicgames email 
    "Password": "YOUR_PASSWORD",#The bots epicgames password
    "Platform": "Playstation", #Platform : Windows,Mac,Playstation,Xbox,Switch,Android,iOS
    "SeasonLevel": 100, #The bots season level
    "Banner": "OtherBanner28", #The bots banner
    "CustomStatus": "Follow @LupusLeaks on Twitter", #The Bots Status
    "GiveFullAccessTo": "", #Ids of users who can use all commands (split multiple ids with ",")
    "LogoutOnCommand": true, #If true the bot will logout if someone writes "!Logout"
    "RestartOnCommand": true, #If true the bot will logout if someone writes "!Restart"

    "AcceptAllFriendRequests": true, #The Bots will accept all old incoming friend requests
    "AcceptIncomingFriendRequest": true, #The bot will accept the incoming friend requests
    "InviteFriendOnFriendAdded": true, #The bot will invite the user after he got added
    "SendFriendRequestOnFriendRemove": true, #If someone unfriends the bot, the bot will send a friend request to this person
    "JoinPartyOnInvitation": true, #If true the party will join parties on invite

    "SetSkinOnCommand": true, #If true users can control the skin via "!Skin <Skin Name> *lang=<Language Code> *<VariantChannelName>=<Variant Name>" example : "!Skin ghoul trooper --lang=de --material=rosa"
    "DefaultSkin": "Ghoul Trooper", #The bot will wear this skin if he joins a new party

    "SetBackpackOnCommand": true, #If true users can control the backpack via "!Backpack <Backpack Name> *lang=<Language Code>" example : "!Skin disko --lang=de"
    "DefaultBackpack": "",#The bot will wear this backpack if he joins a new party

    "SetEmoteOnCommand": true, #If true users can control the emote via "!Emote <Emote Name> *lang=<Language Code>" example : "!Emote Floss --lang=de"
    "LetOthersStopEmote": true, #If true users can use the command "!Stop Emote"
    "EmoteAfterJoiningParty": true, 
    "EmoteName": "True Heart", #The bot will dance this emote if EmoteAfterJoiningParty is true

    "KickMembersOnCommand": true, #If true users can kick members via "!Kick <User Name>"
    "PromoteMembersOnCommand": true, #If true users can promote members via "!Promote <User Name>" or "!Promote" to promote yourself
    "InviteUserOnCommand": true, #If true users can invite others via "!Invite <User Name>" or "!Invite" to invite yourself
    "LeavePartyOnCommand": true, #If true the bot will leave if others write "!leave party"
    "ThanksOnPromote": true, #If true the bot will emote after he got promoted

    "SendFriendRequestsOnCommand": true, #If true users can add users via "!Add <User Name>"
    "RemoveOthersOnCommand": true, #If true users can remove users via "!Remove <User Name>" or "!Remove" to remove yourself

    "ChangeBattlePassInfoOnCommand": true, #If true users can use the command "!BP <True/False> <Level> <Self XP Boost> <Friend XP Boost>"
    "ChangeStatusOnCommand": true, #If true users can use the command "!Status <Status>"
    "ChangeBannerOnCommand": true, #If true users can use the command "!Banner <Banner Name> --level=<Season Level>" example: "!Banner OtherBanner28 --level=150"
    "SetReadyOnCommand": true, #If true users can use the command "!Ready"
    "SetNotReadyOnCommand": true, #If true users can use the command "!Not Ready"

    "SendCurrentFriendCountOnCommand": true, #If true users can use the command "?friends"
    "SendCurrentBlockedUserCountOnCommand": true, #If true users can use the command "?blocked"
    "SendShopPriceOnCommand": true, #If true users can use the command "?shop price"
    "SendAssistedChallengeOnCommand": true, #If true users can use the command "?Assisted challenge"
    "SendCurrentBannerNameOnCommand": true, #If true users can use the command "?banner"
    "SendIDOnCommand": true, #If true users can use the command "?id" to get the bots id or "?Id <User Name>" to get the id of the user name
    "SendCurrentPartyLeaderOnCommand": true, #If true users can use the command "?party leader"
    "SendTimeBotJoinedTheLobbyOnCommand": true, #If true users can use the command "?joined" 
    "SendPartyInfosOnCommand": true, #If true users can use the command "?party"

    "ChangePlatformOnCommand": true, #If true users can change the platform of the bot(, the bot will leave the party)
    "TryToRejoinOldParty": true, #The Bot will try to rejoin the party after he changed his platform
}
```
