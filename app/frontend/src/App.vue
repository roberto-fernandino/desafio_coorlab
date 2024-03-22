<script>
import SideBar from "./components/SideBar.vue";
import Prices from "./components/Prices.vue";
import Modal from "./components/Modal.vue";

export default {
  components: {
    SideBar,
    Prices,
    Modal,
  },
  data() {
    return {
      showShopComponent: false,
      showModalError: false,
    };
  },
  methods: {
    onCalcClicked() {
      this.showShopComponent = !this.showShopComponent;
    },
  },
};
</script>

<template>
  <SideBar @calc-clicked="onCalcClicked" />
  <Prices v-if="showShopComponent" @show-error="showModalError = true" />
  <div id="modal" v-if="showModalError">
    <Modal @clean-error="showModalError = false" />
  </div>
</template>

<style scoped>
#modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000; /* Increased z-index */
  background-color: rgba(
    0,
    0,
    0,
    0.5
  ); /* Optional: for semi-transparent background */
}
</style>
