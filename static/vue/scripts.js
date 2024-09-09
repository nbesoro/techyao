const pageElement = document.getElementById("page-name");
const page_name = pageElement.getAttribute("data-page-name");

const app = Vue.createApp({
	data() {
		return {
			// Customer
			customers: {},
			customer: {
				first_name: "",
				last_name: "",
				email: "",
				phone: "",
				phone2: "",
				addresse: "",
				postal_code: "",
				city: "",
				gender: "",
			},
			// Categorie
			categories: {},
			category: {
				name: "",
			},
			// Product
			products: {},
			product: {
				category: "",
				name: "",
				ref: "",
				vat: "",
				price: "",
				description: "",
			},
			//
			configs: [],
			message: "Hello world",
			update: false,
			sending: false,
			searchQuery: "",
			// Error
			errors: {},
			on_success: false,
			on_bad_error: false,
			on_server_error: false,
		};
	},
	delimiters: ["{", "}"],
	mounted() {
		this.load_page_list_data();
	},
	methods: {
		load_page_list_data() {
			switch (page_name) {
				case "customer":
					this.load_customers();
					break;
				case "product":
					console.log("You chose a banana.");
					break;
				case "category":
					this.load_categories();
					break;
				default:
					console.log("Unknown fruit.");
					break;
			}
		},
		init() {},
		portPlaceholder() {
			return JSON.parse(this.form.use_tls)
				? "Enter SSL port"
				: "Enter TLS port";
		},
		displayInput() {
			return JSON.parse(this.contact.use_file);
		},
		error_message(key) {
			return this.errors.hasOwnProperty(key) ? this.errors[key] : false;
		},
		post_request(url, data) {
			self.sending = true;
			axios
				.post(url, data)
				.then((response) => {
					self.sending = false;
					this.request_success();
				})
				.catch((error) => {
					self.sending = false;
					this.on_success = false;
					this.request_error(error);
				});
		},
		add_new_customer() {
			this.post_request("/api/customer/", this.customer);
		},
		add_new_category() {
			this.post_request("/api/category/", this.category);
		},
		load_customers() {
			axios
				.get(`/api/customer/?search=${this.searchQuery}`)
				.then((response) => {
					this.customers = response.data;
				})
				.catch((err) => {
					this.customers = {};
					console.log(err);
				});
		},
		load_categories() {
			axios
				.get(`/api/category/?search=${this.searchQuery}`)
				.then((response) => {
					this.categories = response.data;
				})
				.catch((err) => {
					this.categories = {};
					console.log(err);
				});
		},
		load_modal_to_update(c) {
			this.form = c;
			this.update = true;
		},
		load_modal_to_add() {
			this.init();
		},
		// Search
		search_customers() {
			this.load_customers();
		},
		search_categories() {
			this.load_categories();
		},
		// Error Message
		request_error(error) {
			if (error.response) {
				if (error.response.status == 400) {
					this.on_bad_error = true;
					this.errors = error.response.data;
				} else {
					this.on_server_error = true;
				}
			} else if (error.request) {
				console.log("Error request:", error.request);
			} else {
				console.log("Error message:", error.message);
			}
		},
		request_success() {
			this.on_success = true;
			this.on_bad_error = false;
			this.on_server_error = false;
			this.errors = {};
		},
	},
});

// Monter l'application Vue sur l'élément avec l'ID "app"
app.mount("#vue-app");
