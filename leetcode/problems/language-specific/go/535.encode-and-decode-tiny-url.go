/*
 * @lc app=leetcode id=535 lang=golang
 *
 * [535] Encode and Decode TinyURL
 */

// @lc code=start

const (
	BASE_HOST = "http://tinyurl.com/"
	SEED      = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
)

type Codec struct {
	urlToCode map[string]string
	codeToURL map[string]string
}

func Constructor() Codec {
	rand.Seed(time.Now().UnixNano())
	return Codec{map[string]string{}, map[string]string{}}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	_, longUrlOk := this.urlToCode[longUrl]
	for !longUrlOk {
		code := ""
		for i := 0; i < 6; i++ {
			code += string(SEED[rand.Intn(len(SEED))])
		}

		if _, ok := this.codeToURL[code]; !ok {
			this.urlToCode[longUrl] = code
			this.codeToURL[code] = longUrl
			longUrlOk = true
		}
	}

	return fmt.Sprintf("%v%v", BASE_HOST, this.urlToCode[longUrl])
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	shortUrlSplit := strings.Split(shortUrl, "/")
	return this.codeToURL[shortUrlSplit[len(shortUrlSplit)-1]]
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */

// @lc code=end

