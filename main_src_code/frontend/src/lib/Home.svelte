<script>
	import bg1 from "../assets/bg1.jpg";
	import bg2 from "../assets/bg2.jpg";
	import { ImageLoader } from "carbon-components-svelte";
	import Navbar from "./Navbar.svelte";
	import Footer from "./Footer.svelte";

</script>

<Navbar />
<div>
	<ImageLoader src={bg1} alt="bg1"/>
	<div class="mar">
		<h5 class="heading"> OUR NOBEL CAUSE IS:</h5>
		<h2 class="heading"> Make 
			<strong><em>Doctors life</em></strong>
			 a bit easier using AI
		</h2>
	</div>
	<ImageLoader src={bg2} alt="bg2"/>
</div>
<Footer />

<style>
	.mar {
		margin: 10vw;
	}
</style>
