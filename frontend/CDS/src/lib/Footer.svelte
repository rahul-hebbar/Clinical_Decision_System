<script>
	import avatar from "../assets/avatar.svg";
	import { 
		Tile,
		ImageLoader,
		Grid,
		Row,
		Column,
		Tag,
		Link
	} from "carbon-components-svelte";
	import LogoGitHub32 from "carbon-icons-svelte/lib/LogoGitHub32";
</script>

<Tile>
	<Grid>
		<Row>
			<Column sm={4} md={6} lg={6}>
				<h3 class="heading">Info About the Developer</h3>
			</Column>
			<Column sm={4} md={8} lg={8}>
				<Tile light>
					<Grid>
						<Row>
							<Column sm={8} md={4} lg={4}>
								<img src={avatar} alt="Profile Pic" class="img">
							</Column>
							<Column sm={8} md={12} lg={12}>
								<h5> Hi!! I'm RAHUL</h5>
								<p> Pursuing Mtech at DIAT Pune </p><br />
								<span>
									Skills:
									<Tag>Full Stack Web Development</Tag>
									<Tag>ML/AI</Tag>
								</span>
							</Column>
						</Row>
					</Grid>
				</Tile>
			</Column>
			<Column sm={8} md={2} lg={2}>
				<div>
					<div class="heading"> My Socials </div><br/>
					<div class="heading">
						<Link href="https://github.com/rahul-hebbar" 
						icon={LogoGitHub32} 
						target="_blank"/>
					</div>
					<hr />
					<div class="credit">
						Image by <u>Gerd Altmann</u>, <u>Gordon Johnson</u> from Pixabay
					</div>
				</div>
			</Column>
		</Row>
	</Grid>
</Tile>


<style>
	.img {
		height: 100px;
		display: block;
		margin-left: auto;
		margin-right: auto;
	}
	.credit {
	  text-align: justify;
	  text-justify: inter-word;
	}
</style>