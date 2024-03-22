<script>
import axios from "axios";
import Trip from "./Trip.vue";
import TripText from "./TripText.vue";
import Modal from "./Modal.vue";
export default {
  data() {
    return {
      cities: [],
      trips: [],
      selectedCity: null,
      selectedDate: null,
      filtered: false,
      notSelectedError: false,
    };
  },
  components: {
    "trip-component": Trip,
    "trip-text": TripText,
    "error-modal": Modal,
  },
  mounted() {
    this.getCities();
  },
  methods: {
    async getCities() {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/cities/?format=json"
        );
        const newCities = response.data;
        for (let city of newCities) {
          if (!this.cities.find((c) => c.name === city.name)) {
            this.cities.push(city);
          }
        }
      } catch (error) {
        console.error(error);
      }
    },
    async searchTrips() {
      // Cleaning trips in case its second search
      this.trips = [];

      // Checking if user selected City and Date
      const cityId = this.selectedCity;
      const selectedDate = document.getElementById("dateInput").value;
      if (!this.selectedCity || !selectedDate) {
        this.$emit("show-error");
      } else {
        try {
          const response = await axios.get(
            `http://localhost:8000/api/trips/by_city/${cityId}`
          );
          const newTrips = response.data;

          // Adding every trip to the vue comp. obj. array attribute 'trips'
          let cheapestTrip = null;
          let fastestTrip = null;
          for (let trip of newTrips) {
            trip.duration = parseInt(trip.duration.replace("h", ""));
            // Check if this trip is cheaper
            if (
              !cheapestTrip ||
              trip.price_econ < cheapestTrip.price_econ ||
              trip.price_confort < cheapestTrip.price_confort
            ) {
              cheapestTrip = trip;
            }
            // Check if this trip is faster
            if (!fastestTrip || trip.duration < fastestTrip.duration) {
              fastestTrip = trip;
            }
            this.trips.push(trip);
          }
          for (let trip of this.trips) {
            if (trip.id === cheapestTrip.id) {
              trip.cheaper = true;
            } else {
              trip.cheaper = false;
            }
            if (trip.id === fastestTrip.id) {
              trip.faster = true;
            } else {
              trip.faster = false;
            }
          }
          this.removeSpan();
        } catch (erro) {
          console.error(erro);
        }
        this.filtered = true;
      }
    },
    removeSpan() {
      document.getElementById("notSelected").style.display = "none";
      document.getElementById("clearButton").style.display = "block";
    },
    cleanTrips() {
      this.trips = [];
      this.filtered = false;
      document.getElementById("notSelected").style.display = "block";
      document.getElementById("clearButton").style.display = "none";
    },
  },
};
</script>

<template>
  <div id="container">
    <div id="topBar">
      <img src="../assets/truck.svg" alt="Icone caminhão" />
      <span>Calculadora de viagens</span>
    </div>
    <div id="midlecontainer">
      <div id="leftSide">
        <div id="filters">
          <div id="filtersHeader">
            <img
              src="../assets/hand-coins.svg"
              alt="Hand icon with coins droping on it"
            />
            <span>Calcule o Valor da Viagem</span>
          </div>
          <div id="citySelectContainer">
            <span id="citySpan">Destino</span>
            <select name="city" id="citySelect" v-model="selectedCity">
              <option value="" disabled selected>Escolha uma cidade</option>
              <option v-for="city in cities" :key="city.id" :value="city.id">
                {{ city.name }}
              </option>
            </select>
          </div>
          <div id="dateContainer">
            <span id="dateSpan">Selecione uma data</span>
            <input
              type="date"
              name="date"
              id="dateInput"
              v-model="selectedDate"
            />
          </div>
          <button id="searchButton" @click="searchTrips">Buscar</button>
        </div>
      </div>
      <div id="rightSide">
        <trip-text v-if="filtered" />
        <trip-component
          v-for="(trip, index) in trips"
          :key="index"
          :trip="trip"
          :cheaper="trip.cheaper"
          :faster="trip.faster"
        ></trip-component>
        <span id="notSelected">Nenhum dado selecionado</span>
        <button v-if="filtered" @click="cleanTrips" id="clearButton">
          Limpar
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
#container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}
#clearButton {
  padding: 0.8rem;
  border: none;
  background-color: #f4a532;
  border-radius: 1rem;
  margin-top: 4rem;
  font-weight: 600;
  font-family: sans-serif;
  &:hover {
    cursor: pointer;
  }
}

#topBar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: start;
  background-color: #2b2f42;
  padding: 1.5rem;
  border-top-left-radius: 2rem;
  border-top-right-radius: 2rem;
  width: 70%;

  span {
    color: #fff;
    font-size: 1.5rem;
    margin-left: 1rem;
    font-family: sans-serif;
    font-weight: bold;
  }
}
#midlecontainer {
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 70%;
  background-color: #fafafa;
  padding: 1.5rem;
  border-bottom-left-radius: 2rem;
  border-bottom-right-radius: 2rem;
  margin-top: -1rem;

  #leftSide {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #f4f3f4;
    border-radius: 1rem;
    padding: 2rem;
    width: 35%;
    #filters {
      display: flex;
      flex-direction: column;
      align-items: center;

      #filtersHeader {
        display: flex;
        align-items: center;
        margin-bottom: 4rem;
        margin-top: 3rem;

        span {
          font-family: sans-serif;
          font-weight: 700;
          font-size: 1.2rem;
          margin-left: 0.5rem;
        }
      }

      #searchButton {
        color: white;
        padding: 1rem;
        border-radius: 1rem;
        background-color: #04a8b5;
        font-family: sans-serif;
        font-weight: 600;
        border: none;
        margin-top: 3rem;
        &:hover {
          cursor: pointer;
        }
      }

      #dateContainer {
        display: flex;
        flex-direction: column;
        align-items: start;
        margin-top: 3.5rem;
        width: 100%;

        #dateSpan {
          color: #5a565a;
          margin-bottom: 0.5rem;
        }

        #dateInput {
          padding: 1rem;
          box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
          border: none;
          border-radius: 1rem;
          background-color: #fafafa;
          color: gray;
          width: 90%;
        }
      }
      #citySelectContainer {
        width: 100%;
        #citySpan {
          color: #5a565a;
          margin-bottom: 0.5rem;
        }
        #citySelect {
          width: 100%;
          padding: 1rem;
          border-radius: 0.5rem;
          box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
          border: none;
          margin-bottom: 1rem;
          background-color: #fafafa;
          color: black;
        }
      }
    }
  }
  #rightSide {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    max-width: 80%;
    width: 75%;
    height: 100%;

    #notSelected {
      color: #9d9c9d;
      font-family: sans-serif;
      font-weight: 700;
    }
  }
}
</style>
