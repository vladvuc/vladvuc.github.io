# The beginning

Once upon a time, in a small town nestled amidst rolling hills, this is just an example of a website.

Inspired by the digital age, the quest has been to put the website on the internet.

<img align="right" width="100" height="100"  title="Image title" alt="Another image" width="350" src="files/img/favicon.png">

![Example image]('files/img/Vlad_profile_xs.png', "Hello")

## The Wolfman

The term **Wolfman** typically refers to a fictional character or archetype commonly found in folklore, mythology, and popular culture. The Wolfman is often depicted as a human who possesses the ability to transform into a wolf or a wolf-like creature, typically during the full moon.

The concept of the Wolfman has its roots in various mythologies and legends, such as werewolf folklore. 

<img align="left" width="180" title="My image" alt="My profile image" src="files/img/Vlad_profile_xs.png" style="border-radius:50%">

## Lightning

Lightning is a natural electrical discharge that occurs during thunderstorms, captivating us with its awe-inspiring displays of raw power and natural beauty. It is a result of the buildup and discharge of electrical energy within clouds or between clouds and the ground. When the electrical charge within a storm cloud becomes imbalanced, it seeks a path of least resistance to neutralize the charge. This rapid discharge of electricity generates a bolt of lightning, which can branch out in intricate patterns across the sky.

```sql
SELECT first_name
FROM patients
whise allergy IS NULL;
```

### Example of third heading

H<sub>2</sub>O

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