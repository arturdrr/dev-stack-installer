# Dev Stack Ultra Completa

Este repositório contém scripts e configurações para configurar uma Dev Stack completa, otimizada para diferentes ambientes: local e VPS.

## Estrutura do Repositório

- **`local-install/`**: Contém scripts e configurações para a instalação da dev stack em um ambiente de desenvolvimento local (sua máquina).
- **`vps-install/`**: Contém scripts e configurações para a instalação da dev stack completa em um servidor VPS (Virtual Private Server).
- **`docs/`**: Documentação adicional sobre a arquitetura, melhores práticas e outros tópicos relevantes.

## Como Usar

Para uma instalação guiada e inteligente, utilize o script Python interativo na raiz deste repositório. Para instalações não interativas ou específicas de ambiente, consulte os scripts em `local-install/` ou `vps-install/`.

## Como Usar o Instalador Python Interativo

1.  **Execute o instalador**:
    ```bash
    python3 installer.py
    ```
2.  **Siga o menu**: O instalador apresentará um menu onde você pode escolher quais etapas deseja executar ou iniciar a instalação completa.
3.  **Retomar instalação**: Em caso de interrupção ou erro, você pode executar o script novamente. Ele retomará do último ponto de verificação salvo.

Logs detalhados da instalação são gravados em `devstack_install.log` e o checkpoint em `install_checkpoint.txt`.

## Ordem de Instalação Inteligente

A instalação segue uma ordem inteligente para garantir que todas as dependências e ferramentas essenciais estejam disponíveis antes das ferramentas que delas dependem, evitando falhas e garantindo um ambiente funcional desde o início.

Cada etapa verifica se a ferramenta ou dependência já está instalada para evitar reinstalação desnecessária. Os scripts são criados para falhar caso dependam de uma etapa não concluída, garantindo execução sequencial correta. Há também a possibilidade de retomar a instalação em caso de erro, identificando o último passo completado, e configurações adaptativas para diferentes ambientes (local ou VPS), ativando apenas componentes relevantes.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).