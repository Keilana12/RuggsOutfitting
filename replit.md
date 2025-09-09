# Rugg's Outfitting L.L.C. Website

## Overview
This is a Flask web application for Rugg's Outfitting L.L.C., a Montana-based family business offering outfitting services, hunting trips, and ranch experiences. The project was originally built using Google App Engine with Python 2.7 and webapp2, and has been successfully migrated to modern Flask and Python 3.11 for the Replit environment.

## Recent Changes
- **September 9, 2025**: Migrated from webapp2 to Flask framework
- **September 9, 2025**: Updated from Python 2.7 to Python 3.11
- **September 9, 2025**: Configured for Replit deployment and hosting
- **September 9, 2025**: Added proper static file serving for assets and images
- **September 9, 2025**: Set up development workflow and deployment configuration

## Project Architecture
### Technology Stack
- **Backend**: Flask (Python 3.11)
- **Template Engine**: Native Jinja2 (via Flask's render_template_string)
- **Static Assets**: CSS, JavaScript, images served through Flask routes
- **Deployment**: Configured for Replit autoscale deployment

### Directory Structure
- `main.py` - Main Flask application with all routes
- `pages/` - HTML templates for different pages (header, footer, content)
- `assets/` - CSS, JavaScript, and font files
- `images/` - Website images and photos
- `.gitignore` - Python and development environment exclusions

### Routes
- `/` - Home page
- `/hunting` - Big game hunting information
- `/outfitting` - Outfitting services
- `/ranch` - River Ranch services
- `/contact` - Contact information and family history

### Static File Handling
The application serves static files through dedicated Flask routes:
- `/assets/<path>` - CSS, JS, and font files
- `/images/<path>` - Image files
- `/favicon.ico` - Site favicon

## Current State
The application is fully functional and ready for use. All routes work correctly, static assets load properly, and the site maintains its original design and functionality. The Flask server is configured to run on port 5000 with cache control headers to prevent browser caching issues during development.

## User Preferences
- Maintain the original website design and functionality
- Keep the family business branding and content intact
- Ensure all images and assets load correctly