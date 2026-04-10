class FloatingGallery {
  constructor(containerId, photos) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.photos = photos;
    this.shuffle(this.photos);
    this.nodes = [];
    this.particles = [];
    this.width = this.container.offsetWidth;
    this.height = this.container.offsetHeight;
    this.mouseX = -1000;
    this.mouseY = -1000;

    this.init();
    this.animate();
    this.startCycling();
    window.addEventListener('resize', () => this.onResize());
    this.container.addEventListener('mousemove', (e) => this.onMouseMove(e));
  }

  shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }

  init() {
    // Create floating cards
    const numCards = Math.min(this.photos.length, window.innerWidth < 768 ? 6 : 14);
    for (let i = 0; i < numCards; i++) {
        const photo = this.photos[Math.floor(Math.random() * this.photos.length)];
        this.addCard(photo);
    }

    // Create background particles
    const numParticles = 10;
    for (let i = 0; i < numParticles; i++) {
        this.addParticle();
    }
  }

  addCard(photo) {
    const card = document.createElement('a');
    card.className = 'floating-card';
    card.href = '/photography/';
    
    const img = document.createElement('img');
    // Use smaller viewBox for homepage performance
    img.src = photo.src.replace(/viewBox=\d+/, 'viewBox=512');
    img.alt = photo.alt;
    
    card.appendChild(img);
    this.container.appendChild(card);

    // Initial random state
    const w = 150 + Math.random() * 100;
    const node = {
        el: card,
        img: img,
        isHovered: false,
        isFading: false,
        x: Math.random() * (this.width - w),
        y: Math.random() * (this.height - w * 1.3),
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        rotation: (Math.random() - 0.5) * 20,
        vr: (Math.random() - 0.5) * 0.1,
        w: w
    };
    
    card.addEventListener('mouseenter', () => { node.isHovered = true; });
    card.addEventListener('mouseleave', () => { node.isHovered = false; });
    
    card.style.width = `${w}px`;
    this.nodes.push(node);
  }

  addParticle() {
    const el = document.createElement('div');
    el.className = 'floating-particle';
    const size = 100 + Math.random() * 300;
    el.style.width = `${size}px`;
    el.style.height = `${size}px`;
    
    this.container.appendChild(el);
    
    this.particles.push({
        el: el,
        x: Math.random() * this.width,
        y: Math.random() * this.height,
        vx: (Math.random() - 0.5) * 0.2,
        vy: (Math.random() - 0.5) * 0.2,
        size: size
    });
  }

  onMouseMove(e) {
    const rect = this.container.getBoundingClientRect();
    this.mouseX = e.clientX - rect.left;
    this.mouseY = e.clientY - rect.top;
  }

  onResize() {
    this.width = this.container.offsetWidth;
    this.height = this.container.offsetHeight;
  }

  animate() {
    // Update cards
    this.nodes.forEach(node => {
        // Drifting velocity
        node.x += node.vx;
        node.y += node.vy;
        node.rotation += node.vr;

        // Interaction (slight repulsion from mouse)
        // Only apply physics if NOT hovered
        if (!node.isHovered && !node.isFading) {
            const dx = node.x + node.w/2 - this.mouseX;
            const dy = node.y + node.w/2 - this.mouseY;
            const dist = Math.sqrt(dx*dx + dy*dy);
            if (dist < 300) {
                const force = (300 - dist) / 3000;
                node.vx += dx * force;
                node.vy += dy * force;
            }

            node.x += node.vx;
            node.y += node.vy;
            node.rotation += node.vr;
        }

        // Boundary bounce with damping
        const damping = 0.95;
        if (node.x < 0) { node.x = 0; node.vx *= - damping; }
        if (node.x + node.w > this.width) { node.x = this.width - node.w; node.vx *= - damping; }
        if (node.y < 0) { node.y = 0; node.vy *= - damping; }
        if (node.y + node.w * 1.3 > this.height) { node.y = this.height - node.w * 1.3; node.vy *= - damping; }

        // Speed limit
        const limit = 2;
        node.vx = Math.max(-limit, Math.min(limit, node.vx));
        node.vy = Math.max(-limit, Math.min(limit, node.vy));
        
        // Friction
        node.vx *= 0.995;
        node.vy *= 0.995;

        node.el.style.transform = `translate3d(${node.x}px, ${node.y}px, 0) rotate(${node.rotation}deg)`;
    });

    // Update particles
    this.particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        
        if (p.x < -p.size) p.x = this.width;
        if (p.x > this.width) p.x = -p.size;
        if (p.y < -p.size) p.y = this.height;
        if (p.y > this.height) p.y = -p.size;

        p.el.style.transform = `translate3d(${p.x}px, ${p.y}px, 0)`;
    });

    requestAnimationFrame(() => this.animate());
  }

  startCycling() {
    setInterval(() => {
        this.cycleImage();
    }, 10000); // Cycle every 10 seconds
  }

  cycleImage() {
    // Pick a card that isn't hovered or already fading
    const eligible = this.nodes.filter(n => !n.isHovered && !n.isFading);
    if (!eligible.length) return;
    
    const node = eligible[Math.floor(Math.random() * eligible.length)];
    const newPhoto = this.photos[Math.floor(Math.random() * this.photos.length)];
    
    node.isFading = true;
    node.el.style.opacity = '0';
    
    setTimeout(() => {
        // Swap content
        node.img.src = newPhoto.src.replace(/viewBox=\d+/, 'viewBox=512');
        node.img.alt = newPhoto.alt;
        
        // Randomize new position
        node.x = Math.random() * (this.width - node.w);
        node.y = Math.random() * (this.height - node.w * 1.3);
        node.vx = (Math.random() - 0.5) * 0.4;
        node.vy = (Math.random() - 0.5) * 0.4;
        
        // Wait for image load before fade in
        node.img.onload = () => {
            node.el.style.opacity = '1';
            setTimeout(() => { node.isFading = false; }, 800);
        };
    }, 850); // Match CSS transition duration
  }
}
