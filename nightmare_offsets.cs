namespace NightmareOffsets {
    public static class Globals {
        public const nint dwEntityList = 0x3761a58;
        public const nint dwLocalPlayerController = 0x37665e0;
        public const nint dwViewMatrix = 0x376bd40;
        public const nint dwGlobalVars = 0x0;
    }
    public static class Offsets {
        public static class C_BaseEntity {
            public const nint m_iHealth = 0x334;
            public const nint m_iMaxHealth = 0x330;
            public const nint m_lifeState = 0x33c;
            public const nint m_iTeamNum = 0x3e3;
            public const nint m_pGameSceneNode = 0x310;
            public const nint m_bSpotted = 0x2218;
            public const nint m_vecAbsVelocity = 0x404;
            public const nint m_fFlags = 0x3c8;
        }
        public static class CGameSceneNode {
            public const nint m_vecAbsOrigin = 0xc8;
            public const nint m_vecAbsVelocity = 0x38;
            public const nint m_modelState = 0x170;
            public const nint m_pBoneArray = 0x1f0;
        }
        public static class CCitadelPlayerController {
            public const nint m_hHeroPawn = 0x8ac;
            public const nint m_iszPlayerName = 0x6f0;
            public const nint m_angEyeAngles = 0x6c4;
            public const nint m_nPlayerLevel = 0x7a0;
            public const nint m_iKillStreak = 0x7b0;
            public const nint m_vecInventory = 0x1110;
            public const nint m_iNetWorth = 0x618;
        }
        public static class C_BasePlayerPawn {
            public const nint m_hActiveWeapon = 0x1030;
            public const nint m_iClip1 = 0x10a0;
            public const nint m_hAbilities = 0x1b10;
            public const nint m_vecViewOffset = 0x418;
        }
        public static class C_BaseAbility {
            public const nint m_flNextReadyTime = 0x5d8;
            public const nint m_flNextPrimaryAttack = 0x168;
            public const nint m_nCharges = 0x5ec;
            public const nint m_unLevel = 0x5f8;
        }
    }
}
