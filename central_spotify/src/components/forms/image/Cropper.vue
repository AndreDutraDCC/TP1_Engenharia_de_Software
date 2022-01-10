<template>
  <div>
    <input
      style="display: none;"
      ref="input"
      type="file"
      name="image"
      accept="image/*"
      @change="setImage"
    />

    <div>
        <v-row justify="center" class="mt-3">
          <v-col cols="8" sm="8" md="7" lg="7" xl="7" v-show="imgSrc">
            <div class="img-cropper">
              <vue-cropper
                ref="cropper"
                :aspect-ratio="ratio"
                :autoCropArea="1"
                :src="imgSrc"
                :imgStyle="{'max-width': '100%', 'max-height': '600px', 'min-height':'300px', 'min-width':'300px'}"
                preview=".preview"
              />
            </div>
            <div style="position: relative;">
              <div style="position: absolute; left: 5px; bottom: 5px;">
                <v-progress-circular color="primary" :value="rotationDegree"></v-progress-circular>
              </div>
            </div>
          </v-col>
          <v-col cols="8" sm="8" md="7" lg="7" xl="7" v-show="!imgSrc">
            <div class="img-cropper-skeleton">
            </div>
          </v-col>
          <v-col v-if="imgSrc" cols="12" sm="12" md="7" lg="7" xl="7">
            <v-slider
              color="primary"
              v-model="rotationDegreeComp"
              max="100"
              min="0"
            ></v-slider>
            <div class="row justify-center">
              <v-btn text color="primary" fab role="button" @click.prevent="zoom(-0.2)">
                <v-icon>mdi-magnify-minus-outline</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="zoom(0.2)">
                <v-icon>mdi-magnify-plus-outline</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="move(0, 10)">
                <v-icon>mdi-arrow-up</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="move(0, -10)">
                <v-icon>mdi-arrow-down</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="move(10, 0)">
                <v-icon>mdi-arrow-left</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="move(-10, 0)">
                <v-icon>mdi-arrow-right</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="rotate(-90)">
                <v-icon>mdi-rotate-left</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="rotate(90)">
                <v-icon>mdi-rotate-right</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="flipX">
                <v-icon>mdi-flip-horizontal</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="flipY">
                <v-icon>mdi-flip-vertical</v-icon>
              </v-btn>
              <v-btn text color="primary" fab role="button" @click.prevent="reset">
                <v-icon>mdi-cached</v-icon>
              </v-btn>
            </div>
          </v-col>
        </v-row>
        <v-row justify="space-around">
          <v-col>
            <v-btn block text color="primary" @click.prevent="showFileChooser">
              <v-icon class="mx-5">mdi-cloud-upload-outline</v-icon> Escolher Imagem
            </v-btn>
          </v-col>
        </v-row>
            <!-- <div class="actions">
              
              <a
                href="#"
                role="button"
                @click.prevent="cropImage"
              >
                Crop
              </a>
              <a
                href="#"
                role="button"
                @click.prevent="reset"
              >
                Reset
              </a>
              <a
                href="#"
                role="button"
                @click.prevent="getData"
              >
                Get Data
              </a>
              <a
                href="#"
                role="button"
                @click.prevent="setData"
              >
                Set Data
              </a>
              <a
                href="#"
                role="button"
                @click.prevent="getCropBoxData"
              >
                Get CropBox Data
              </a>
              <a
                href="#"
                role="button"
                @click.prevent="setCropBoxData"
              >
                Set CropBox Data
              </a>
              <a
                href="#"
                role="button"
                @click.prevent="showFileChooser"
              >
                Upload Image
              </a>
            </div> -->
            <!-- <p>Preview</p>
            <div class="preview" /> -->
            <!-- <p>Cropped Image</p>
            <div class="cropped-image">
              <img
                v-if="cropImg"
                :src="cropImg"
                alt="Cropped Image"
              />
              <div v-else class="crop-placeholder" />
            </div> -->
    </div>
  </div>
</template>

<script>
import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';

