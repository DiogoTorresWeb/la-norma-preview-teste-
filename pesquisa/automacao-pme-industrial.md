# Automação de chão de fábrica em PME industrial — o que é viável

**Data de acesso:** 28/09/2026 · **Para:** Ato 3 do deck do Daniel.

**Aviso que vale para o documento inteiro:** o que o Diogo observa dentro da fábrica é
observação dele e vai atribuída a ele. O que está pesquisado aqui é **o que a tecnologia
permite**, não o que a La Norma já tem. Em nenhum momento se afirma qual sistema a empresa
usa — isso é pergunta de diagnóstico, não fato.

---

## 1. As quatro dores observadas

Relato do Diogo, que trabalha na montagem:

1. **Etiqueta da máquina (pegatina).** Zebra ZD421 + impressora industrial para a etiqueta da
   caixa. A cada máquina vendida, alguém — o supervisor — fica no computador fazendo as
   etiquetas dos pedidos, uma a uma. Em alta temporada, isso pode tomar quase o dia.
2. **Albarán.** Sempre depende de uma pessoa parada gerando.
3. **Etiqueta da DHL.** Idem.
4. **Pré-montagem.** Projeto que há tempos não sai do papel. O próprio Diogo diz o motivo:
   não é falta de gente tentando, é falta de estrutura e de uma forma controlada de fazer.

O que essas quatro têm em comum: **prendem uma pessoa qualificada em trabalho repetitivo,
em horário em que ela faria falta em outro lugar.** Esse é o argumento, não "a empresa é
desorganizada".

---

## 2. Etiqueta — o caminho técnico

A ZD421 entende **ZPL**, a linguagem de etiqueta da própria Zebra. Isso muda tudo: significa
que a etiqueta é **texto**, e texto se gera em lote.

Três caminhos documentados, do mais simples ao mais integrado:

