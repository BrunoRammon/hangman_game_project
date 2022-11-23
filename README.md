# Jogo da forca (Hangman game)
Um jogo da forca desenvolvido com uso do streamlit

- Para executar localmente clone o repositório e dentro da pasta execute o comando:
<code>streamlit run src_streamlit.py</code>

- Assim que a linha de comando for executada uma nova aba aprecerá no seu browser com uma tela semelhante a esta:
<p align="center">
<img src="/tutorial_images/tutorial_img_1.png" alt="drawing" width="700"/>
</p>

- Agora basta escolher uma letra no campo destinado para tal:
<p align="center">
<img src="/tutorial_images/tutorial_img_2.png" alt="drawing" width="700"/>
</p>

- Se for uma letra correta o campo 'Palavra:' será atualizado

- Se não for uma letra correta o campo 'Letras erradas já escolhidas: ' e a imagem da forca serão atualizados:
<p align="center">
<img src="/tutorial_images/tutorial_img_3.png" alt="drawing" width="700"/>
</p>

 - Se após 6 tentativas erradas o usuário não completar a palavra, então o carrasco chutará o balde que apoia o enforcado ('it's sad, but it's true'), terminando o jogo e deixando uma criança muito triste:
 <p align="center">
  <img src="/tutorial_images/tutorial_img_game_over.png" alt="drawing" width="700"/>
 </p>

 - Se o usuário acertar a palavra uma criança feliz comemorará efusivamente sua vitória:
 <p align="center">
  <img src="/tutorial_images/tutorial_img_win.png" alt="drawing" width="700"/>
 </p>
 
 ## Observações:
 - Até o momento uma pequena lista de nome de frutas é usada como banco de palavras. Posteriormente, será usado um banco de palavras maior e mais geral.
