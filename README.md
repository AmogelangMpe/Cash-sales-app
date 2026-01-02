# PaySnap - Mobile App

A fully functional mobile-first cash sales tracking application with comprehensive inventory management, designed for South African mini supermarkets.

## Features

### 📊 Dashboard
- **Today's Revenue**: Large hero metric showing daily earnings
- **Total Sales & Average Sale**: Quick stats at a glance
- **Low Stock Alerts**: Automatic warnings when products are running low (≤10 items)
- **Out of Stock Alerts**: Notifications for products that need immediate restocking

### 🛒 New Sale
- **Product Grid**: 2-column layout with large tap targets for quick selection
- **Real-time Stock Display**: Shows remaining quantity for each product
- **Color-coded Warnings**: 
  - Red for low stock (≤10 items)
  - Disabled/grayed out for out-of-stock items
- **Smart Cart**: 
  - Prevents overselling (can't add more than available stock)
  - Shows itemized cart with quantity controls
  - Sticky footer with total
- **Quick Checkout**: 3-step process (tap products → complete → confirm)

### 📦 Products Management
- **Add/Edit Products**: Full CRUD operations with name, price, and stock quantity
- **Stock Tracking**: Visual indicators for stock levels
- **Quick Restock Buttons**: One-tap restocking (+10, +20, +50)
- **Stock Warnings**: Visual alerts for low stock items

### 📈 Insights Screen
- **Stock Alerts**: Lists all out-of-stock and low-stock products
- **Top Sellers**: Ranked list of 5 best-selling products with:
  - Total quantity sold
  - Total revenue generated
  - Current stock level
- **Least Sold**: Products that haven't sold yet (helps identify slow movers)
- **Restock Recommendations**: Smart suggestions based on:
  - Sales velocity (how fast items are selling)
  - Current stock levels
  - Popularity

### 💾 Data Persistence
- All data stored in browser localStorage
- Works completely offline
- No internet connection required

## How It Works

### Inventory Tracking
1. **When you add a sale**: Inventory automatically decreases for each product sold
2. **Stock Updates**: Products show current stock levels in real-time
3. **Prevents Overselling**: System blocks adding more items to cart than available
4. **Sales Analytics**: Tracks total sold and revenue per product

### Stock Management
- **Low Stock Threshold**: Products with 10 or fewer items are flagged
- **Out of Stock**: Products with 0 stock are disabled and can't be sold
- **Quick Restock**: Use +10, +20, +50 buttons for fast inventory updates
- **Manual Stock Entry**: Edit products to set exact stock quantities

### Sales Insights
- **Top Sellers**: Helps identify your best-performing products
- **Least Sold**: Shows products that aren't moving (consider reducing orders)
- **Restock Recommendations**: Suggests which popular items need restocking based on sales patterns

## Installation as Mobile App

This is a **Progressive Web App (PWA)** that can be installed on your phone like a native app!

### Quick Setup:
1. **Generate Icons**: Open `create-icons.html` in your browser to create app icons
2. **Serve the App**: Run a local server (see `INSTALL.md` for details)
3. **Install**: 
   - **Android**: Chrome menu → "Install app"
   - **iOS**: Safari Share → "Add to Home Screen"
   - **Desktop**: Click install icon in address bar

See `INSTALL.md` for detailed installation instructions.

## Usage

1. **Open the app** (in browser or as installed app)
2. **Add Products**: Go to Products screen → Add New Product
3. **Make Sales**: Go to New Sale → Tap products → Complete Sale
4. **Monitor Inventory**: Check Dashboard for alerts, or go to Insights for detailed analysis
5. **Restock**: Use quick restock buttons or edit products directly

## Design Features

- **Mobile-First**: Optimized for touch interactions with 56px+ tap targets
- **Speed-Optimized**: 10-15 second sale flow with minimal taps
- **Offline-First**: Works without internet connection
- **South African Rand**: All prices formatted as R (Rand)
- **Green Theme**: Primary color associated with money/growth
- **Large Typography**: Easy to read and scan
- **Bottom Navigation**: Thumb-friendly navigation (Home, New Sale, Products)

## Sample Data

The app comes pre-loaded with sample products:
- Bread (R12.50, 20 in stock)
- Milk (R15.00, 15 in stock)
- Eggs (R25.00, 30 in stock)
- Sugar (R18.00, 10 in stock)
- Cooking Oil (R35.00, 8 in stock)
- Rice (R45.00, 12 in stock)

You can delete these and add your own products.

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers (iOS Safari, Chrome Mobile)

## Data Storage

All data is stored locally in your browser using localStorage. To backup your data:
1. Open browser Developer Tools (F12)
2. Go to Application/Storage tab
3. Find Local Storage
4. Copy the data

To restore, paste the data back into localStorage.

---

**Note**: This is a prototype/demo application. For production use, consider adding:
- Data export/import functionality
- Cloud backup
- Multi-user support
- Receipt printing
- Barcode scanning

