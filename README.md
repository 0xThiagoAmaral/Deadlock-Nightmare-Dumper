# 🌑 NightmareDumper - Deadlock Offset Engine

![Deadlock](https://img.shields.io/badge/Game-Deadlock-red?style=for-the-badge)
![Engine](https://img.shields.io/badge/Engine-Source_2-orange?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)

O **NightmareDumper** é um motor de extração de offsets de nível industrial para o jogo **Deadlock (Source 2)**. Ele utiliza técnicas avançadas de *Pattern Scanning* e *Schema Walking* para garantir que seu cheat/loader esteja sempre atualizado com a build mais recente do jogo.

## 🚀 Funcionalidades

- **Pattern Scanning (AoB)**: Localiza endereços globais (`EntityList`, `LocalPlayer`, `ViewMatrix`) via assinaturas de bytes resilientes.
- **Real-Time Schema Walker**: Extrai membros de classe (`m_iHealth`, `m_hPawn`, etc.) diretamente da memória do jogo, ignorando a necessidade de atualizações manuais constantes.
- **Dual Mode**: Suporte para extração online (processo vivo) com validação de memória.
- **Output JSON**: Gera um arquivo estruturado pronto para ser consumido por loaders C++, C# ou scripts Lua.

## 🛠️ Como Usar

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o Dumper**:
   Certifique-se de que o **Deadlock** está aberto e você está no menu principal ou em uma partida.
   ```bash
   python nightmare_dumper.py
   ```

3. **Verifique os Resultados**:
   O arquivo `nightmare_offsets.json` será geratedo na raiz do diretório com os dados mais recentes.

## 📁 Estrutura de Arquivos

- `nightmare_dumper.py`: O núcleo do motor de extração.
- `nightmare_offsets.json`: Dados finais para o seu cheat.
- `nightmare_validator.py`: Ferramenta de prova real para validar se os offsets estão lendo dados corretos da memória.
- `docs/Notas_Reversing.md`: Documentação técnica das vtables e assinaturas.

## 🛡️ OpSec & Segurança

> [!WARNING]
> Este projeto é apenas para fins educacionais e de pesquisa em Engenharia Reversa. O uso em servidores oficiais pode resultar em banimento. O dumper foi desenhado para ser furtivo, mas use por sua conta e risco.

---
*Desenvolvido por Nightmare Dev Team.*
