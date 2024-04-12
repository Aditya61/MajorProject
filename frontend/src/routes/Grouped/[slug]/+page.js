export function load({ params }) {
    const slug = params.slug;
    const attrib = slug.slice(0,slug.indexOf(","))
    const val = slug.slice(slug.indexOf(",")+1,slug.length)
    return {
		attrib: attrib,
        val: val
	};
}