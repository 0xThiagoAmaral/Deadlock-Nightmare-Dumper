#pragma once
#include <cstddef>

namespace Nightmare {
    namespace Globals {
        constexpr std::ptrdiff_t dwEntityList = 0x3761a58;
        constexpr std::ptrdiff_t dwLocalPlayerController = 0x37665e0;
        constexpr std::ptrdiff_t dwViewMatrix = 0x376bd40;
        constexpr std::ptrdiff_t dwGlobalVars = 0x0;
    }

    namespace Offsets {
        namespace C_BaseEntity {
            constexpr std::ptrdiff_t m_iHealth = 0x334;
            constexpr std::ptrdiff_t m_iMaxHealth = 0x330;
            constexpr std::ptrdiff_t m_lifeState = 0x33c;
            constexpr std::ptrdiff_t m_iTeamNum = 0x3e3;
            constexpr std::ptrdiff_t m_pGameSceneNode = 0x310;
            constexpr std::ptrdiff_t m_bSpotted = 0x2218;
            constexpr std::ptrdiff_t m_vecAbsVelocity = 0x404;
        }
        namespace CGameSceneNode {
            constexpr std::ptrdiff_t m_vecAbsOrigin = 0xc8;
            constexpr std::ptrdiff_t m_vecAbsVelocity = 0x38;
            constexpr std::ptrdiff_t m_modelState = 0x170;
        }
        namespace CCitadelPlayerController {
            constexpr std::ptrdiff_t m_hHeroPawn = 0x8ac;
            constexpr std::ptrdiff_t m_iszPlayerName = 0x6f0;
            constexpr std::ptrdiff_t m_angEyeAngles = 0x6c4;
            constexpr std::ptrdiff_t m_iPlayerState = 0x8b4;
            constexpr std::ptrdiff_t m_vecInventory = 0x1110;
        }
        namespace C_BasePlayerPawn {
            constexpr std::ptrdiff_t m_hActiveWeapon = 0x1030;
            constexpr std::ptrdiff_t m_iClip1 = 0x10a0;
            constexpr std::ptrdiff_t m_hAbilities = 0x1b10;
        }
        namespace C_BaseAbility {
            constexpr std::ptrdiff_t m_flNextReadyTime = 0x5d8;
            constexpr std::ptrdiff_t m_nCharges = 0x5ec;
            constexpr std::ptrdiff_t m_unLevel = 0x5f8;
        }
    }
}
