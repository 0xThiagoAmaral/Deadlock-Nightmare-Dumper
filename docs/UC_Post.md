[TITLE]
[Release] Deadlock Nightmare Dumper - Multi-Language SDK & 33 Hero Crawler

[CONTENT]
Yo guys, 

Tired of looking for offsets after every Deadlock patch? Yeah, me too. 

I decided to clean up my personal dumper and release it for everyone. It's a Python-based engine that handles the heavy lifting of Source 2 schema walking and pattern scanning. Instead of just giving you a static list of offsets that will be dead in a week, this tool finds them in real-time.

[B][SIZE="4"]What's inside:[/SIZE][/B]
[LIST]
[*] [B]Hero Crawler[/B]: It actually scans the schema for all [B]33 heroes[/B]. It finds even the hidden Lab pawns and abilities without you needing to hardcode anything.
[*] [B]SDK Generation[/B]: It generates [B]C++ (.hpp)[/B] and [B]C# (.cs)[/B] files automatically. Just run the script, copy the SDK to your project, and you're good to go.
[*] [B]JSON Output[/B]: If you're doing stuff in Lua or Python, it's all there in a structured JSON.
[*] [B]Discord Webhooks[/B]: You can set a webhook in [I]config.json[/I] to get notified when the dump is done. Great if you're running this on a server or for your dev team.
[*] [B]Stable Patterns[/B]: I've picked the most resilient signatures for EntityList, ViewMatrix, and LocalPlayer. 
[/LIST]

[B][SIZE="4"]Preview of the SDK output:[/SIZE][/B]
[CODE]
namespace Nightmare {
    namespace Globals {
        constexpr std::ptrdiff_t dwEntityList = 0x3761a58;
        constexpr std::ptrdiff_t dwLocalPlayerController = 0x37665e0;
        constexpr std::ptrdiff_t dwViewMatrix = 0x376bd40;
    }
    // All hero pawns and netvars follow...
}
[/CODE]

[B][SIZE="4"]How to run it:[/SIZE][/B]
1. Install Pymem: [I]pip install pymem requests[/I]
2. Have Deadlock open.
3. Run [I]python nightmare_dumper.py[/I].
4. Check the root folder for your SDKs and the JSON file.

[B][SIZE="4"]Source Code:[/SIZE][/B]
[URL="https://github.com/0xThiagoAmaral/Deadlock-Nightmare-Dumper"]GitHub - Deadlock Nightmare Dumper[/URL]

I added a config file for webhooks that's ignored by git, so you don't accidentally leak your tokens.

Hope this helps you guys build some cool stuff. Feel free to fork or open a PR if you find something that needs fixing.

Cheers,
[B]0xThiagoAmaral[/B]
[/CONTENT]
