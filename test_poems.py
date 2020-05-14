from Poem import Poem
from Poem_database import Poem_database

test_poems = [
    # 3 paragraphs string
    "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a "
    "horrible vermin. \n He lay on his armour-like back, and if he lifted his head a little he could see his brown "
    "belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and "
    "seemed ready to slide off any moment. \n His many legs, pitifully thin compared with the size of the rest of "
    "him, waved about helplessly as he looked. \"What's happened to me? \" he thought. It wasn't a dream. His room, "
    "a proper human room although a little too small, lay peacefully between its four familiar walls.",
    # 1400 characters string with spaces and points
    "The European languages are members of the same family. Their separate existence is a myth. For science, music, "
    "sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and "
    "their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay "
    "expensive translators. \n To achieve this, it would be necessary to have uniform grammar, pronunciation and more "
    "common words. If several languages coalesce, the grammar of the resulting language is more simple and regular "
    "than that of the individual languages. The new common language will be more simple and regular than the existing "
    "European languages. It will be as simple as Occidental; in fact, it will be Occidental. \n To an English person, "
    "it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is. The "
    "European languages are members of the same family. Their separate existence is a myth. For science, music, "
    "sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and "
    "their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay "
    "expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more "
    "common words. If several languages coalesce, the grammar of the resulting language is more simple and regular "
    "than that of the individual languages. ",
    # 850 words with spaces, no points (merci Marcel)
    "Sans honneur que précaire, sans liberté que provisoire, jusqu’à la découverte du crime ; sans situation "
    "qu’instable, comme pour le poète la veille fêté dans tous les salons, applaudi dans tous les théâtres de "
    "Londres, chassé le lendemain de tous les garnis sans pouvoir trouver un oreiller où reposer sa tête, tournant la "
    "meule comme Samson et disant comme lui : “Les deux sexes mourront chacun de son côté” ; exclus même, "
    "hors les jours de grande infortune où le plus grand nombre se rallie autour de la victime, comme les juifs "
    "autour de Dreyfus, de la sympathie – parfois de la société – de leurs semblables, auxquels ils donnent le dégoût "
    "de voir ce qu’ils sont, dépeint dans un miroir, qui ne les flattant plus, accuse toutes les tares qu’ils "
    "n’avaient pas voulu remarquer chez eux-mêmes et qui leur fait comprendre que ce qu’ils appelaient leur amour (et "
    "à quoi, en jouant sur le mot, ils avaient, par sens social, annexé tout ce que la poésie, la peinture, "
    "la musique, la chevalerie, l’ascétisme, ont pu ajouter à l’amour) découle non d’un idéal de beauté qu’ils ont "
    "élu, mais d’une maladie inguérissable ; comme les juifs encore (sauf quelques-uns qui ne veulent fréquenter que "
    "ceux de leur race, ont toujours à la bouche les mots rituels et les plaisanteries consacrées) se fuyant les uns "
    "les autres, recherchant ceux qui leur sont le plus opposés, qui ne veulent pas d’eux, pardonnant leurs "
    "rebuffades, s’enivrant de leurs complaisances ; mais aussi rassemblés à leurs pareils par l’ostracisme qui les "
    "frappe, l’opprobre où ils sont tombés, ayant fini par prendre, par une persécution semblable à celle d’Israël, "
    "les caractères physiques et moraux d’une race, parfois beaux, souvent affreux, trouvant (malgré toutes les "
    "moqueries dont celui qui, plus mêlé, mieux assimilé à la race adverse, est relativement, en apparence, "
    "le moins inverti, accable celui qui l’est demeuré davantage), une détente dans la fréquentation de leurs "
    "semblables, et même un appui dans leur existence, si bien que, tout en niant qu’ils soient une race (dont le nom "
    "est la plus grande injure), ceux qui parviennent à cacher qu’ils en sont, ils les démasquent volontiers, "
    "moins pour leur nuire, ce qu’ils ne détestent pas, que pour s’excuser, et allant chercher comme un médecin "
    "l’appendicite l’inversion jusque dans l’histoire, ayant plaisir à rappeler que Socrate était l’un d’eux, "
    "comme les Israélites disent de Jésus, sans songer qu’il n’y avait pas d’anormaux quand l’homosexualité était la "
    "norme, pas d’anti-chrétiens avant le Christ, que l’opprobre seul fait le crime, parce qu’il n’a laissé subsister "
    "que ceux qui étaient réfractaires à toute prédication, à tout exemple, à tout châtiment, en vertu d’une "
    "disposition innée tellement spéciale qu’elle répugne plus aux autres hommes (encore qu’elle puisse s’accompagner "
    "de hautes qualités morales) que de certains vices qui y contredisent comme le vol, la cruauté, la mauvaise foi, "
    "mieux compris, donc plus excusés du commun des hommes ; formant une franc-maçonnerie bien plus étendue, "
    "plus efficace et moins soupçonnée que celle des loges, car elle repose sur une identité de goûts, de besoins, "
    "d’habitudes, de dangers, d’apprentissage, de savoir, de trafic, de glossaire, et dans laquelle les membres "
    "mêmes, qui souhaitent de ne pas se connaître, aussitôt se reconnaissent à des signes naturels ou de convention, "
    "involontaires ou voulus, qui signalent un de ses semblables au mendiant dans le grand seigneur à qui il ferme la "
    "portière de sa voiture, au père dans le fiancé de sa fille, à celui qui avait voulu se guérir, se confesser, "
    "qui avait à se défendre, dans le médecin, dans le prêtre, dans l’avocat qu’il est allé trouver; tous obligés à "
    "protéger leur secret, mais ayant leur part d’un secret des autres que le reste de l’humanité ne soupçonne pas et "
    "qui fait qu’à eux les romans d’aventure les plus invraisemblables semblent vrais, car dans cette vie romanesque, "
    "anachronique, l’ambassadeur est ami du forçat : le prince, avec une certaine liberté d’allures que donne "
    "l’éducation aristocratique et qu’un petit bourgeois tremblant n’aurait pas en sortant de chez la duchesse, "
    "s’en va conférer avec l’apache ; partie réprouvée de la collectivité humaine, mais partie importante, "
    "soupçonnée là où elle n’est pas, étalée, insolente, impunie là où elle n’est pas devinée; comptant des adhérents "
    "partout, dans le peuple, dans l’armée, dans le temple, au bagne, sur le trône; vivant enfin, du moins un grand "
    "nombre, dans l’intimité caressante et dangereuse avec les hommes de l’autre race, les provoquant, jouant avec "
    "eux à parler de son vice comme s’il n’était pas sien, jeu qui est rendu facile par l’aveuglement ou la fausseté "
    "des autres, jeu qui peut se prolonger des années jusqu’au jour du scandale où ces dompteurs sont dévorés ; "
    "jusque-là obligés de cacher leur vie, de détourner leurs regards d’où ils voudraient se fixer, de les fixer sur "
    "ce dont ils voudraient se détourner, de changer le genre de bien des adjectifs dans leur vocabulaire, "
    "contrainte sociale, légère auprès de la contrainte intérieure que leur vice, ou ce qu’on nomme improprement "
    "ainsi, leur impose non plus à l’égard des autres mais d’eux-mêmes, et de façon qu’à eux-mêmes il ne leur "
    "paraisse pas un vice.",
    # 290 characters string, no spaces
    "ze2o9pDPNRAyH0oGyL8nuQL4uoiVKO4aR1w4ItcN1lEe3WdZcYLNqSkHYzQZi817CcurgjPEbbhkjIGhxr6PjVnq4zXxGF4deTdebx9Cox1YPjd2ND0"
    "A4syUxeQjPqoeVosodw98cBmugixPPl3poPeJJMzde9Dp6U0qvp3NLUGCWDFdEyWwyWim7UHoUmcD1dKAt5RRaROZdXdwKjAKcPE913RoktFImpSpTH"
    "csuB2RdluJDNds5N8XHZ1YWSswnu2UigQAJRhLs1bUwwsAZttvCjBJn4fjA2 ",
    # Inferno string : everything is mixed
    "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a "
    "horrible vermin. \n Sans honneur que précaire, sans liberté que provisoire, jusqu’à la découverte du crime ; sans situation "
    "qu’instable, comme pour le poète la veille fêté dans tous les salons, applaudi dans tous les théâtres de "
    "Londres, chassé le lendemain de tous les garnis sans pouvoir trouver un oreiller où reposer sa tête, tournant la "
    "meule comme Samson et disant comme lui : “Les deux sexes mourront chacun de son côté” ; exclus même, "
    "hors les jours de grande infortune où le plus grand nombre se rallie autour de la victime, comme les juifs "
    "autour de Dreyfus, de la sympathie – parfois de la société – de leurs semblables, auxquels ils donnent le dégoût "
    "de voir ce qu’ils sont, dépeint dans un miroir, qui ne les flattant plus, accuse toutes les tares qu’ils "
    "n’avaient pas voulu remarquer chez eux-mêmes et qui leur fait comprendre que ce qu’ils appelaient leur amour (et "
    "à quoi, en jouant sur le mot, ils avaient, par sens social, annexé tout ce que la poésie, la peinture, "
    "la musique, la chevalerie, l’ascétisme, ont pu ajouter à l’amour) découle non d’un idéal de beauté qu’ils ont "
    "élu, mais d’une maladie inguérissable ; comme les juifs encore (sauf quelques-uns qui ne veulent fréquenter que "
    "\n His many legs, pitifully thin compared with the size of the rest of "
    "him, waved about helplessly as he looked. \"What's happened to me? \" he thought. It wasn't a dream. His room, "
    "a proper human room although a little too small, ze2o9pDPNRAyH0oGyL8nuQL4uoiVKO4aR1w4ItcN1lEe3WdZcYLNqSkHYzQZi817CcurgjPEbbhkjIGhxr6PjVnq4zXxGF4deTdebx9Cox1YPjd2ND0"
    "A4syUxeQjPqoeVosodw98cBmugixPPl3poPeJJMzde9Dp6U0qvp3NLUGCWDFdEyWwyWim7UHoUmcD1dKAt5RRaROZdXdwKjAKcPE913RoktFImpSpTH "
    "csuB2RdluJDNds5N8XHZ1YWSswnu2UigQAJRhLs1bUwwsAZttvCjBJn4fjA2 lay peacefully between its four familiar walls."
]

title_tests = [
    "Bannières de mai",
    "Automne",
    "Emma",
    "Le fils des armures",
    "L'abandon",
    "Aux Champs Élyséens",
    "Le confiteor de l'artiste",
    "La Gitana"
]

for test in title_tests:
    random_poem = Poem_database.query.filter_by(title=test).all()[0]
    poem = Poem(
        author=random_poem.author,
        title=random_poem.title,
        content=random_poem.content
    )
    print(f"Poem {poem.title}")
    poem.parse()
    print("Parsed poem :")
    print(*poem.parsed_content, sep="\n +")


for test in test_poems:
    print("\n\n\n")
    poem = Poem(
        content=test
    )
    poem.parse()
    print("Parsed poem :")
    print(*poem.parsed_content, sep="\n +")
