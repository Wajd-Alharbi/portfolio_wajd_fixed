# Wajd Alharbi - AI/ML Engineer Portfolio

A modern, bilingual (English/Arabic) portfolio website built with Streamlit, featuring a responsive design and smooth animations.

## Features

✨ **Bilingual Support** - Seamlessly switch between English and Arabic (RTL support)
🎨 **Modern Design** - Beautiful gradient backgrounds and smooth transitions
📱 **Responsive** - Works perfectly on desktop and mobile devices
🌙 **Dark Theme** - Eye-friendly dark mode with professional color scheme
⚡ **Fast Loading** - Optimized performance with minimal dependencies
🔗 **Social Integration** - LinkedIn, GitHub, and Twitter links
📸 **Profile Photo** - Professional profile image support

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd portfolio_wajd_updated
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, copy the URL from the terminal

## Project Structure

```
portfolio_wajd_updated/
├── app.py                 # Main Streamlit application
├── components.py          # Reusable UI components
├── content.py            # Bilingual content and data
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── assets/
    ├── style.css        # Custom CSS styling
    └── profile.png      # Your profile photo
```

## Customization

### Update Your Information

Edit `content.py` to update:
- Your name and role
- Education details
- Work experience
- Projects
- Skills
- Contact information

### Update Social Links

In `components.py`, modify the URLs in the `social_links()` function:
```python
<a href="https://www.linkedin.com/in/your-profile" ...>LinkedIn</a>
<a href="https://github.com/your-username" ...>GitHub</a>
```

### Change Colors and Styling

Edit `assets/style.css` to customize:
- Color scheme
- Font sizes
- Spacing
- Animations

## Browser Support

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment Options

### Streamlit Cloud (Recommended - Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select this app and deploy

### Other Options
- Heroku
- AWS
- Google Cloud
- Azure
- DigitalOcean

## Troubleshooting

**Issue: Content appears as code**
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Restart Streamlit: Press `C` in terminal, then run `streamlit run app.py` again

**Issue: Images not loading**
- Ensure `assets/profile.png` exists
- Check file permissions
- Try clearing cache

**Issue: Language toggle not working**
- Refresh the page
- Clear browser cache
- Check browser console for errors (F12)

## Performance Tips

- Keep images optimized and compressed
- Use CDN for external assets
- Minimize CSS file size
- Cache static content

## License

This portfolio is personal and proprietary. Feel free to use as a template for your own portfolio.

## Support

For issues or questions, please check the [Streamlit documentation](https://docs.streamlit.io)

---

**Built with ❤️ using Streamlit**
