# Notas de Reversing - NightmareDumper

## Estado Atual
- Projeto migrado para Python (Industrialização).
- Dependências: `pymem`.
- Foco: Deadlock (Source 2).
- Base: cs2-dumper + lógica customizada de Schema.

## Descobertas Técnicas

### ISchemaSystem VTable (schemasystem.dll)
| Índice | Função | Descrição |
|--------|--------|-----------|
| 11 (0x58) | `GetAllTypeScopes` | Retorna vetor de contextos (client, engine, etc). |
| 13 (0x68) | `FindTypeScopeForModule` | Busca contexto por nome de módulo. |

### Estruturas Core
| Estrutura | Offset/Tamanho (CS2) | Offset/Tamanho (Deadlock) | Nota |
|-----------|----------------------|---------------------------|------|
| `CEntityIdentity` | `0x78` | `0x70` | Reduzido em 8 bytes. |

### Classes Alvo
- `CCitadelPlayerController` (Antigo `CCSPlayerController`)
- `CCitadelPlayerPawn` (Antigo `CCSPlayerPawn`)

## Assinaturas (AoB)
*A serem validadas:*
- `dwEntityList`: `48 8B 0D ?? ?? ?? ?? 48 89 7C 24 ?? 8B C1 C1 E9 09`
- `dwLocalPlayerController`: `48 8B 05 ?? ?? ?? ?? 48 85 C0 74 4F`
- `dwViewMatrix`: `48 8D 0D ?? ?? ?? ?? 48 C1 E0 06`
