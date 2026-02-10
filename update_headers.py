#!/usr/bin/env python3
"""
Script to update all HTML file headers in APP2026 folder to match index.html structure
"""
import re
from pathlib import Path

# Files to skip
SKIP_FILES = {
    'index.html',
    'index - Copy.html',
    'contacts.html',  # Already updated
    'post1.html',     # Already updated
    'post2.html',     # Already updated
   'ranking.html',   # Custom header
    'calendario.html', # Custom header
    'ene26.html',     # Deleted
    'feb26.html',     # Deleted  
    'mar26.html',     # Deleted
    'post-quote - Copy.html',  # Copy file
    'update_headers.py'  # This script
}

# The correct header and mobile header from index.html
CORRECT_HEADER = '''<!-- Header -->
        <header class="top_panel_wrap top_panel_style_3 scheme_original">
          <div
            class="top_panel_wrap_inner top_panel_inner_style_3 top_panel_position_above"
          >
            <!-- User panel -->
            <div class="top_panel_top">
              <div class="content_wrap clearfix">
                <div class="top_panel_top_contact_area icon-smartphone">
                  +507 6674-1441
                </div>
                <div class="top_panel_top_open_hours icon-mail-2">
                  info@padelpanama.org
                </div>
                <div class="top_panel_top_user_area">
                  <ul id="menu_user" class="menu_user_nav">
                    <li class="top_panel_top_search">
                      <div
                        class="search_wrap search_style_regular search_state_fixed"
                      >
                        <div class="search_form_wrap">
                          <form
                            role="search"
                            method="get"
                            class="search_form"
                            action="#"
                          >
                            <button
                              type="submit"
                              class="search_submit icon-magnifier"
                              title="Start search"
                            ></button>
                            <input
                              type="text"
                              class="search_field"
                              placeholder="Search"
                              value=""
                              name="s"
                            />
                          </form>
                        </div>
                        <div class="search_results widget_area scheme_original">
                          <a class="search_results_close icon-cancel"></a>
                          <div class="search_results_content"></div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <!-- /User panel -->
            <!-- Top Menu -->
            <div class="top_panel_middle">
              <div class="content_wrap">
                <div class="contact_logo">
                  <div class="logo">
                    <a href="index.html">
                      <img
                        src="images/logo-1.png"
                        alt="APP Logo"
                        style="max-height: 60px; width: auto"
                      />
                    </a>
                  </div>
                </div>
                <div class="menu_main_social_wrap">
                  <div class="top_panel_top_socials">
                    <div
                      class="sc_socials sc_socials_type_icons sc_socials_shape_square sc_socials_size_small"
                    >
                      <div class="sc_socials_item">
                        <a
                          href="#"
                          target="_blank"
                          class="social_icons social_twitter"
                        >
                          <span class="icon-twitter"></span>
                        </a>
                      </div>
                      <div class="sc_socials_item">
                        <a
                          href="#"
                          target="_blank"
                          class="social_icons social_facebook"
                        >
                          <span class="icon-facebook"></span>
                        </a>
                      </div>
                      <div class="sc_socials_item">
                        <a
                          href="#"
                          target="_blank"
                          class="social_icons social_gplus"
                        >
                          <span class="icon-gplus"></span>
                        </a>
                      </div>
                    </div>
                  </div>
                  <div class="menu_main_wrap">
                    <a
                      href="#"
                      class="menu_main_responsive_button icon-menu"
                    ></a>
                    <nav class="menu_main_nav_area">
                      <ul id="menu_main" class="menu_main_nav">
                        <li class="menu-item current-menu-item">
                          <a href="index.html">Home</a>
                        </li>
                        <li class="menu-item">
                          <a href="calendario.html">Torneos</a>
                        </li>
                        <li class="menu-item">
                          <a href="ranking.html">Ranking</a>
                        </li>
                        <li class="menu-item">
                          <a href="nosotros.html">Nosotros</a>
                        </li>
                        <li class="menu-item">
                          <a href="contacts.html">Contacto</a>
                        </li>
                      </ul>
                    </nav>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Top Menu -->
          </div>
        </header>
        <!-- /Header -->
        <!-- Header Mobile -->
        <div class="header_mobile">
          <div class="content_wrap">
            <div class="menu_button icon-menu"></div>
            <div class="logo">
              <a href="index.html">
                <img
                  src="images/logo-1.png"
                  alt="APP Logo"
                  style="max-height: 50px; width: auto"
                />
              </a>
            </div>
          </div>
          <div class="side_wrap">
            <div class="close">Close</div>
            <div class="panel_top">
              <nav class="menu_main_nav_area">
                <ul id="menu_main_mobile" class="menu_main_nav">
                  <li class="menu-item current-menu-item">
                    <a href="index.html">Home</a>
                  </li>
                  <li class="menu-item">
                    <a href="calendario.html">Torneos</a>
                  </li>
                  <li class="menu-item">
                    <a href="ranking.html">Ranking</a>
                  </li>
                  <li class="menu-item">
                    <a href="nosotros.html">Nosotros</a>
                  </li>
                  <li class="menu-item">
                    <a href="contacts.html">Contacto</a>
                  </li>
                </ul>
              </nav>
              <div class="search_wrap search_style_regular search_state_fixed">
                <div class="search_form_wrap">
                  <form method="get" class="search_form" action="#">
                    <button
                      type="submit"
                      class="search_submit icon-magnifier"
                      title="Start search"
                    ></button>
                    <input
                      type="text"
                      class="search_field"
                      placeholder="Search"
                      value=""
                      name="s"
                    />
                  </form>
                </div>
                <div class="search_results widget_area scheme_original">
                  <a class="search_results_close icon-cancel"></a>
                  <div class="search_results_content"></div>
                </div>
              </div>
            </div>
            <div class="panel_bottom">
              <div class="contact_socials">
                <div
                  class="sc_socials sc_socials_type_icons sc_socials_shape_square sc_socials_size_small"
                >
                  <div class="sc_socials_item">
                    <a
                      href="#"
                      target="_blank"
                      class="social_icons social_twitter"
                    >
                      <span class="icon-twitter"></span>
                    </a>
                  </div>
                  <div class="sc_socials_item">
                    <a
                      href="#"
                      target="_blank"
                      class="social_icons social_facebook"
                    >
                      <span class="icon-facebook"></span>
                    </a>
                  </div>
                  <div class="sc_socials_item">
                    <a
                      href="#"
                      target="_blank"
                      class="social_icons social_gplus"
                    >
                      <span class="icon-gplus"></span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="mask"></div>
        </div>
        <!-- /Header Mobile -->'''

