import bs4
import re

with open(r'd:\Dev\Thermal-Motion-Group\design-system\tmg_homepage_responsive_sofia.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), 'html.parser')

with open(r'd:\Dev\Thermal-Motion-Group\phase-2-full\index.html', 'r', encoding='utf-8') as f:
    orig_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

# 1. CSS Injection
new_css = """
/* --- NEW PHASE 2 CSS --- */
/* Announcement Bar */
.ann-dots { display:flex; gap:6px; justify-content:center; margin-top:6px; }
.ann-dot { width:6px; height:6px; border-radius:50%; background:#fff; opacity:0.4; transition:opacity 0.2s; }
.ann-dot.active { opacity:1; }

/* Navigation Dropdown */
.nav-dropdown { position:relative; display:flex; align-items:center; }
.dropdown-menu { position:absolute; top:100%; left:50%; transform:translateX(-50%); background:#fff; border:1px solid var(--lines); box-shadow:0 8px 24px rgba(0,0,0,0.08); padding:0; display:none; flex-direction:column; min-width:240px; margin-top:0px; opacity:0; transition:opacity 0.2s, transform 0.2s; pointer-events:none; z-index: 1001; border-radius:0; }
.nav-dropdown:hover .dropdown-menu { display:flex; opacity:1; transform:translateX(-50%) translateY(0); pointer-events:auto; margin-top:0; }
.dm-link { padding:12px 20px; display:block; text-decoration:none; color:var(--navy); font-family:var(--BF); font-size:14px; transition:background 0.2s; }
.dm-link:hover { background:var(--surface-low); color:var(--navy); }
.dm-sub { display:block; font-family:var(--HF); font-size:10px; text-transform:uppercase; letter-spacing:0.15em; color:var(--muted); margin-top:4px; }
.dm-div { height:1px; background:var(--lines); margin:4px 0; }
.dm-all { padding:12px 20px; font-family:var(--HF); font-size:12px; text-transform:uppercase; letter-spacing:0.1em; color:var(--red); text-decoration:none; display:block; }

/* Nav Actions */
.nav-actions { display:flex; gap:20px; align-items:center; }
.nav-icon { font-size:20px; color:var(--navy); cursor:pointer; position:relative; }
.nav-icon:hover { color:var(--red); }
.cart-badge { position:absolute; top:-6px; right:-8px; background:var(--red); color:#fff; font-family:var(--HF); font-size:9px; width:16px; height:16px; display:flex; align-items:center; justify-content:center; }

/* Filter Tabs */
.filter-row { display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:24px; flex-wrap:wrap; gap: 16px; }
.filter-tabs { display:flex; overflow-x:auto; gap:0; scrollbar-width:none; align-items: center; }
.filter-tabs::-webkit-scrollbar { display:none; }
.ftab { padding:10px 20px; font-family:var(--HF); font-size:12px; text-transform:uppercase; letter-spacing:0.1em; color:var(--muted); border-bottom:2px solid transparent; cursor:pointer; white-space:nowrap; }
.ftab.active { color:var(--navy); border-bottom-color:var(--red); }

/* Buttons & Elements */
.btn-s { font-family:var(--HF); font-size:13px; letter-spacing:.1em; text-transform:uppercase; background:var(--navy); color:#fff; border:none; padding:16px 28px; justify-content:center; display:inline-flex; align-items:center; cursor:pointer; transition:background 0.2s; text-decoration:none; }
.btn-s:hover { background:#1e293b; }
.btn-p { font-family:var(--HF); font-size:13px; letter-spacing:.1em; text-transform:uppercase; background:var(--red); color:#fff; border:none; padding:16px 28px; justify-content:center; display:inline-flex; align-items:center; cursor:pointer; transition:background 0.2s; text-decoration:none; }
.btn-p:hover { background:#a02020; }
.btn-o { font-family:var(--HF); font-size:13px; letter-spacing:.1em; text-transform:uppercase; background:transparent; color:var(--navy); border:1px solid var(--navy); padding:16px 28px; justify-content:center; display:inline-flex; align-items:center; cursor:pointer; transition:all 0.2s; text-decoration:none; }
.btn-o:hover { background:var(--surface-low); }
.btn-nl { font-family:var(--HF); font-size:13px; letter-spacing:.1em; text-transform:uppercase; background:var(--pitch); color:#fff; border:none; padding:16px 28px; justify-content:center; display:inline-flex; align-items:center; cursor:pointer; transition:background 0.2s; text-decoration:none; height:48px; }
.btn-nl:hover { background:var(--navy); }

/* Product Carousel & Cards updates */
.prod-grid { align-items: stretch; }
.pc-wrap { display: flex; align-self: stretch; height: auto; }
.pcard { flex: 1; display: flex; flex-direction: column; height: 100%; }
.pcard-body { flex: 1; display: flex; flex-direction: column; }
.pcard .cta-grid { margin-top: auto; }
.pcard .btn-o { margin-top: auto; }
.pcard-img { position:relative; }
.wishlist-btn { position:absolute; top:12px; right:12px; width:32px; height:32px; background:#fff; border:1px solid var(--lines); display:flex; align-items:center; justify-content:center; opacity:0; pointer-events:none; transition:opacity 0.2s; color:var(--red); font-size:18px; cursor:pointer; z-index:10; }
.pcard:hover .wishlist-btn { opacity:1; pointer-events:auto; }

.pcard-price { font-family:var(--HF); font-size:16px; color:var(--navy); font-variant-numeric:tabular-nums; margin-left:auto; }
.pcard-top-row { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; }

.tag-div { background:var(--red); color:#fff; border:1px solid var(--red); }
.tag-ind { background:transparent; color:var(--red); border:1px solid var(--red); }

.cta-grid { display:grid; grid-template-columns:1fr 40px; gap:8px; }
.cart-sq { width:40px; height:40px; background:#fff; border:1px solid var(--lines); display:flex; align-items:center; justify-content:center; cursor:pointer; color:var(--navy); font-size:18px; transition:background 0.2s, border-color 0.2s; }
.cart-sq:hover { background:var(--surface-low); border-color:var(--navy); }

/* Newsletter */
.nl-sec { background:var(--red); padding:40px 20px; position:relative; overflow:hidden; }
.nl-bg-pattern { position:absolute; inset:0; background:repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,0.1) 10px, rgba(255,255,255,0.1) 11px); z-index:0; }
.nl-wrap { display:grid; grid-template-columns:1fr; gap:32px; align-items:center; max-width: 1440px; margin: 0 auto; position:relative; z-index:1; }
.nl-eb { font-family:var(--HF); font-size:12px; text-transform:uppercase; letter-spacing:0.25em; color:rgba(255,255,255,0.8); margin-bottom:12px; }
.nl-h2 { font-family:var(--HF); font-size:32px; text-transform:uppercase; color:#fff; line-height:1.2; margin-bottom:16px; }
.nl-sub { font-family:var(--BF); font-size:15px; color:rgba(255,255,255,0.9); line-height:1.6; }
.nl-form { display:flex; flex-direction:column; gap:12px; }
.nl-inp { height:48px; background:transparent; border:1px solid rgba(255,255,255,0.4); padding:0 20px; font-family:var(--BF); font-size:15px; color:#fff; width:100%; outline:none; transition:border-color 0.2s; border-radius:0; }
.nl-inp:focus { border-color:#fff; }
.nl-inp::placeholder { color:rgba(255,255,255,0.6); }
.nl-note { font-family:var(--BF); font-size:12px; color:rgba(255,255,255,0.7); margin-top:12px; }
@media(min-width:768px) {
    .nl-sec { padding:56px 40px; }
    .nl-wrap { grid-template-columns:1fr 1fr; gap:80px; }
    .nl-form { flex-direction:row; }
    .nl-inp { flex:1; }
}

/* Industries Grid */
.hdr-row { display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:48px; flex-wrap:wrap; gap:20px; }
.hdr-left { flex:1; min-width:300px; margin-bottom:0 !important; }
.ind-grid { display:grid; grid-template-columns:1fr; gap:16px; }
@media(min-width:768px) { .ind-grid { grid-template-columns:1fr 1fr; } }
@media(min-width:1024px) { .ind-grid { grid-template-columns:1fr 1fr 1fr; } }
.ind-card { background:#fff; border:1px solid var(--lines); padding:32px 28px; position:relative; transition:border-color 0.3s; display:flex; flex-direction:column; text-decoration:none; border-radius:0; }
.ind-card .pcard-accent { position:absolute; top:0; left:0; right:0; height:3px; background:transparent; transition:background 0.3s; }
.ind-card:hover { border-color:var(--red); }
.ind-card:hover .pcard-accent { background:var(--red); }
.ind-icon { font-size:28px; color:var(--red); margin-bottom:16px; display:block; }
.ind-title { font-family:var(--HF); font-size:18px; text-transform:uppercase; color:var(--pitch); margin-bottom:8px; }
.ind-desc { font-family:var(--BF); font-size:14px; color:var(--muted); line-height:1.6; }
.ind-link { font-family:var(--HF); font-size:11px; text-transform:uppercase; letter-spacing:0.1em; color:var(--red); margin-top:auto; padding-top:16px; display:block; text-decoration:none; }

/* Testimonials */
.test-layout { display:grid; grid-template-columns:1fr; gap:40px; }
@media(min-width:768px) { .test-layout { grid-template-columns:35% 1fr; gap:60px; } }
.test-list { position:relative; height:180px; overflow:hidden; }
.test-item { display:flex; align-items:center; gap:16px; position:absolute; width:100%; transition:all 0.5s cubic-bezier(0.16,1,0.3,1); }
.ti-img { width:40px; height:40px; border-radius:50%; border:2px solid var(--lines); background:var(--surface); }
.ti-info { display:flex; flex-direction:column; }
.ti-name { font-family:var(--HF); font-size:14px; text-transform:uppercase; letter-spacing:0.05em; color:var(--muted); transition:color 0.5s; }
.ti-rat { font-family:var(--BF); font-size:12px; color:var(--muted); }
.ti-rat span { color:var(--red); }

.test-item.active { opacity:1; transform:translateY(70px) scale(1); z-index:2; pointer-events:auto; }
.test-item.active .ti-img { border-color:var(--red); }
.test-item.active .ti-name { color:var(--pitch); }
.test-item.prev { opacity:0.35; transform:translateY(10px) scale(0.9); z-index:1; pointer-events:none; filter:grayscale(1); }
.test-item.next { opacity:0.35; transform:translateY(130px) scale(0.9); z-index:1; pointer-events:none; filter:grayscale(1); }
.test-item.hidden { opacity:0; transform:translateY(-40px) scale(0.9); pointer-events:none; }

.test-quote-col { border-left:1px solid var(--lines); padding-left:20px; display:flex; flex-direction:column; justify-content:center; }
@media(min-width:768px) { .test-quote-col { padding-left:60px; } }
.tq-mark { font-family:var(--HF); font-size:72px; color:var(--red); opacity:0.15; line-height:0.5; margin-bottom:8px; display:block; }
.tq-text { font-family:var(--BF); font-size:17px; font-style:italic; line-height:1.7; color:var(--deep); transition:opacity 0.4s ease; min-height:80px; margin-bottom:16px; }
.tq-name { font-family:var(--HF); font-size:13px; text-transform:uppercase; color:var(--pitch); }
.tq-co { font-family:var(--BF); font-size:13px; color:var(--muted); }

/* Enquiry Modal */
.modal-ov { position:fixed; inset:0; background:rgba(15,23,42,0.7); backdrop-filter:blur(4px); -webkit-backdrop-filter:blur(4px); z-index:2000; display:flex; align-items:center; justify-content:center; padding:20px; opacity:0; pointer-events:none; transition:opacity 0.3s; }
.modal-ov.open { opacity:1; pointer-events:auto; }
.modal-bx { background:#fff; padding:48px; max-width:560px; width:100%; position:relative; border-radius:0; }
.modal-cl { position:absolute; top:24px; right:24px; font-size:24px; color:var(--muted); cursor:pointer; transition:color 0.2s; }
.modal-cl:hover { color:var(--pitch); }
"""
style_tag = soup.find('style')
style_tag.append(new_css)

# Update DOM

# [01] Announcement Bar
expo_bar = soup.find('div', class_='expo-bar')
expo_bar.clear()
expo_bar['id'] = 'ann-bar'
expo_bar['style'] = 'display:flex; flex-direction:column; justify-content:center; align-items:center; position:relative; min-height:40px;'
expo_bar.append(bs4.BeautifulSoup('''
<div id="ann-text" class="expo-bar-t" style="transition: opacity 0.4s ease;">🔴 EXPO 2026 — Booth 4A · Apr 20–26 · Come find us</div>
''', 'html.parser'))

# [02] Utility Bar
si_row = soup.find('div', class_='si-row')
si_row.append(bs4.BeautifulSoup('<a href="#" class="si"><i class="ph ph-facebook-logo"></i></a>', 'html.parser'))

# [03] Navigation Bar
logo_img = soup.find('div', class_='logo').find('img')
logo_img['src'] = './assets/tmg-logo.svg'

navlinks = soup.find('div', class_='navlinks')
navlinks.clear()
navlinks.append(bs4.BeautifulSoup('''
<a href="#products" class="nl" style="text-decoration:none">Products</a>
<div class="nav-dropdown">
  <span class="nl" style="display:flex; align-items:center; gap:4px;">Solutions <i class="ph ph-caret-down" style="font-size:10px;"></i></span>
  <div class="dropdown-menu">
    <a href="#" class="dm-link">Aftermarket Coolers <span class="dm-sub">TMG E-Commerce</span></a>
    <a href="#" class="dm-link">Power Transformers <span class="dm-sub">Static Products</span></a>
    <a href="#" class="dm-link">Battery Management <span class="dm-sub">Static Products</span></a>
    <a href="#" class="dm-link">CJP Fabrication <span class="dm-sub">External Partner ↗</span></a>
    <a href="#" class="dm-link">Seals, Hydraulics & Valves <span class="dm-sub">External Partner ↗</span></a>
    <a href="#" class="dm-link">Innovation & Prototyping <span class="dm-sub">Custom Services</span></a>
    <div class="dm-div"></div>
    <a href="#" class="dm-all">View All Solutions &rarr;</a>
  </div>
</div>
<a href="#about" class="nl" style="text-decoration:none">About</a>
<a href="#contact" class="nl" style="text-decoration:none">Contact / RFQ</a>
''', 'html.parser'))

# Update nav-right (need to add nav-actions next to hamburger)
hamburger = soup.find('div', class_='hamburger')
nav_actions = bs4.BeautifulSoup('''
<div class="nav-actions">
  <i class="ph ph-magnifying-glass nav-icon"></i>
  <i class="ph ph-user nav-icon desktop-only"></i>
  <div class="nav-icon"><i class="ph ph-shopping-cart"></i><div class="cart-badge" id="cart-b">0</div></div>
</div>
''', 'html.parser')
hamburger.insert_before(nav_actions)

# Update Mobile Menu
mobile_menu = soup.find('div', class_='mobile-menu')
mobile_menu.insert(1, bs4.BeautifulSoup('''
<a href="#" class="mlink" style="text-decoration:none">Solutions <i class="ph ph-caret-down"></i></a>
<div style="background:var(--surface-low); padding:10px 0;">
    <a href="#" class="mlink" style="font-size:14px; border-bottom:none; padding:10px 0;">Aftermarket Coolers</a>
    <a href="#" class="mlink" style="font-size:14px; border-bottom:none; padding:10px 0;">Power Transformers</a>
    <a href="#" class="mlink" style="font-size:14px; border-bottom:none; padding:10px 0;">Battery Management</a>
</div>
''', 'html.parser'))

def make_product_card(name, price, tag1, tags, spec1, spec2, spec3, img_slug, btn_type='buy'):
    tags_html = f'<span class="tag tag-div">{tag1}</span>' + ''.join([f'<span class="tag tag-ind">{t}</span>' for t in tags])
    if btn_type == 'buy':
        cta = f'''
        <div class="cta-grid">
            <button class="btn-p" onclick="addCart()">Buy Now</button>
            <div class="cart-sq" onclick="addCart()"><i class="ph ph-shopping-cart"></i></div>
        </div>
        '''
    else:
        cta = f'<button class="btn-o" style="width:100%" onclick="openModal()">Enquire Now</button>'
        
    return f'''
    <div class="pcard">
        <div class="pcard-accent"></div>
        <div class="pcard-img">
            <img src="./assets/images/{img_slug}2.png" alt="{name}">
            <div class="wishlist-btn"><i class="ph ph-heart"></i></div>
        </div>
        <div class="pcard-body">
            <div class="pcard-top-row">
                <div class="pcard-name">{name}</div>
                <div class="pcard-price">{price}</div>
            </div>
            <div class="tags">{tags_html}</div>
            <div class="specs">
                <div class="spec">{spec1}</div>
                <div class="spec">{spec2}</div>
                <div class="spec">{spec3}</div>
            </div>
            {cta}
        </div>
    </div>
    '''

# [06] Shop By Division
shop_div = soup.find('div', id='products')
shop_div.clear()
shop_div['class'] = 'sec alt'
shop_div.append(bs4.BeautifulSoup(f'''
<div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:48px; flex-wrap:wrap; gap:20px;">
    <div style="display:flex; flex-direction:column;">
        <div class="eyebrow">Revenue Divisions</div>
        <div class="sec-h2">Shop the Ecosystem</div>
        <div class="sec-rule" style="margin-bottom:24px;"></div>
        <div class="sec-body" style="margin-bottom:0; max-width:600px;">Browse components from across TMG's active product divisions.</div>
    </div>
    <div style="display:flex; gap:12px;">
        <button class="btn-o">Request a Quote</button>
        <button class="btn-p">View All Products</button>
    </div>
</div>

<div class="filter-row">
    <div class="filter-tabs" id="ftabs1">
        <div class="ftab active" data-f="all">All</div>
        <div class="ftab" data-f="aftermarket">Aftermarket Coolers</div>
        <div class="ftab" data-f="power">Power Transformers</div>
        <div class="ftab" data-f="battery">Battery Systems</div>
    </div>
    <div class="pnav-arrs">
        <div class="parr" onclick="scrollGrid('pgrid1', -1)"><i class="ph ph-arrow-left"></i></div>
        <div class="parr" onclick="scrollGrid('pgrid1', 1)"><i class="ph ph-arrow-right"></i></div>
    </div>
</div>

<div class="prod-grid-wrap fade-edges">
    <div class="prod-grid" id="pgrid1">
        <!-- Add multiple data-cat cards here -->
        <div class="pc-wrap" data-cat="aftermarket">
            {make_product_card("Aftermarket Radiator XR-240", "$1,249", "Aftermarket Coolers", ["Mining", "Oil & Gas"], "240mm Core", "Alloy Construction", "Fits: CAT 320–340 Series", "aftermarket_radiator_xr-240", "buy")}
        </div>
        <div class="pc-wrap" data-cat="aftermarket">
            {make_product_card("Charge Air Cooler CAC-18T", "$849", "Aftermarket Coolers", ["Heavy Transport", "Mining"], "18 inch Bar-and-Plate Core", "Pressure-tested to 120 PSI", "OEM-grade aluminium", "charge_air_cooler_cac-18t", "buy")}
        </div>
        <div class="pc-wrap" data-cat="power">
            {make_product_card("Step-Up Transformer T-500U", "Enquire", "Power Transformers", ["Data Centers", "Battery Storage"], "500 kVA", "ONAN Cooled", "IEEE C57.12 Compliant", "step-up_transformer_t-500u", "enquire")}
        </div>
        <div class="pc-wrap" data-cat="battery">
            {make_product_card("BESS Coolant Loop BCL-48", "Enquire", "Battery Systems", ["Battery Storage", "Data Centers"], "48V Nominal Loop", "Dual-redundant pump", "-40°C Operational", "bess_coolant_loop_bcl-48", "enquire")}
        </div>
        <div class="pc-wrap" data-cat="aftermarket">
            {make_product_card("Oil Cooler OC-6000", "$620", "Aftermarket Coolers", ["Oil & Gas", "Data Centers"], "6000 BTU/hr", "Hydraulic Oil Compatible", "Compact Form Factor", "oil_cooler_oc-6000", "buy")}
        </div>
    </div>
</div>
''', 'html.parser'))

# [07] Newsletter & [08] Ready To Ship (insert after shop_div)
newsletter_html = f'''
<div class="nl-sec">
    <div class="nl-bg-pattern"></div>
    <div class="nl-wrap">
        <div>
            <div class="nl-eb">Stay Informed</div>
            <div class="nl-h2">New Stock. New Industries. Direct to You.</div>
            <div class="nl-sub">Subscribe for product drops, restocks, and engineering insights from the TMG team.</div>
        </div>
        <div>
            <div class="nl-form">
                <input type="email" class="nl-inp" placeholder="Email address">
                <button class="btn-nl">Subscribe</button>
            </div>
            <div class="nl-note">No spam. Unsubscribe anytime.</div>
        </div>
    </div>
</div>

<div class="sec">
    <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:48px; flex-wrap:wrap; gap:20px;">
        <div style="display:flex; flex-direction:column;">
            <div class="eyebrow">Direct Distribution</div>
            <div class="sec-h2">Ready to Ship — No Lead Time</div>
            <div class="sec-rule" style="margin-bottom:24px;"></div>
            <div class="sec-body" style="margin-bottom:0; max-width:600px;">Spec-matched aftermarket components in stock. Same-week fulfillment on most SKUs.</div>
        </div>
        <div style="display:flex; gap:12px;">
            <button class="btn-o">Request a Quote</button>
            <button class="btn-p">Shop All Products</button>
        </div>
    </div>

    <div class="filter-row">
        <div class="filter-tabs" id="ftabs2">
            <div class="ftab active" data-f="all">All</div>
            <div class="ftab" data-f="aftermarket">Aftermarket Coolers</div>
        </div>
        <div class="pnav-arrs">
            <div class="parr" onclick="scrollGrid('pgrid2', -1)"><i class="ph ph-arrow-left"></i></div>
            <div class="parr" onclick="scrollGrid('pgrid2', 1)"><i class="ph ph-arrow-right"></i></div>
        </div>
    </div>

    <div class="prod-grid-wrap fade-edges">
        <div class="prod-grid" id="pgrid2">
            <div class="pc-wrap" data-cat="aftermarket">
                {make_product_card("Charge Air Cooler CAC-18T", "$849", "Aftermarket Coolers", ["Heavy Transport", "Mining"], "18 inch Bar-and-Plate Core", "Pressure-tested to 120 PSI", "OEM-grade aluminium", "charge_air_cooler_cac-18t", "buy")}
            </div>
            <div class="pc-wrap" data-cat="aftermarket">
                {make_product_card("Oil Cooler OC-6000", "$620", "Aftermarket Coolers", ["Oil & Gas", "Data Centers"], "6000 BTU/hr", "Hydraulic Oil Compatible", "Compact Form Factor", "oil_cooler_oc-6000", "buy")}
            </div>
            <div class="pc-wrap" data-cat="aftermarket">
                {make_product_card("Radiator Core RC-100M", "$480", "Aftermarket Coolers", ["Mining", "Agriculture"], "100mm width", "4-row copper core", "Universal bolt pattern", "radiator_core_rc-100m", "buy")}
            </div>
             <div class="pc-wrap" data-cat="aftermarket">
                {make_product_card("Aftermarket Radiator XR-240", "$1,249", "Aftermarket Coolers", ["Mining", "Oil & Gas"], "240mm Core", "Alloy Construction", "Fits: CAT 320–340 Series", "aftermarket_radiator_xr-240", "buy")}
            </div>
        </div>
    </div>
</div>
'''
shop_div.insert_after(bs4.BeautifulSoup(newsletter_html, 'html.parser'))

# [09] Industries
industries_div = soup.find('div', id='industries')
industries_div.clear()
industries_div.append(bs4.BeautifulSoup('''
<div class="hdr-row">
    <div class="hdr-left">
        <div class="eyebrow">Application Spectrum</div>
        <div class="sec-h2">Built for the Most Demanding Industries</div>
        <div class="sec-rule"></div>
        <div class="sec-body">From data centre cooling to oilfield heat exchangers — TMG components are application-engineered for real-world operating conditions.</div>
    </div>
    <button class="btn-o">View All Industries</button>
</div>
<div class="ind-grid">
    <a href="#" class="ind-card"><div class="pcard-accent"></div><i class="ph ph-cpu ind-icon"></i><div class="ind-title">Data Centers</div><div class="ind-desc">Precision cooling for high-density server and edge compute environments.</div><div class="ind-link">View Industry &rarr;</div></a>
    <a href="#" class="ind-card"><div class="pcard-accent"></div><i class="ph ph-lightning ind-icon"></i><div class="ind-title">Gen-Set & Power Generation</div><div class="ind-desc">Thermal management for standby generators and continuous power platforms.</div><div class="ind-link">View Industry &rarr;</div></a>
    <a href="#" class="ind-card"><div class="pcard-accent"></div><i class="ph ph-tractor ind-icon"></i><div class="ind-title">Mining & Agriculture</div><div class="ind-desc">Durable radiator cores engineered for high-dust, high-vibration field operation.</div><div class="ind-link">View Industry &rarr;</div></a>
    <a href="#" class="ind-card"><div class="pcard-accent"></div><i class="ph ph-drop ind-icon"></i><div class="ind-title">Oil & Gas</div><div class="ind-desc">Hydraulic and engine cooling for upstream and downstream oil field machinery.</div><div class="ind-link">View Industry &rarr;</div></a>
    <a href="#" class="ind-card"><div class="pcard-accent"></div><i class="ph ph-truck ind-icon"></i><div class="ind-title">Heavy Transport & Fleet</div><div class="ind-desc">Charge air and coolant solutions for long-haul diesel and CNG fleets.</div><div class="ind-link">View Industry &rarr;</div></a>
    <a href="#" class="ind-card"><div class="pcard-accent"></div><i class="ph ph-battery-charging ind-icon"></i><div class="ind-title">Battery Energy Storage</div><div class="ind-desc">BESS thermal architectures to prevent thermal runaway in large-scale energy storage.</div><div class="ind-link">View Industry &rarr;</div></a>
</div>
''', 'html.parser'))

# [10] Testimonials (insert after industries)
testimonials_html = '''
<div class="sec">
    <div class="eyebrow">Social Proof</div>
    <div class="sec-h2">Trusted by Operators Worldwide</div>
    <div class="sec-rule"></div>
    <div class="test-layout">
        <div class="test-list" id="tlist">
            <div class="test-item active">
                <img src="https://i.pravatar.cc/150?u=1" class="ti-img">
                <div class="ti-info">
                    <div class="ti-name">Edward Alexander</div>
                    <div class="ti-rat"><span>★</span> 4.9 on Oct 12</div>
                </div>
            </div>
            <div class="test-item next">
                <img src="https://i.pravatar.cc/150?u=2" class="ti-img">
                <div class="ti-info">
                    <div class="ti-name">Diana Johnston</div>
                    <div class="ti-rat"><span>★</span> 4.9 on Nov 05</div>
                </div>
            </div>
            <div class="test-item prev">
                <img src="https://i.pravatar.cc/150?u=3" class="ti-img">
                <div class="ti-info">
                    <div class="ti-name">Lauren Contreras</div>
                    <div class="ti-rat"><span>★</span> 5.0 on Sep 22</div>
                </div>
            </div>
        </div>
        <div class="test-quote-col">
            <span class="tq-mark">❝</span>
            <div class="tq-text" id="tq-text">TMG had our radiator spec'd, shipped, and installed before our competitor even sent back a quote. Zero downtime on site.</div>
            <div class="tq-name" id="tq-name">Edward Alexander</div>
            <div class="tq-co" id="tq-co">Fleet Operations Manager, Southern Transport Co.</div>
        </div>
    </div>
</div>
'''
industries_div.insert_after(bs4.BeautifulSoup(testimonials_html, 'html.parser'))

# [11] About
about_div = soup.find('div', id='about')
about_photo = about_div.find('div', class_='about-photo')
about_photo.clear() # removes the img
about_content = about_div.find('div', class_='about-content')
about_content.append(bs4.BeautifulSoup('''
<div style="display:flex; gap:12px; margin-top:32px;">
    <button class="btn-p">Our Story</button>
    <button class="btn-o">Contact Engineering</button>
</div>
''', 'html.parser'))

# Update Stats
stats = about_div.find_all('div', class_='stat-n')
if len(stats) >= 4:
    stats[0].string = "20+"
    stats[1].string = "5,000+"
    stats[2].string = "14"
    stats[3].string = "98%"
stat_labels = about_div.find_all('div', class_='stat-l')
if len(stat_labels) >= 4:
    stat_labels[1].string = "SKUs"
    stat_labels[2].string = "Countries"
    stat_labels[3].string = "On-Time"

# [12] Divisions
ecosystem_div = orig_soup.find('section', id='ecosystem')
if ecosystem_div:
    # We must fix CSS tokens for ecosystem since we used raw classes
    eco_style = bs4.BeautifulSoup("""<style>
      .div-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
      @media (min-width: 768px) { .div-grid { grid-template-columns: repeat(2, 1fr); } }
      @media (min-width: 1024px) { .div-grid { grid-template-columns: repeat(3, 1fr); } }
      .div-card { background: white; border: 1px solid var(--lines); display: flex; flex-direction: column; position: relative; text-decoration: none; transition: all 0.3s ease; height: 100%; }
      .div-accent { position: absolute; top: 0; left: 0; right: 0; height: 4px; opacity: 0; transition: opacity 0.3s; z-index: 5; }
      .div-img-area { aspect-ratio: 16/9; position: relative; overflow: hidden; display: flex; justify-content: center; align-items: center; }
      .div-pattern { position: absolute; inset: 0; opacity: 0.1; z-index: 1; }
      .div-icon { font-size: 80px; color: white; opacity: 0.15; transition: opacity 0.3s; z-index: 2; }
      .div-card:hover { transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06); }
      .div-card:hover .div-accent { opacity: 1; }
      .div-card:hover .div-icon { opacity: 0.3; }
      .bc-tmg .div-img-area { background: linear-gradient(135deg, #222f4b, #1e293b); }
      .bc-tmg .div-accent { background: #222f4b; }
      .div-body { padding: 32px 24px; display: flex; flex-direction: column; flex: 1; }
      .div-type { font-family: 'Sofia Sans', sans-serif; font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--muted); margin-bottom: 12px; }
      .div-title { font-family: 'Sofia Sans', sans-serif; font-size: 20px; text-transform: uppercase; color: var(--navy); margin-bottom: 12px; }
      .div-desc { font-size: 14px; line-height: 1.6; color: var(--muted); flex-grow: 1; margin-bottom: 16px; font-family: var(--BF); }
      .div-arrow { font-size: 24px; color: var(--muted); transition: all 0.2s; align-self: flex-start; }
      .div-card:hover .div-arrow { transform: translateX(6px); color: var(--navy); }
      .bc-cjp .div-img-area { background: linear-gradient(135deg, #1a5c7a, #113e52); }
      .bc-cjp .div-accent { background: #1a5c7a; }
      .bc-pwr .div-img-area { background: linear-gradient(135deg, #c02b2d, #7f1d1d); }
      .bc-pwr .div-accent { background: #c02b2d; }
      .bc-bat .div-img-area { background: linear-gradient(135deg, #1b6b42, #0f3f26); }
      .bc-bat .div-accent { background: #1b6b42; }
      .bc-seal .div-img-area { background: linear-gradient(135deg, #b0580f, #753909); }
      .bc-seal .div-accent { background: #b0580f; }
      .bc-inn .div-img-area { background: linear-gradient(135deg, #452080, #2b1352); }
      .bc-inn .div-accent { background: #452080; }
    </style>""", 'html.parser')
    style_tag.append(eco_style)
    
    # Update ecosystem header strategy
    header_container = ecosystem_div.find('div', class_='container')
    if header_container:
        # replace the text parts
        old_eyebrow = header_container.find('span', class_='eyebrow')
        if old_eyebrow: old_eyebrow.extract()
        old_h2 = header_container.find('h2')
        if old_h2: old_h2.extract()
        old_rule = header_container.find('div', class_='red-rule')
        if old_rule: old_rule.extract()
        old_p = header_container.find('p')
        if old_p: old_p.extract()
        
        new_header = bs4.BeautifulSoup('''
        <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:48px; flex-wrap:wrap; gap:20px;">
            <div style="display:flex; flex-direction:column;">
                <div class="eyebrow">Enterprise Hierarchy</div>
                <div class="sec-h2">The TMG Thermal Ecosystem</div>
                <div class="sec-rule" style="margin-bottom:24px;"></div>
                <div class="sec-body" style="margin-bottom:0; max-width:600px;">Navigate our specific divisions to find spec-matched components, complete cooling platforms, or custom engineering services.</div>
            </div>
            <div style="display:flex; gap:12px;">
                <button class="btn-o">Request a Consult</button>
            </div>
        </div>
        ''', 'html.parser')
        header_container.insert(0, new_header)

    ecosystem_div['class'] = 'sec alt'
    about_div.insert_after(ecosystem_div)

# [13] Contact
contact_btn = soup.find('div', id='contact').find('button', class_='form-btn')
contact_btn['class'] = 'btn-p'
contact_btn.string = 'Send Inquiry'
contact_btn.append(bs4.BeautifulSoup(' <i class="ph ph-arrow-right"></i>', 'html.parser'))

# [14] Footer
flogo_img = soup.find('div', class_='flogo').find('img')
flogo_img['src'] = './assets/tmg-logo-white.svg'

ficons = soup.find('div', class_='ficons')
ficons.append(bs4.BeautifulSoup('<a href="#" class="fi"><i class="ph ph-facebook-logo"></i></a>', 'html.parser'))

# Modal HTML
modal_html = '''
<div class="modal-ov" id="enqModal">
    <div class="modal-bx">
        <i class="ph ph-x modal-cl" onclick="closeModal()"></i>
        <div class="eyebrow">Contact Sales</div>
        <div class="sec-h2" style="font-size:24px;">Enquire Now</div>
        <div class="sec-rule" style="margin-bottom:24px;"></div>
        <input type="text" class="ff-full" placeholder="Name">
        <input type="email" class="ff-full" placeholder="Email">
        <input type="text" class="ff-full" placeholder="Company">
        <textarea class="ff-ta" placeholder="Message & Requirements"></textarea>
        <button class="btn-p" style="width:100%" onclick="closeModal()">Send Enquiry</button>
    </div>
</div>
'''
soup.body.append(bs4.BeautifulSoup(modal_html, 'html.parser'))


# Scripts
new_js = """
// 1. Announcement Bar
const annTexts = [
    "🔴 EXPO 2026 — Booth 4A · Apr 20–26 · Come find us",
    "🔴 New: Charge Air Coolers now in stock — Ships in 3–5 business days",
    "🔴 Free shipping on orders over $500 within the continental US"
];
let annIdx = 0;
const annEl = document.getElementById('ann-text');
setInterval(() => {
    annEl.style.opacity = '0';
    setTimeout(() => {
        annIdx = (annIdx + 1) % annTexts.length;
        annEl.innerHTML = annTexts[annIdx];
        annEl.style.opacity = '1';
    }, 400);
}, 4000);

// 3. Nav scroll hide
let lastScrollY = window.scrollY;
const navbar = document.querySelector('.nav');
window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        if (window.scrollY > lastScrollY) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
    }
    lastScrollY = window.scrollY;
});

// Shop / Filters
function setupFilters(tabsId, gridId) {
    const tabs = document.querySelectorAll(`#${tabsId} .ftab`);
    const grid = document.getElementById(gridId);
    tabs.forEach(t => {
        t.addEventListener('click', () => {
            tabs.forEach(x => x.classList.remove('active'));
            t.classList.add('active');
            const f = t.getAttribute('data-f');
            const cards = grid.querySelectorAll('.pc-wrap');
            cards.forEach(c => {
                if (f === 'all' || c.getAttribute('data-cat') === f) {
                    c.style.display = 'flex';
                    setTimeout(()=>c.style.opacity='1', 50);
                } else {
                    c.style.opacity = '0';
                    setTimeout(()=>c.style.display='none', 200);
                }
            });
        });
    });
}
setupFilters('ftabs1', 'pgrid1');
if(document.getElementById('ftabs2')) setupFilters('ftabs2', 'pgrid2');

function scrollGrid(id, dir) {
    const g = document.getElementById(id);
    const card = g.querySelector('.pc-wrap');
    if(card) {
        g.scrollBy({ left: (card.offsetWidth + 16) * dir, behavior: 'smooth' });
    }
}

// Cart Badge
let cartCount = sessionStorage.getItem('cartCount') ? parseInt(sessionStorage.getItem('cartCount')) : 0;
const cb = document.getElementById('cart-b');
cb.textContent = cartCount;
function addCart() {
    cartCount++;
    cb.textContent = cartCount;
    sessionStorage.setItem('cartCount', cartCount);
}

// Modal
function openModal() { document.getElementById('enqModal').classList.add('open'); }
function closeModal() { document.getElementById('enqModal').classList.remove('open'); }
document.getElementById('enqModal').addEventListener('click', (e) => {
    if(e.target.id === 'enqModal') closeModal();
});

// Testimonials
const tData = [
    {q: "TMG had our radiator spec'd, shipped, and installed before our competitor even sent back a quote. Zero downtime on site.", n: "Edward Alexander", c: "Fleet Operations Manager, Southern Transport Co."},
    {q: "The power transformer platform they configured for our BESS installation was exactly to spec. First time, every time. Seamless and easy process.", n: "Diana Johnston", c: "Senior Engineer, GridLink Energy"},
    {q: "When we had a custom cooling failure in the field, their engineering team had a prototype solution to us in 72 hours. Truly white-glove.", n: "Lauren Contreras", c: "Director of Maintenance, Pacific Mining Corp."}
];

let tIdx = 0;
const items = document.querySelectorAll('.test-item');
const qtext = document.getElementById('tq-text');
const qname = document.getElementById('tq-name');
const qco = document.getElementById('tq-co');

setInterval(() => {
    qtext.style.opacity = '0';
    
    items[tIdx].className = 'test-item prev';
    const nextIdx = (tIdx + 1) % 3;
    items[nextIdx].className = 'test-item active';
    const prevIdx = (tIdx + 2) % 3;
    items[prevIdx].className = 'test-item next';
    
    tIdx = nextIdx;
    
    setTimeout(() => {
        qtext.textContent = tData[tIdx].q;
        qname.textContent = tData[tIdx].n;
        qco.textContent = tData[tIdx].c;
        qtext.style.opacity = '1';
    }, 400);
}, 5000);
"""
# find last script tag and append
scripts = soup.find_all('script')
if scripts:
    scripts[-1].append(new_js)

with open(r'd:\Dev\Thermal-Motion-Group\phase-2-full\index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
