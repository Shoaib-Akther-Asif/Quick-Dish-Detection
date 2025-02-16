from fastai.vision.all import load_learner
import gradio as gr

food_labels = (
    'bbq ribs',
    'burger',
    'cheesecake',
    'curry',
    'donut',
    'dumplings',
    'fried chicken',
    'fries', 'hot dog',
    'ice cream',
    'noodles',
    'omelette',
    'pancakes',
    'pasta',
    'pizza',
    'rice dish',
    'salad',
    'sandwich',
    'smoothie',
    'soup',
    'steak',
    'stew',
    'sushi',
    'taco',
    'waffles'
)
label_mapping = {
    "bbq ribs": "BBQ Ribs 🍖",
    "burger": "Burger 🍔",
    "cheesecake": "Cheesecake 🍰",
    "curry": "Curry 🍛",
    "donut": "Donut 🍩",
    "dumplings": "Dumplings 🥟",
    "fried chicken": "Fried Chicken 🍗",
    "fries": "Fries 🍟",
    "hot dog": "Hot Dog 🌭",
    "ice cream": "Ice Cream 🍨",
    "noodles": "Noodles 🍜",
    "omelette": "Omelette 🥚",
    "pancakes": "Pancakes 🥞",
    "pasta": "Pasta 🍝",
    "pizza": "Pizza 🍕",
    "rice dish": "Rice Dish 🍚",
    "salad": "Salad 🥗",
    "sandwich": "Sandwich 🥪",
    "smoothie": "Smoothie 🥤",
    "soup": "Soup 🍲",
    "steak": "Steak 🥩",
    "stew": "Stew 🍛",
    "sushi": "Sushi 🍣",
    "taco": "Taco 🌮",
    "waffles": "Waffles 🧇"
}
model = load_learner('model/food-recognizer-v1.pkl')

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    predictions_dict = dict(zip(food_labels, map(float, probs))) # Convert probs to dictionary
    # Get the label with the highest probability
    top_label = max(predictions_dict, key=predictions_dict.get)
    top_prob = predictions_dict[top_label]  # Get the highest probability
    formatted_label = label_mapping.get(top_label, top_label)
    return f"Selected item is {formatted_label}"

image = gr.Image(type="pil")
label = gr.Label()
examples = [
    'test_item/check_0.jpg',
    'test_item/check_1.jpg',
    'test_item/check_2.jpg',
    'test_item/check_3.jpg',
    'test_item/check_4.jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)