def update_file(file_path):
    """Update a single HTML file's header"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the header section from <!--Header --> to <!-- /Header Mobile -->
    pattern = r'<!--\s*Header\s*-->.*?<!--\s*/Header Mobile\s*-->'
    
    if not re.search(pattern, content, re.DOTALL):
        return False
    
    # Replace the old header with the correct one
    new_content = re.sub(pattern, CORRECT_HEADER, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    app_dir = Path(__file__).parent
    html_files = sorted([file for file in app_dir.glob('*.html') 
                        if file.name not in SKIP_FILES])
    
    updated_files = []
    failed_files = []
    
    print(f"Found {len(html_files)} files to update\n")
    
    for file_path in html_files:
        try:
            if update_file(file_path):
                updated_files.append(file_path.name)
                print(f"✓ Updated: {file_path.name}")
            else:
                print(f"⊘ Skipped (no header found): {file_path.name}")
        except Exception as e:
            failed_files.append((file_path.name, str(e)))
            print(f"✗ Error in {file_path.name}: {e}")
    
    print(f"\n\nSummary:")
    print(f"Updated: {len(updated_files)} files")
    print(f"Failed: {len(failed_files)} files")
    
    if updated_files:
        print(f"\nUpdated files:")
        for file in sorted(updated_files):
            print(f"  - {file}")
    
    if failed_files:
        print(f"\nFailed files:")
        for file, error in failed_files:
            print(f"  - {file}: {error}")

if __name__ == '__main__':
    main()
