# TestePDF
Leitura de PDF e retirada de tabelas do arquivo

## Comandos de atualização do repositório

Para atualizar o repositório Github, basta ter o Git instalado e seguir os seguintes passos:

  0. Certifique que o repositório foi criado. Acesse o repositório -> `git clone caminhodorepositorio`   

  1. Certifique-se que você está na branch desejada -> `git branch nomedabranch`
  2. Atualize a branch principal do projeto -> `git pull origin main`
  3. Mescle as mudanças da branch de desenvolvimento na branch principal -> `git checkout main` e em seguida `git merge nomedabranch`
  4. Verifique se os arquivos já estão prontos para o commit -> `git status` (Se estiverem vermelhos, continuar no passo 5. Se estiverem verdes, pular para o passo 6.)
  5. Adicione todas as mudanças -> `git add .`
  6. Commit das mudanças -> `git commit -m "Mensagem de integração das mudanças"`
  7. Atualize o repositório Github -> `git push origin main`
  
(OPCIONAL) Caso não vá utilizar mais a branch, poderá excluí-la com os seguintes comandos:
* Excluir localmente -> `git branch -d nomedabranch`
* Excluir remotamente -> `git push origin --delete nomedabranch`
