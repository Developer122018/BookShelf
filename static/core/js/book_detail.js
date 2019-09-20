class ImageViewer {
    constructor(selector) {
      this.selector = selector;
      $(this.secondaryImages).click(() => this.setMainImage(event));
      $(this.mainImage).click(() => this.showLightbox(event));
      $(this.lightboxClose).click(() => this.hideLightbox(event));
    }
    
    get secondaryImageSelector() {
      return '.secondary-image';
    }
    
    get mainImageSelector() {
      return '.main-image';
    }
    
    get lightboxImageSelector() {
      return '.lightbox';
    }
    
    get lightboxClose() {
      return '.lightbox-controls-close';
    }
    
    get secondaryImages() {
      var secondaryImages = $(this.selector).find(this.secondaryImageSelector).find('img')
      return secondaryImages;
    }
    
    get mainImage() {
      var mainImage = $(this.selector).find(this.mainImageSelector);
      return mainImage;
    }
    
    get lightboxImage() {
      var lightboxImage = $(this.lightboxImageSelector);
      return lightboxImage;
    }
    
    setLightboxImage(event){
      var src = this.getEventSrc(event);
      this.setSrc(this.lightboxImage, src);
    }
    
    setMainImage(event){
      var src = this.getEventSrc(event);
      this.setSrc(this.mainImage, src);
    }
    
    getSrc(node){
      var image = $(node).find('img');
    }
    
    setSrc(node, src){
      var image = $(node).find('img')[0];
      image.src = src;
    }
    
    getEventSrc(event){
      return event.target.src;
    }
    
    showLightbox(event){
      this.setLightboxImage(event);
      $(this.lightboxImageSelector).addClass('show');
    }
    
    hideLightbox(){
      $(this.lightboxImageSelector).removeClass('show');
    }
  }
  
  new ImageViewer('.image-viewer');