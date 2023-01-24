const svg = document.querySelector("svg");

// const trackLabel = document.querySelector("span.track-label");
// const trackInput = document.querySelector("input.track-input");
const trackCircle = document.querySelector("circle.track");

// const fillLabel = document.querySelector("span.fill-label");
// const fillInput = document.querySelector("input.fill-input");
const fillCircle = document.querySelector("circle.fill");

const pulseCircle = document.querySelector("circle.pulse");

let initialized = false;

const cleanUp = () => {
	initialized = true;

	fillCircle.style.setProperty("--pi", Math.PI);
	pulseCircle.style.setProperty("--pi", Math.PI);

	setTimeout(() => {
		trackCircle.classList.remove("init");
		fillCircle.classList.remove("init");
		pulseCircle.classList.remove("init");
	}, 200);
};

const makePie = () => {
	const percent = parseInt(57);
	const offset = (100 - percent) / 100;

	// fillLabel.textContent = `${percent}%`;
	fillCircle.style.setProperty("--offset", offset);

	if (!initialized) cleanUp();
};

const adjustTrack = () => {
	const width = parseInt(svg.getAttribute("viewBox").split(" ")[3]);
	const track = parseInt(7);
	const radius = (width - track) / 2;
	const diameter = radius * 2;

	// trackLabel.textContent = `${track}`;

	trackCircle.style.setProperty("--track", track);
	trackCircle.setAttribute("r", radius);

	fillCircle.style.setProperty("--track", track);
	fillCircle.setAttribute("r", radius);
	fillCircle.style.setProperty("--diameter", diameter);

	pulseCircle.style.setProperty("--track", track);
	pulseCircle.setAttribute("r", radius);
	pulseCircle.style.setProperty("--diameter", diameter);

	makePie();
};

// fillInput.addEventListener("input", makePie);
// trackInput.addEventListener("input", adjustTrack);
adjustTrack();