- **ZPL direto para a impressora** via driver "Generic / Text Only" do Windows — manda-se o
  arquivo, ela imprime ([FolderMill](https://www.foldermill.com/kb/install-generic-text-driver-in-windows),
  [Zebra Support](https://supportcommunity.zebra.com/s/article/Sending-ZPL-Commands-to-a-Printer)).
- **Modelo com variáveis + fonte de dados.** Desenha-se a etiqueta uma vez, com marcadores, e
  cada linha da lista de pedidos vira uma etiqueta. A própria Zebra documenta o padrão de
  carregar um CSV e inserir os dados no ZPL
  ([docs.zebra.com — CSV Program](https://docs.zebra.com/us/en/printers/software/zpl-pg/c-zbi-zbi-commands/r-zbi-example-programs/r-zbi-csv-program.html)).
- **Script com impressoras e etiquetas nomeadas**, imprimindo por nome e substituindo
  variáveis a partir da fonte de dados
  ([exemplo público](https://github.com/sharptree/zebra-printing-scripts)).

**Por que este é o piloto recomendado:** é o mais isolado (não depende de mudar sistema de
ninguém), o mais visível (o resultado é uma pilha de etiquetas saindo sozinha) e o mais fácil
de reverter se não prestar. O ganho é do tipo que se vê no mesmo dia.

**O que precisa ser confirmado antes de prometer qualquer coisa:** como a etiqueta é feita
hoje — que programa, que modelo, e de onde sai a lista de pedidos do dia. Sem isso, qualquer
estimativa é invenção.

## 3. Albarán e etiqueta da DHL

A DHL publica **MyDHL API**, que integra diretamente com o sistema de pedidos e faz três
coisas relevantes: **gerar a etiqueta**, **pedir ou cancelar a recolhida** e **devolver o
rastreamento** para dentro do sistema ([DHL — integrações web](https://www.dhl.com/es-es/ecommerce/home/ecommerce-shipments/web-integrations.html)).

Ou seja: a etiqueta da transportadora deixa de ser um passo manual e passa a ser consequência
do pedido existir.

O albarán segue a mesma lógica — é um documento derivado do pedido. Em ERPs de PME isso já é
comportamento padrão: confirma-se a entrega e o envio é registrado junto com a etiqueta
correspondente (o caso do Odoo é público e bem documentado,
[Odoo — integração DHL](https://www.odoo.com/documentation/17.0/es_419/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials.html)).

**A pergunta que abre a conversa com o Daniel**, e que o deck deve fazer em vez de responder:
*em que sistema o pedido é lançado hoje?* Se existe um sistema central, o trabalho é
integração. Se cada setor tem o seu, o trabalho começa antes — e aí o primeiro ganho é o
lugar único, não a automação.

## 4. Pré-montagem — por que não sai do papel

Aqui a pesquisa é a parte mais útil, porque ela explica o que o Diogo já sentiu sem ter o nome.

**O que é pré-montagem bem feita (kitting):** a montagem controlada de componentes num
conjunto verificado que atende **uma ordem de produção específica**. Feito direito, encurta
troca de setup, elimina procura de peça na linha e evita peça errada — porque empurra a
complexidade para antes da linha, num processo disciplinado
([Racklify](https://racklify.com/encyclopedia/kitting-implementation-and-best-practices/),
[SG Systems](https://sgsystemsglobal.com/glossary/kitting-pre-assembly-for-production/)).

**Por que iniciativas assim falham** — e isso é literatura revisada, não opinião de blog. Uma
revisão sistemática de falhas de melhoria contínua em ambiente industrial identifica os temas
recorrentes: motivos e expectativas, cultura e ambiente, liderança, **abordagem de
implementação**, treinamento, gestão de projeto, **nível de envolvimento dos funcionários** e
retorno de resultado
([Emerald / IJPPM](https://www.emerald.com/ijppm/article/63/3/370/149832),
[Heriot-Watt](https://researchportal.hw.ac.uk/en/publications/failure-of-continuous-improvement-initiatives-in-manufacturing-en/)).
Nenhum deles é "as pessoas não se esforçaram".

Dois achados que batem com o que o Diogo descreve:

- **Boa parte da falha é escolha errada do problema, não execução ruim** — erro de
  identificação a montante responde por algo entre um quinto e um terço das narrativas de
  falha ([Hephanos](https://www.hephanos.com/knowledge/problem-isnt-execution)).
- **Sistema baseado só em documento não segura o conhecimento real.** Procedimento escrito não
  captura o operador que percebe pelo som que a máquina está diferente, nem o inspetor que
  reconhece o defeito limítrofe ([manual.to](https://manual.to/continuous-improvement-why-initiatives-plateau-18-months/)).

**A tradução para o deck:** tentar organizar a pré-montagem "na mão, todo ano" falha por
motivo estrutural conhecido, não por falta de empenho. O caminho que a literatura aponta é o
oposto do documento grande: **checklist digital no ponto de uso**, ligado a uma ordem de
produção, que ao mesmo tempo guia e registra o que aconteceu
([Workerbase](https://medium.com/workerbase/digital-checklists-for-efficient-data-collection-and-standard-work-in-manufacturing-6a088f4027f7),
[Azumuta](https://www.azumuta.com/blog/how-to-digitize-kitting-in-your-manufacturing-processes/)).
O dado que ele gera é o que permite melhorar depois — sem ele, cada tentativa recomeça do zero.

---

## 5. O que o deck pode afirmar, e o que não pode

**Pode:**
- que a ZD421 aceita ZPL e que impressão em lote a partir de uma lista é padrão documentado
  pela Zebra;
- que a DHL oferece API para etiqueta, recolhida e rastreamento;
- que albarán é documento derivado do pedido e que ERPs de PME já fazem isso;
- que a falha de iniciativas de organização de processo tem causa estudada, e que checklist
  digital no ponto de uso é o caminho apontado;
- o que o **Diogo observa** na fábrica — atribuído a ele, como observação.

**Não pode:**
- dizer qual sistema a La Norma usa;
- estimar horas ou dinheiro economizado — **nada foi medido**;
- afirmar que qualquer uma dessas automações é simples antes de ver como o trabalho é feito hoje;
- prometer prazo.

A frase que resolve isso na reunião: *"isto é o que eu vejo de dentro; antes de prometer
qualquer coisa, preciso ver como se faz hoje."* Custa nada e protege tudo.
