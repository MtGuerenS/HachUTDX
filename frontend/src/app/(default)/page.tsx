import Link from 'next/link'

export default function Home() {

  return (
  <main class="bg-gradient-to-tr from-gray-200 to-gray-100 w-screen h-screen overflow-y-auto">
    <div class="bg-house bg-cover bg-center w-full flex flex-col justify-center items-center" style={{height: "30em"}}>


      <h1 class="bg-gradient-to-tr from-purple-500 to-blue-400 bg-clip-text text-transparent text-8xl p-6 mt-16" style={{fontFamily: `GroovyDay`}}>
        HATCH
      </h1>
      <div>
        <Link href="/Login" class="font-sans font-bold text-2xl bg-gradient-to-tr from-purple-100 to-blue-100 bg-clip-text text-transparent px-6 py-2">
          SIGN IN
        </Link>
      </div>
    </div>

    <div class="bg-gradient-to-tr from-blue-200 to-blue-100 w-screen inline-flex" style={{height: "50vw", maxHeight: "30em"}}>
      <div class="ml-4 mr-2 my-4 bg-gradient-to-tr from-purple-500 to-blue-400" style={{width: "calc(50vw - 2rem)", borderRadius:"20px"}}>
        <div class="font-sans font-medium text-xs text-center h-4 w-24 ml-4 mt-4 pb-6 pt-2 px-2 border border-blue-100 text-blue-100 rounded-full" >
          ABOUT US
        </div>
        <div class="m-4">
          Generate some text
        </div>
      </div>
      <div class="bg-boxes bg-cover bg-center mr-4 ml-2 my-4" style={{width: "calc(50vw - 2rem)", borderRadius:"20px"}} />
    </div>
  </main>
  )
}