export default {
  name:'Cropper',
  components: {
    VueCropper,
  },
  props: {
    ratio: Number
  },
  data() {
    return {
      imgSrc: '',
      cropImg: '',
      rotationDegree: 0,
      data: null,
      config: {},
    };
  },
  methods: {
    cropImage() {
      // get image data for post processing, e.g. upload or setting image src
      this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL();
      this.$emit('cropped',this.cropImg)
    },
    flipX() {
      // const dom = this.$refs.flipX;
      // let scale = dom.getAttribute('data-scale');
      let scale = this.config.scaleX
      scale = scale ? -scale : -1;
      this.$refs.cropper.scaleX(scale);
      this.config.scaleX = scale
      // dom.setAttribute('data-scale', scale);
    },
    flipY() {
      // const dom = this.$refs.flipY;
      // let scale = dom.getAttribute('data-scale');
      let scale = this.config.scaleY
      scale = scale ? -scale : -1;
      this.$refs.cropper.scaleY(scale);
      this.config.scaleY = scale
      // dom.setAttribute('data-scale', scale);
    },
    getCropBoxData() {
      this.data = JSON.stringify(this.$refs.cropper.getCropBoxData(), null, 4);
    },
    getData() {
      this.data = JSON.stringify(this.$refs.cropper.getData(), null, 4);
    },
    move(offsetX, offsetY) {
      this.$refs.cropper.move(offsetX, offsetY);
    },
    reset() {
      this.rotateTo(0)
      this.$refs.cropper.reset();
    },
    rotate(deg) {
      this.rotationDegree += Math.round( ( deg / 360 ) * 100)
      if(this.rotationDegree < 0) this.rotationDegree += 100
      if(this.rotationDegree >= 100) this.rotationDegree = this.rotationDegree - 100
      this.$refs.cropper.rotate(deg);
    },
    rotateTo(deg) {
      this.rotationDegree = Math.round( ( deg / 360 ) * 100)
      if(this.rotationDegree < 0) this.rotationDegree += 100
      if(this.rotationDegree >= 100) this.rotationDegree = this.rotationDegree - 100
      this.$refs.cropper.rotateTo(deg);
    },
    setCropBoxData() {
      if (!this.data) return;

      this.$refs.cropper.setCropBoxData(JSON.parse(this.data));
    },
    setData() {
      if (!this.data) return;

      this.$refs.cropper.setData(JSON.parse(this.data));
    },
    setImage(e) {
      const file = e.target.files[0];

      if (file.type.indexOf('image/') === -1) {
        alert('Por favor, selecione uma imagem');
        return;
      }

      if (typeof FileReader === 'function') {
        const reader = new FileReader();

        reader.onload = (event) => {
          this.imgSrc = event.target.result;
          // rebuild cropperjs with the updated source
          this.$refs.cropper.replace(event.target.result);
        };

        reader.readAsDataURL(file);
      } else {
        alert('Sorry, FileReader API not supported');
      }
    },
    showFileChooser() {
      this.$refs.input.click();
    },
    zoom(percent) {
      this.$refs.cropper.relativeZoom(percent);
    },
  },
  computed: {
    rotationDegreeComp: {
      get(){
        return this.rotationDegree
      },
      set(env){
        this.rotateTo(env*3.6)
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

input[type="file"] {
  display: none;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0 5px 0;
}

.header h2 {
  margin: 0;
}

.header a {
  text-decoration: none;
  color: black;
}

.content {
  display: flex;
  justify-content: space-between;
}

.cropper-area {
  max-height: 450px;
  max-width: 450px;
}

.actions {
  margin-top: 1rem;
}

.actions a {
  display: inline-block;
  padding: 5px 15px;
  background: #0062CC;
  color: white;
  text-decoration: none;
  border-radius: 3px;
  margin-right: 1rem;
  margin-bottom: 1rem;
}

textarea {
  width: 100%;
  height: 100px;
}

.preview-area {
  width: 307px;
}

.preview-area p {
  font-size: 1.25rem;
  margin: 0;
  margin-bottom: 1rem;
}

.preview-area p:last-of-type {
  margin-top: 1rem;
}

.preview {
  width: 100%;
  height: calc(372px * (9 / 16));
  overflow: hidden;
}

.crop-placeholder {
  width: 100%;
  height: 200px;
  background: #ccc;
}

.cropped-image img {
  max-width: 100%;
}

.img-cropper-skeleton {
  max-width: 350px;
  min-width: 250px;
  max-height: 450px;
  min-height: 250px;
  border-radius: 5px;
  margin: 5px auto;
  background-color: rgba(0,0,0,.3);
}
</style>
