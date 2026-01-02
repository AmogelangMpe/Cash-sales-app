#!/usr/bin/env python3
"""
Simple icon generator for PaySnap
Requires: pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
except ImportError:
    print("Installing Pillow...")
    import subprocess
    subprocess.check_call(["pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont
    import os

def create_icon(size):
    """Create a PaySnap icon with green gradient and PS text"""
    # Create image with green gradient
    img = Image.new('RGB', (size, size), color='#10b981')
    
    # Create gradient effect
    from PIL import ImageFilter
    draw = ImageDraw.Draw(img)
    
    # Draw gradient (simplified - solid green with lighter top)
    for y in range(size):
        # Calculate gradient color
        ratio = y / size
        r = int(132 + (5 - 132) * ratio)  # #84cc16 to #059669
        g = int(204 + (150 - 204) * ratio)
        b = int(22 + (105 - 22) * ratio)
        draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))
    
    # Draw white "PS" text
    try:
        # Try to use a nice font
        font_size = int(size * 0.4)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    draw.text(
        (size/2, size/2),
        "PS",
        fill='white',
        font=font,
        anchor='mm'  # middle-center anchor
    )
    
    # Add border
    border_width = max(2, int(size * 0.02))
    draw.rectangle(
        [(border_width, border_width), (size-border_width, size-border_width)],
        outline='rgba(255, 255, 255, 76)',  # Semi-transparent white
        width=border_width
    )
    
    return img

def main():
    print("Generating PaySnap icons...")
    
    # Generate 192x192 icon
    print("Creating icon-192.png...")
    icon192 = create_icon(192)
    icon192.save('icon-192.png', 'PNG')
    print("✓ Created icon-192.png")
    
    # Generate 512x512 icon
    print("Creating icon-512.png...")
    icon512 = create_icon(512)
    icon512.save('icon-512.png', 'PNG')
    print("✓ Created icon-512.png")
    
    print("\n✅ All icons generated successfully!")
    print("Files saved in current directory:")
    print("  - icon-192.png")
    print("  - icon-512.png")

if __name__ == '__main__':
    main()

