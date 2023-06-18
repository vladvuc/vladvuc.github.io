---
name: "Venus"
discoverer: "Galileo Galilei"
---

# The beginning

Once upon a time, in a small town nestled amidst rolling hills, there lived a creative and ambitious individual boy. The boy had a passion for storytelling and wanted to share her tales with the world. However, she realized that traditional means of publishing limited her reach.

Inspired by the digital age, the boy decided to embark on a new adventure—creating her own website. Armed with determination and a vision, she set out on a quest to bring her stories to life on the vast landscape of the internet.

<img align="right" width="100" height="100"  title="Image title" alt="Another image" width="350" src="files/img/favicon.png">

## The Wolfman

The term **Wolfman** typically refers to a fictional character or archetype commonly found in folklore, mythology, and popular culture. The Wolfman is often depicted as a human who possesses the ability to transform into a wolf or a wolf-like creature, typically during the full moon.

The concept of the Wolfman has its roots in various mythologies and legends, such as werewolf folklore. 

<img align="left" width="180" title="My image" alt="My profile image" src="files/img/Vlad_profile_xs.png" style="border-radius:50%">

## Lightning

Lightning is a natural electrical discharge that occurs during thunderstorms, captivating us with its awe-inspiring displays of raw power and natural beauty. It is a result of the buildup and discharge of electrical energy within clouds or between clouds and the ground. When the electrical charge within a storm cloud becomes imbalanced, it seeks a path of least resistance to neutralize the charge. This rapid discharge of electricity generates a bolt of lightning, which can branch out in intricate patterns across the sky.

```sql
SELECT first_name
FROM patients
where allergy IS NULL;
```

### Example of third heading

H<sub>2</sub>O

## Trying to figure out LaTeX

```latex
a_1 = b_1 + c_1  
a_2 = b_2 + c_2 - d_2 + e_2
```

Из неког разлога Латекс не функционише, па не знам како ћемо то да решимо, али знам да хоћемо.

Atoms are the fundamental building blocks of matter, the smallest units that retain the characteristics of an element. Composed of a dense nucleus containing protons and neutrons, surrounded by a cloud of electrons, atoms exhibit incredible diversity and form the basis of everything we see in the universe. They combine and interact to create molecules, which in turn give rise to the vast array of substances and materials around us. Understanding the behavior and properties of atoms has been crucial in advancing fields such as chemistry and physics, shaping our understanding of the world at the most fundamental level. Atoms are remarkable in their simplicity yet hold the key to unraveling the complexities of the universe.

> Ths is a Python script:
>> THIS IS ANOTHER LINE INSIDE OF LINE

```python
def get_invoice(arg):
    data = pd.read_csv("data/taxes-all.csv")
    index = -1
    if arg == 'total':
        last_element = data['Invoice_No'].iloc[index]
        while 'VUC' not in last_element:
            index -= 1
            last_element = data['Invoice_No'].iloc[index]
        invoice = last_element[-2:]
    elif arg == 'current':
        last_element = data['Invoice_No'].iloc[-1]
        invoice = last_element[-6:-3]
    return int(invoice)
```