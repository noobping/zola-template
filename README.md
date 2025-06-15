[![GitHub Pages](https://github.com/noobping/zola-template/actions/workflows/pages.yml/badge.svg)](https://github.com/noobping/zola-template/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-default.svg)](https://opensource.org/licenses/MIT)

# Zola template

A ready-to-use template featuring my [custom theme](https://github.com/noobping/zola-theme) for [Zola](https://www.getzola.org/) — a fast, modern static site generator.

## Getting started for the first time

To get started with this template, follow these steps:

1. Use the "Use this template" button on GitHub to create a new repository based on this template.
2. Name your repository (e.g., `my-zola-site`).
3. Add a description for your repository.
4. Edit the [config](config.toml) file to customize your site. 
    - You can change the `title` to the name of your site, 
    - and the `description` to a brief summary of what your site is about. 
    - Update the `author` section with your name.
    - Update the `base_url` in the [config](config.toml) file to match your repository name (e.g., `https://<username>.github.io/my-zola-site/`). You can also set it to a custom domain if you have one.

## Deploying your site

To deploy your Zola site, you can use GitHub Pages. Follow these steps:
1. Go to the "Settings" tab of your repository.
2. Scroll down to the "Pages" section.
3. Use GitHub Actions to deploy your site.

## Customizing your site

You can customize your site by editing the following files:

- `config.toml`: This is the main configuration file for your Zola site. You can change the title, description, author, and other settings here.
- `content/`: This directory contains your site's content. You can add new pages, posts, and other content here. Please add images to the same directory as the Markdown file that references them.

For more information on how to use Zola, refer to the [Zola documentation](https://www.getzola.org/documentation/) or go to [my theme repository](https://github.com/noobping/zola-theme) for more details on how to use my theme.
