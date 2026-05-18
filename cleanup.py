import bs4

with open('index.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), 'html.parser')

# 1. Remove duplicate facebook logos in utility bar
si_row = soup.find('div', class_='si-row')
if si_row:
    # remove all facebook logos
    for a in si_row.find_all('a', class_='si'):
        if a.find('i', class_='ph-facebook-logo'):
            a.decompose()
    # add exactly one back
    si_row.append(bs4.BeautifulSoup('<a href="#" class="si"><i class="ph ph-facebook-logo"></i></a>', 'html.parser'))

# 2. Remove duplicate facebook logos in footer
ficons = soup.find('div', class_='ficons')
if ficons:
    for a in ficons.find_all('a', class_='fi'):
        if a.find('i', class_='ph-facebook-logo'):
            a.decompose()
    ficons.append(bs4.BeautifulSoup('<a href="#" class="fi"><i class="ph ph-facebook-logo"></i></a>', 'html.parser'))

# 3. Remove duplicate ecosystem sections
ecosystems = soup.find_all('section', id='ecosystem')
if len(ecosystems) > 1:
    for eco in ecosystems[1:]:
        eco.decompose()

# 4. Fix product images
# The placeholder images available are: cad_ag_radiator_2.png, cad_genset_radiator_2.png, cad_hydraulic_radiator_2.png, cad_mining_cooler_2.png, cad_oil_radiator_2.png, cad_truck_radiator_2.png
# We will just cycle through them for all product cards
placeholders = [
    'cad_ag_radiator_2',
    'cad_genset_radiator_2',
    'cad_hydraulic_radiator_2',
    'cad_mining_cooler_2',
    'cad_oil_radiator_2',
    'cad_truck_radiator_2'
]
pcards = soup.find_all('div', class_='pcard')
for i, pcard in enumerate(pcards):
    img = pcard.find('img')
    if img:
        img['src'] = f'./assets/products/{placeholders[i % len(placeholders)]}.png'

# 5. Fix bucket section grid single column
# The user said bucket cards take up the whole screen as one single column.
# In my eco_style I used `.div-grid`. Let's check where it went wrong.
# `div-grid` is defined inside a <style> tag at the end of <head>.
# The CSS was:
# .div-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
# @media (min-width: 768px) { .div-grid { grid-template-columns: repeat(2, 1fr); } }
# @media (min-width: 1024px) { .div-grid { grid-template-columns: repeat(3, 1fr); } }
# If this CSS isn't working, maybe the <style> block was messed up?
# Or maybe the class is not div-grid? In the DOM: <div class="div-grid">.
# Let's just ensure the CSS is perfectly injected, or just inject inline styles/better classes.
# I'll just find the div-grid and add the style inline or create a proper CSS rule in the main style block.
# I'll extract all styles from the double style tags, and put them cleanly.
for style in soup.find_all('style'):
    if 'div-grid' in style.text:
        style.string = style.text.replace('.div-grid { display: grid;', '.div-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }')

# 6. Make outline CTAs on the hero banner white
hero = soup.find('div', class_='hero')
if hero:
    hero_btn_o = hero.find('button', class_='btn-o')
    if hero_btn_o:
        hero_btn_o['class'] = 'btn-w-o'

# We also need to add `.btn-w-o` and fix `.btn-o:hover`
new_styles = """
/* Fix button hover blending */
.btn-o:hover {
    background: var(--surface-low);
    color: var(--navy);
    border-color: var(--navy);
}

/* White outline button for Hero */
.btn-w-o {
    font-family: var(--HF);
    font-size: 13px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    background: transparent;
    color: #fff;
    border: 1px solid #fff;
    padding: 16px 28px;
    justify-content: center;
    display: inline-flex;
    align-items: center;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
}
.btn-w-o:hover {
    background: #fff;
    color: var(--navy);
}

/* Ensure Bucket Grid works properly */
@media (min-width: 768px) {
    .div-grid { grid-template-columns: repeat(2, 1fr) !important; }
}
@media (min-width: 1024px) {
    .div-grid { grid-template-columns: repeat(3, 1fr) !important; }
}
"""
style_tag = soup.find('style')
if style_tag:
    style_tag.append(new_styles)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
