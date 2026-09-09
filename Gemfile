source "https://rubygems.org"
gem "csv"
gem "bigdecimal"
gem "webrick"

# GitHub Pages (includes most plugins)
gem "github-pages", group: :jekyll_plugins

# This is the default theme
gem "minima", "~> 2.5"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  # These are already included in github-pages, but we specify them here for clarity
  # jekyll-seo-tag and jekyll-sitemap are already part of github-pages
end

# Windows and JRuby specific gems
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]