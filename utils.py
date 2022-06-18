import os
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


VALID_ARTICLES = ('hat', 'top', 'bottom', 'shoes', 'outerwear', 'accessories')


def sample_items(article, n_samples=1):
    """
    Returns paths of sampled clothing articles
    :param article: the type of clothing to be sampled. Possible values are
                    ('hat', 'top', 'bottom' 'shoes' 'outerwear', 'accessories')
    :param n_samples: Number of sampled articles
    :return: List of paths to sampled articles
    """

    global VALID_ARTICLES
    if article not in VALID_ARTICLES:
        raise ValueError(f"{article} is not a valid clothing type, valid type are {VALID_ARTICLES}")

    path = "./clothes"
    if article == 'hat':
        path += "/hats"
    elif article == 'top':
        path += "/top"
    elif article == 'bottom':
        path += "/bottom"
    elif article == 'shoes':
        path += "/shoes"
    elif article == 'outerwear':
        path += "/outerwear"
    elif article == 'accessories':
        path += "/accessories"
    else:
        print("imposs")

    # make a list of the paths to all objects
    articles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # make a list numbers 0 - (len(paths) - 1)
    possible_indices = [i for i in range(len(articles))]

    sampled_indices = []
    for n in range(n_samples):
        # sample a number from that list, remove it from the list
        sampled_indices.append(possible_indices.pop(random.randrange(len(possible_indices))))

    # place the paths of sampled indices in the list, return it
    sampled_articles_paths = [path + "/" + articles[i] for i in sampled_indices]
    return sampled_articles_paths


def generate_outfit(outerwear=False, hat=False, n_tops=1, n_accessories=0):

    articles_to_sample = ['top', 'bottom', 'shoes']
    if hat:
        articles_to_sample.append('hat')
    if outerwear:
        articles_to_sample.append('outerwear')
    if n_accessories > 0:
        articles_to_sample.append('accessories')

    sampled_articles_paths = {
        'hat': None,
        'top': None,
        'bottom': None,
        'shoes': None,
        'outerwear': None,
        'accessories': None
    }

    for article in articles_to_sample:
        n_samples = 1
        if article == 'top':
            n_samples = n_tops
        if article == 'accessories':
            n_samples = n_accessories

        sampled_articles_paths[article] = sample_items(article, n_samples=n_samples)

    return sampled_articles_paths


def show_fit(generated_fit):
    n_articles_total = 0
    articles_flat_list = []
    for key in generated_fit:
        if generated_fit[key] is not None:
            n_articles_total += len(generated_fit[key])
            articles_flat_list.append([article_path for article_path in generated_fit[key]])

    articles_flat_list = list(np.concatenate(articles_flat_list).flat)

    fig, axes = plt.subplots(1, n_articles_total, figsize=(16, 8))
    for idx, path in enumerate(articles_flat_list):
        axes[idx].imshow(mpimg.imread(path))
        axes[idx].axis('off')

    plt.show()
    plt.close(fig)




if __name__ == "__main__":
    generated_fit = generate_outfit(outerwear=True, hat=True, n_accessories=2)
    print(generated_fit)
    show_fit(generated_fit)
