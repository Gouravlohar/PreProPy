# PreProPy Documentation Website

This folder contains a modern, responsive documentation website for the PreProPy package.

## Features

- **Modern Design**: Clean and professional interface with attention to typography and spacing
- **Responsive Layout**: Works perfectly on all devices from mobile to desktop
- **Dark/Light Mode**: Supports both dark and light themes with automatic system preference detection
- **Interactive Components**: Code copying, smooth scrolling, and dynamic content display
- **Comprehensive Documentation**: Detailed API references, examples, and guides

## Structure

```
webapp/
├── css/
│   └── style.css           # Custom styles beyond Tailwind
├── images/
│   ├── prepropy-logo.svg   # Package logo
│   └── architecture-diagram.svg # Architecture diagram
├── js/
│   └── script.js           # JavaScript for interactivity
└── index.html              # Main documentation page
```

## Usage

To view the documentation website:

1. Simply open the `index.html` file in a web browser

No build process is required as the site uses Tailwind CSS via CDN.

## Customization

- **Colors**: Edit the Tailwind configuration in `index.html` to change the color scheme
- **Content**: Update the HTML in `index.html` to modify content
- **Styling**: Add or modify CSS rules in `css/style.css`
- **Interactivity**: Enhance JavaScript functionality in `js/script.js`

## Browser Support

The documentation website supports all modern browsers:

- Chrome (and Chromium-based browsers like Edge)
- Firefox
- Safari
- Opera

## Credits

- [Tailwind CSS](https://tailwindcss.com/) for utility-first CSS framework
- [Font Awesome](https://fontawesome.com/) for icons
- [Inter](https://fonts.google.com/specimen/Inter) and [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) fonts from Google Fonts
