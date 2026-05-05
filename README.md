# 🌑 Deadlock Nightmare Dumper - Ultimate Source 2 Offset Engine

![GitHub stars](https://img.shields.io/github/stars/0xThiagoAmaral/Deadlock-Nightmare-Dumper?style=for-the-badge&color=gold)
![Deadlock](https://img.shields.io/badge/Game-Deadlock-red?style=for-the-badge)
![Engine](https://img.shields.io/badge/Engine-Source_2-orange?style=for-the-badge)

**Deadlock-Nightmare-Dumper** is an industrial-grade **Offset & Schema Dumper** for Valve's Deadlock. It doesn't just find offsets; it provides a full development ecosystem with multi-language SDK generation and real-time notifications.

> [!IMPORTANT]
> **Pro Edition Features Now Available**: C# SDK support and Discord Webhook integration.

## 🎯 Key Features
- **Dynamic Crawler**: Automatically indexes all **33+ heroes** (including Labs/Hidden pawns).
- **Multi-Language SDK Generation**:
  - **C++ (`.hpp`)**: Organized namespaces with `constexpr` performance.
  - **C# (`.cs`)**: Static classes for easy integration with .NET loaders.
  - **JSON**: Structured data for Lua and Python scripts.
- **Discord Webhook Integration**: Get notified instantly when offsets are updated.
- **Pattern Scanning (AoB)**: Resilient signatures for `EntityList`, `LocalPlayer`, and `ViewMatrix`.
- **Real-Time Validation**: Built-in memory validator to ensure 100% data integrity.

## 🛠️ Configuration (`config.json`)
Manage your dumper settings without touching the source code:
```json
{
  "discord_webhook": "YOUR_WEBHOOK_URL",
  "generate_csharp": true,
  "generate_cpp": true
}
```

## 🚀 Usage
1. **Setup**: `pip install -r requirements.txt`
2. **Run**: `python nightmare_dumper.py`
3. **Deploy**: Copy the generated `.hpp` or `.cs` to your project and start coding!

## 🏷️ GitHub Topics
`deadlock`, `deadlock-game`, `source-2`, `offset-dumper`, `schema-system`, `game-hacking`, `reverse-engineering`, `cheat-development`, `csharp-sdk`, `cpp-sdk`, `discord-webhook`

---
*Developed by 0xThiagoAmaral. For educational and research purposes only.*
